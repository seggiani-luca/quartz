Iniziamo a vedere le **VLAN**, cioè le *Virtual Local Area Network*, funzionalità degli [[Switch]] che ci permette di isolare semanticamente gruppi di porte fra di loro (cioè non metterli nello stesso spazio di broadcasting).

Il problema di un unico spazio di broadcasting è che:
- Si ha una grande mole di traffico in broadcast sulla rete;
- Ci sono delle problematiche di sicurezza date dal fatto che tutti vedono i pacchetti rivolti a tutti;
- Non si ha separazione semantica delle reti, sopratutto a livello organizzativo (la divisione A riceve i pacchetti della divisione A e della divisione B, ecc...).
Allo stesso modo, avere più reti separate significa più cablaggi, più [[Apparati di rete]], e  quindi maggiori costi.

Una soluzione a questo problema è dato proprio dalle *VLAN*: attraverso queste infatti, si può avere:
- Una singola infrastruttura condivisa ([[Apparati di rete]] e [[Cavi]]);
  Più [[Local Area Network]] logiche, esistenti al di sopra dell'infrastruttura fisica.

### VLAN intra-switch
Le VLAN intra-switch vengono disposte all'interno di un singolo [[Switch]], che permette di raggruppare insiemi di porte in domini di broadcast. Questo approccio però risolve il problema solo in parte, in quanto finché non si raggiunge la porta dello switch, l'infrastruttura non può essere condivisa (non si possono "mischiare" più VLAN sulla stessa linea in arrivo allo switch).

### VLAN trunking
Vogliamo quindi cercare di estendere questo concetto a tutti gli switch della rete, cioè permettere la trasmissione di frammenti appartenenti a più VLAN su una solita linea che connette 2 switch (*trunk*). Abbiamo quindi bisogno di un modo di "decorare" i pacchetti Ethernet che viaggiano nella nostra rete, con informazioni riguardo a non solo *chi* sta inviando il pacchetto e a chi è destinato, ma anche a *quale* VLAN appartiene.

Questo porta ad una tipica conformazione della rete che divide i link in:
- Link *di accesso*, che interconnettono dispositivi fisicamente vicini;
- Link *trunk*, che interconnettono più reti di accesso.
Sia gli switch nei link di accesso che in quelli nei trunk dovremo poter distinguere le VLAN.

Vediamo quindi più soluzioni a questo problema:
- **Frame filtering**: andiamo ad introdurre negli switch una mappa che associa ad ogni indirizzo MAC nella rete, la VLAN di appartenenza. I pro di questo approccio sono il controllo assoluto sulle VLAN, e il supporto immediato per la mobilità degli host (se si sposta un host, la sua entrata nella tabella resta tale). I contro sono invece l'inefficienza del forwarding, e la difficile scalabilità (per ogni nuovo dispositivo si deve introdurre un'entrata nella tabella),
- **Frame tagging**: andiamo ad estendere il pacchetto Ethernet stesso introducendo un *tag* che specifica a quale VLAN appartiene un pacchetto. Esistono più soluzioni che implementano questo meccanismo, fra cui **ISL** (*Cisco Inter-Switch Link*), proprietario CISCO, e l'**IEEE 802.1Q**. Questo meccanismo è molto più scalabile, sia per il controllo che per la gestione (il sistema scala per numero di VLAN anziché numero di utenti). I contro sono che il sistema deve essere interoperabile fra più router, e non c'è alcun supporto di base per la mobilità.

### IEEE 802.1Q
Lo standard **IEEE 802.1Q** è un estensione di Ethernet pensato per supportare le VLAN, col meccanismo del frame tagging, introducendo nei pacchetti (attraverso l'*IEEE 802.3ac*) 4 byte che specificano un *tag* di VLAN su 12 bit. Esiste poi lo standard *IEEE 802.1p* che introduce un meccanismo di *priorità* fra VLAN.

Il pacchetto esteso attraverso *IEEE 802.3ac* (cioè conl'informazione di tagging delle VLAN) contiene la seguente informazione nel campo `type` del pacchetto Ethernet: 

![[ieeeq.png|400]]

Questa in particolare è:
- *TPID*, su 2 byte, che rappresenta una stringa fissa di identificazione del tag VLAN;
- *PCP*, su 3 bit, che rappresenta la classe di priorità della VLAN;
- *DEI*, che sta per *Drop Eligible Indicator*, usato sempre per la gestione della qualità del servizio, in particolare in presenza di sovraccarico della rete (segnala se il frame può essere scartato in caso di overload);
- *VID*, cioè il *VLAN ID* vero e proprio, che sta su 12 bit. Notando che `0x000` e `0xFFF` sono riservati, abbiamo che supportiamo al massimo 4094 VLAN.

Esistono due tipologie di dispositivi VLAN, una volta stabilito lo standard *IEEE 802.Q*:
- **VLAN-aware**, che gestiscono sia frame con tag che senza tag;
- **VLAN-unaware**, che gestiscono solo frame senza tag.
In verità, ad essere VLAN-aware non sono i dispositivi ma le *NIC* dei dispositivi. I dispositivi che montano NIC che implementano lo standard *802.1Q* vengono detti *VLAN-aware*. Un dispositivo utente può quindi essere collegato ad una porta di uno switch che viene associata ad una singola VLAN, quindi senza doversi preoccupare del tagging, oppure può essere VLAN-aware e gestire esso stesso il tagging dei pacchetti.

Abbiamo quindi una distinzione migliore di link di accesso e link trunk:
- Un link *di accesso* è inteso come un link su cui viaggiano frame privi di tag VLAN, secondo quanto detto sopra;
- Un link *trunk* è inteso come un link su cui viaggiano frame con tag VLAN, cioè appartenenti a più VLAN (segnalati appunto dal tag);
- Un link *ibrido*, a questo punto, è un link su cui viaggiano sia frame con tag che senza tag. I frame senza tag in un link ibrido vengono inoltrati ad una *native VLAN* associata al link.
Nella realtà notiamo che non si parla di link, ma di *porte*, cioè appartengono ad un link di accesso, trunk o ibrido, le porte configurate come tali.

Lo standard, nell'implementazione CISCO, supporta più range di ID per le VLAN:
- **Normal Range VLAN**: usate in reti di piccole/medie imprese ed enterprise, sono identificate da un VLAN ID tra 1 e 1005. Gli ID 1 e 1002–1005 sono riservati, creati automaticamente e non possono essere eliminati. Le configurazioni sono salvate in un file database VLAN chiamato `vlan.dat`, nella memoria flash dello switch
- **Extended Range VLAN:** permettono ai service provider di scalare verso più clienti. Sono identificate da un VLAN ID tra **1006 e 4094**. Supportano **meno funzionalità** rispetto alle VLAN normali, e sono salvate nel file di configurazione corrente.

Esistono quindi alcuni tipi di VLAN speciali nei router [[Cisco IOS]]:
- **Default VLAN**: la VLAN preconfigurata per i router CISCO (solitamente VLAN ID 1). Non può essere rinominata o rimossa, e tutte le interfacce ne fanno parte all'avvio del router;
- **Native VLAN**: il traffico su link di tipo ibrido viaggia su questa VLAN quando non ha un tag di VLAN valido. Per motivi di sicurezza, è consigliato che sia una VLAN diversa da quella di default;
- **Management VLAN**: sono di questo tipo tutte le VLAN configurate per accedere alle funzionalità di management di uno switch. Alla *Switch Virtual Interface* (**SVI**) di questa VLAN viene assegnato un indirizzo IP e una maschera di rete. Abbiamo visto un caso di utilizzo delle VLAN di management quando parlavamo della configurazione degli [[Switch]] da remoto al livello 3. Anche qui si consiglia di usare una VLAN diversa da quella di default.

### Configurazione delle VLAN
La configurazione delle VLAN può essere visualizzata con `show running-config` o `show vlan brief` (più sintetico). Per creare una nuova VLAN, quindi, si può usare la modalità di configurazione:
```
S1#configure terminal
S1#vlan <vlan-id>
S1#name <vlan-name>
S1#end
```

A questo punto, per associare una porta ad una VLAN, si procede come già visto in [[Switch#Configurazione di uno switch]]:
```
Sw0#config terminal
Enter configuration commands, one per line. End with CNTL/Z.
Sw0(config)#interface range Fa0/18-24 # seleziona tutti gli switch Fa da 0 a 24
Sw0(config-if-range)#switchport mode <mode> # access, trunk
Sw0(config-if-range)#switchport access vlan <vlan>
```

Nel caso si configuri una porta di tipo *trunk*, poi, notiamo che possiamo configurare la VLAN nativa come:
```
S1(config-if)#switchport trunk native vlan <vlan-id>
```

### DTP
Esiste un protocollo, detto **DTP** (*Cisco Dynamic Trunking Protocol*) che permette la configurazione automatica della tipologia di porte, ovvero gestisce la negoziazione del trunk per stabilire un collegamento trunk tra switch. Ne abbiamo già visto alcune modalità di uso due esempi fa, in `switchport mode <mode> # access, trunk`.

Vediamo quindi un riassunto delle modalità di trunking:
- **access**: porta in modalità accesso (una sola VLAN, niente trunking)
- **trunk**:  porta forzata in trunk (effettua il tagging del traffico VLAN)
- **dynamic auto** (*default su Cisco Catalyst 2960*): può diventare trunk, ma non lo richiede attivamente, ovvero aspetta che sia l’altro lato a iniziare;
- **dynamic desirable**: può diventare trunk e prova attivamente a negoziarlo, ovvero manda richieste per attivare il trunk sull'altro lato.

### Configurazione e gestione dei trunk
Esistono più modalità di gestione del trunking, che non deve per forza essere manuale:
- **Statica**: le VLAN consentite (_allowed VLANs_) sono configurate manualmente su ogni porta trunk. Questo è il tipo di configurazione che abbiamo visto finora;
- **Dinamica**: le VLAN consentite sono determinate automaticamente dagli switch  e comunicate tra loro attraverso i link trunk. La configurazione dinamica richiede un apposito protocollo di comunicazione tra switch:
	- **Proprietario:** *Cisco Virtual Trunking Protocol* (**VTP**);
	- **Standard IEEE 802.1Q:** *Multiple VLAN Registration Protocol* (**MVRP**).