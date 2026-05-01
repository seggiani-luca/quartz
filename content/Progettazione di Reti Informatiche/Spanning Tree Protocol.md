Lo *Spanning Tree Protocol* (**STP**) è un protocollo in esecuzione dagli [[Switch]] che ho l'obiettivo di eliminare gli *anelli* nelle reti di livello 2, in maniera tale da creare una rete overlay rappresentante un *albero di copertura* della rete di livello 2 stessa. Questo è fatto in quanto in una rete di livello 2, dove gli switch si comportano in qualche modo da *replicatori* di pacchetti, la presenza di anelli porta a ciclaggio infinito dei pacchetti sulla rete, o frame unicast duplicati (cosa chiaramente non desiderata).

Le topologie di rete di livello 2 che contengono cicli sono tipiche nel caso si progettino reti *ridondanti*, cioè dove si hanno connessioni multiple a più switch (di cui uno principale e più secondari, nel caso il primo fallisca).

### Funzionamento
L'idea di base di STP è quella di bloccare alcuni link appositamente selezionati in maniera da formare una rete overlay che rappresenti un albero di copertura. STP è un protocollo completamente distribuito, che attraversa 3 fasi:
1. Selezione del *root bridge* (che è lo switch radice dell'albero);
2. Selezione delle *porte root*, cioè quelle che comunicano col root bridge;
3. Selezione delle *porte designate*, distinte dalle *porte alternate*, che vengono disabilitate.

#### Selezione del root bridge
La comunicazione fra switch con STP in esecuzione si fa attraverso lo scambio di **BDPU** (*Bridge Protocol Data Unit*). Questi sono particolari pacchetti che contengono:
- **Flag**: rappresentano se il pacchetto è di tipo *TC* (*Topology Change*) o *TCA* (*Topology Change Acknowledgment*);
- **Root ID**: l'identificatore dell'(eventuale candidato) root bridge;
- **Bridge ID**: l'identificatore dello switch che invia la BPDU;
- **Root path cost**: costo del percorso dallo switch che invia la BPDU al root bridge;
- **Port ID**: identificatore della porta attraverso la quale il BPDU viene inviato dallo switch che lo invia;
- **Message age**: tempo trascorso da quando lo switch ha emesso il primo BPDU di configurazione;
- **Max age**: tempo massimo di validità, oltre il quale il processo STP va riavviato;
- **Hello time**: tempo fra due BPDU inviati (solitamente 2 secondi);
- **Forward delay**: controlla le transizioni dello stato delle porte.

I Root Bridge quindi, dal loro avvio inviano agli switch adiacenti questi BPDU ogni 2 secondi per aggiornarsi sullo stato della rete (solo i Root Bridge *iniziano* lo scambio di BPDU). All'avvio, ogni switch è convinto di essere il root bridge (quindi si fa elezione). Se uno switch riceve un BPDU con un Root ID più basso:
- Aggiorna il Root ID interno;
- Aggiorna il costo del percorso verso la root aggiungendo il costo della porta su cui ha ricevuto il BPDU (ingress port);
- Usa il nuovo Root ID e il nuovo costo nei BPDU successivi che invia su tutte le porte.
Dopo un po’ di tempo, solo uno switch continuerà a generare BPDU con Root ID uguale al proprio Bridge ID: quello è il root bridge eletto.

Notiamo poi che un ID per uno switch è rappresentato da 2 byte di priorità e 6 byte di indirizzo MAC dello switch. Esiste uno standard esteso di Cisco che divide i 2 byte di priorità in 4 bit di priorità, e 12 bit di *Extend System ID* (permette di distinguere più istanze di STP per VLAN, come vedremo fra poco).

#### Selezione delle porte root
Anche le porte root (*root port*) vanno decise in parallelo con l'elezione del Root Bridge. La **root port** è la porta dello switch con il minor costo di percorso (*path cost*) verso il Root Bridge. Ogni switch ha una sola root port, tranne il Root Bridge (che non ne ha). Il root path cost associato a una porta è:
$$
\text{costo verso root} + \text{costo link porta root}
$$
Lo spareggio sullo switch che si usa per raggiungere il root si fa sui BPDU ricevuti (che contengono anche il costo verso root che associamo alla porta):
1. BPDU ricevuto con il Bridge ID più basso;
2. BPDU ricevuto con il Port ID più basso.
Come abbiamo detto, questo processo avviene *in parallelo* con l’elezione del root bridge.
- I path cost vengono aggiornati durante lo scambio dei BPDU;
- La root port viene scelta di conseguenza;
- La root port può cambiare più volte prima della convergenza STP.

#### Selezione delle porte designate
Infine, c'è la configurazione delle porte designate (*designated ports*), cioè quelle che vengono mantenute attive da STP. Il Root Bridge configura tutte le sue porte come designated ports. Se uno switch non riceve BPDU su una porta non-root, quella porta viene configurata come designated (forwarding). Se invece lo switch riceve BPDU su una porta non-root, si attiva una *competizione* per la designazione della porta. Su ogni segmento LAN deve esserci una sola designated port non-root, altrimenti si crea un anello. La competizione è vinta dalla porta che trasmette il BPDU con priorità più alta. La priorità è determinata dalla tupla minima:
```
<root path cost, bridge ID, port ID>
```
Quindi, la porta vincente diventa designated port (forwarding). Tutte le altre porte diventano *alternate ports* (stato blocking).

### Configurazione di STP
Per vedere lo stato attuale del protocollo STP su un bridge (switch) si può usare il comando `show spanning-tree`.

Per configurare la priorità di un singolo router, dalla modalità di configurazione globale si può usare il comando:
```
C1(config)#spanning-tree vlan <vlan> priority <priority>
```
dove è necessario fornire anche la VLAN in quanto il protocollo STP viene eseguito separatamente per ogni dominio di broadcast. Questo significa che, idealmente, si potrebbe avere un diverso Root Bridge per ogni VLAN nella nostra rete.

### Protocolli alternativi a STP
Esistono alcuni protocolli alternativi ad STP, fra cui ricordiamo:
1. **RSTP** (*Rapid Spanning Tree Protocol*): ha una convergenza più veloce e reagisce ai cambiamenti della rete entro 3 tempi di Hello ($2 \times 3 = 6$ secondi) oppure entro poche centinaia di millisecondi in caso di guasto fisico di un link. Richiede alcune assunzioni: tutti gli switch devono eseguire RSTP e i collegamenti tra switch devono essere di tipo point-to-point. È stato inizialmente standardizzato come *IEEE 802.1w* ed è ora incluso in *IEEE 802.1D-2004*, che sostituisce lo STP originale;
2. **MSTP** (*Multiple Spanning Tree Protocol*): introduce un approccio per-VLAN configurando uno spanning tree separato per ogni gruppo di VLAN. È stato inizialmente standardizzato come *IEEE 802.1s* ed è ora incluso in *IEEE 802.1Q-2005*;
3. Varianti **STP** proprietarie Cisco, fra cui *Per-VLAN STP* (**PVST**), *Per-VLAN STP Plus* (**PVST+**, lo vediamo sotto), *Rapid-PVSTP+*, ecc...
4. **PVST+** (*Per-VLAN STP Plus*): supporta il trunking *IEEE 802.1Q*, e istanze STP dedicate per VLAN (sostanzialmente è un MSTP proprietario di Cisco). Sfrutta l'*Extend System ID* che abbiamo visto poco fa, e permette una configurazione particolarmente flessibile della rete.