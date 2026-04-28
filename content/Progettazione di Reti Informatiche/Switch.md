Un **router** è un dispositivo di livello *datalink* (vedere [[Modello OSI]]) che si occupa dell'instradamento di frame di livello *datalink* (solitamente [[Ethernet]]). In particolare è:
- Dispositivo di livello 2 (collegamento dati) del modello OSI;
- Collega dispositivi all’interno della stessa [[Local Area Network]];
- Inoltra i frame in base agli indirizzi **MAC** (*Medium Access Control* );
- Può supportare **VLAN** (*Virtual LAN*, vedere [[Local Area Network]]), **PoE** (*Power of Ethernet*), gestione (managed switch).
Il sistema operativo per switch Cisco è il solito [[Cisco IOS]] che abbiamo visto anche per i router.

### Recap sul LAN switching
Veniamo a discutere un argomento già visto a reti informatiche, cioè come si svolge lo scambio di pacchetti su una [[Local Area Network]] Ethernet con hub o switch.

#### Hub
- Ogni PC su una rete LAN avrà una scheda di rete (**NIC**, *Network Interface Card*), che risponderà ad un dato indirizzo **MAC** (*Medium Access Control*);
- Di base, che ci sia un *hub* o uno *switch*, il mezzo Ethernet deve essere assunto come *condiviso*, per cui ogni PC dovrà essere pronto a ricevere messaggi rivolti a sé stesso (quindi da accettare) e rivolti ad altri (quindi da scartare);
- Questa configurazione significherà che il dominio di *collisione* della rete è la stessa cosa del dominio di *trasmissione*, cioè quando si va a trasmettere sul mezzo condiviso si va potenzialmente in collisione con altri dispositivi sulla stessa LAN.
Questa era la visione di Ethernet anni fa, quando ancora non erano diffusi gli switch, e tutto veniva fatto con hub (replicatori di segnale passivi) e cavi coassiali.

#### Switch
La grande rivoluzione di Ethernet è quella degli *switch*, che permettono appunto di separare il dominio di collisione da quello di trasmissione introducendo al centro della rete una componente attiva.
- Ogni PC avrà sempre una NIC e un codice MAC assegnatogli;
- La differenza sarà nel fatto che il mezzo sarà assunto sì condiviso, ma ogni connessione punto-punto fra PC e switch sarà effettivamente isolato. Questo significherà che il singolo PC in trasmissione non potrà incontrare collisione, ma avrà una via di comunicazione diretta con lo switch dove non potrà incappare in collisioni con altri PC. Diciamo che il dominio di *collisione* della rete si riduce al solo link fra PC e switch, mentre il dominio di *trasmissione* resta esteso all'intera rete LAN. Chiamiamo questo processo anche *transparent bridging*;
- Lo switch potrà quindi portare avanti un processo di *self-learning* della topologia di rete. Questo significherà che i pacchetti rivolti ad ogni PC verranno consegnati solo al PC destinatario (dopo un opportuno processo di apprendimento), diminuendo la congestione e aumentando privacy e sicurezza (notando che il mezzo va comunque assunto come condiviso, serve crittografia per pacchetto nel caso di dati sensibili). 

### Database MAC
Uno switch per funzionare (cioè per implementare il *self-learning* che abbiamo nominato sopra) ha bisogno di un *MAC address database*, cioè un database degli indirizzi MAC dei dispositivi che lo switch stesso serve. Ad ogni indirizzo MAC vorremo associare altra informazione utile, fra cui:
- Chiaramente l'*indirizzo MAC* stesso;
- L'id della *porta* a cui il dispositivo con tale MAC è collegato allo switch;
- L'id della *VLAN* a cui il dispositivo deve appartenere, usato per fornire il meccanismo delle VLAN (non si fa switching trasparente fra dispositivi appartenenti a VLAN diverse, ma si delega lo switching al router);
- Il *tipo* di dispositivo, che potrà essere *statico* (configurato per restare nello switch) o *dinamico* (appreso in maniera dinamica e soggetto ad essere rimosso nel caso di obsolescenza);
- L'*ageing*, che indica il tempo da cui è stato appreso l'indirizzo MAC, chiaramente utile nel caso di dispositivi dinamici;
- Stato *STP*, dove **STP** (*Spanning Tree Protocol*, già visto in [[Cisco Packet Tracer#Tipi di evento]]) è un protocollo specifico per il rilevamento di cicli e la riduzione della topologia di rete ad un albero di copertura per gli switch.

### Meccanismo di switching
Il processo di switching di uno switch si riassume quindi come segue:

![[switch_switching.png]]

In serie:
1. Prima riceviamo un frame sulla porta $x$, controlliamo errori, e nel caso ce ne siano lo scartiamo;
2. Se la porta $x$ è configurata per il forwarding, trattiamo il pacchetto, altrimenti lo scartiamo comunque;
3. Controlliamo se abbiamo l'indirizzo MAC destinazione nel database degli indirizzi MAC:
4. In caso affermativo controlliamo di non aver ricevuto il pacchetto dal suo destinatario, e in lo inoltriamo;
5. In caso negativo operiamo in *flooding*, cioè senza ulteriori informazioni possiamo solamente inoltrare su tutte le porte.

### Meccanismo di learning
Il processo di learning si riassume invece come segue:

![[switch_learning.png]]

Cioè in sequenza, quando riceviamo un pacchetto:
- Controlliamo se conosciamo la sorgente, cioè se l'indirizzo MAC sorgente è nel nostro database degli indirizzi MAC;
- In caso negativo lo salviamo nel database e resettiamo il suo tempo di ageing;
- In caso affermativo controlliamo invece se non conoscevamo già tale MAC ma ad una porta diversa (ad esempio nel caso in cui un dispositivo è stato spostato su una porta diversa), e in tal caso aggiorniamo la corrispondente entrata nel database. Altrimenti non facciamo nulla, e in entrambi i casi resettiamo il tempo di ageing.

### Configurazione di uno switch
Abbiamo quindi detto che gli switch usano lo stesso sistema operativo [[Cisco IOS]] a cui siamo abituati. 

Notiamo che di default gli switch sono dispositivi che operano al livello 2 (datalink), per cui potremmo chiederci come si fa a fare una configurazione remota su TCP/IP. Ebbene negli switch moderni è possibile configurare un interfaccia di tipo VLAN, su cui configurare un indirizzo IP. Si può quindi configurare un gateway di default, e quindi procedere a collegarsi al router attraverso TCP/IP.

```
S1#configure terminal
S1(config)#interface vlan 1
S1(config-if)#ip address 172.17.99.2 255.255.255.0
S1(config-if)#no shutdown
S1(config-if)#exit
S1#ip default-gateway 172.17.99.1
S1#end
```

Un esempio di configurazione di base di un interfaccia potrà quindi essere il seguente:
```
S1#configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
S1(config)#interface Fa0/1
S1(config-if)#duplex ?
auto Enable AUTO duplex configuration
full Force full duplex operation
half Force half-duplex operation
S1(config-if)#speed ?
10 Force 10 Mbps operation
100 Force 100 Mbps operation
auto Enable AUTO speed configuration
S1(config-if)#mdix ?
auto Enable automatic MDI crossover detection on this interface
S1(config-if)#end
```

Qui quello che abbiamo fatto è:
- Entrare nella modalità di configurazione da terminale;
- Configuriamo la modalità duplex di un interfaccia;
- Configuriamo la sua velocità;
- Configuriamo l'**MDIX**, che è un protocollo per il rilevamento automatico del tipo di cavo (crossover o straight-through) connesso ad una data porta.

Vediamo quindi la gestione della tabella MAC. Con `show mac-address-table` visualizziamo i contenuti attuali della tabella:
```
Switch#show mac-address-table
Mac Address Table
-------------------------------------------
Vlan Mac Address Type Ports
---- ----------- -------- -----
99 0003.e4ea.0b02 DYNAMIC Fa0/5
99 00d0.baed.1acb DYNAMIC Fa0/18
```

Possiamo configurare, come abbiamo anticipato, entrate di tipo statico nella tabella MAC, con il comando:
```
Switch(config)#mac-address-table static mac_address vlan vlan-id interface-id
```
e possiamo quindi configurare il tempo di ageing da usare in una certa VLAN (o ovunque) con il comando:
```
Switch(config)#mac-address-table aging-time seconds [vlan vlan_id]
```

Notiamo che il valore di default del parametro di ageing è 300 secondi. Variare questo parametro comporta delle questioni da considerare:
- Se l'ageing è troppo basso, lo switch si dimentica velocemente gli indirizzi imparati, e quindi nella maggior parte dei casi si comporta come hub, con tutte le relative inefficienze;
- Se l'ageing è invece troppo alto, lo switch rimane troppo legato alle configurazioni che rileva, e non è capace di adattarsi velocemente a cambiamenti della topologia di rete (ad esempio se si disconnette un dispositivo).

### Sicurezza per gli switch
Iniziamo a trattare la *sicurezza* negli switch introducendo un tipo di attacco comune.

#### MAC address flooding
Un malintenzionato potrebbe compromettere la funzionalità di uno switch collegandosi ad una porta e iniziando a diffondere pacchetti con indirizzi MAC fasulli. Questo porta lo switch ad imparare gli indirizzi MAC forniti (vedere sopra, [[Switch#Meccanismo di learning]]), e quindi la tabella MAC a riempirsi. Una volta che la tabella MAC è piena lo switch, come abbiamo detto, non è più capace di effettuare l'isolamento dei domini di collisione e ritorna ad essere un hub, con tutte le problematiche che abbiamo discusso.

Per risolvere problemi di questo tipo sono predisposti meccanismi di *port security*, che limitano il numero di indirizzi MAC validi che si possono ricevere su una data porta. I pacchetti con un indirizzo sorgente all'infuori di quelli concessi su una porta non vengono inoltrati. Esistono diversi tipi di indirizzi MAC validi configurabili:
- *Statici*, configurati manualmente, salvati nella tabella dei MAC e quindi nella configurazione. Ovviamente questi sono assunti validi;
- *Dinamici*, appresi in maniera dinamica, e allocati nella tabella dei MAC. Non vengono salvati nella configurazione e devono essere imparati di nuovo al riavvio dello switch;
- *Sticky* ("appiccicosi"), appresi sempre in maniera dinamica, e allocati sia nella tabella dei MAC che nella configurazione corrente. Vengono quindi ricordati anche dopo un riavvio.

In [[Cisco IOS]] la configurazione della port security può essere fatta come segue:
```
Sw1#configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
Sw1(config)#interface fa0/18
Sw1(config-if)#switchport mode access
Sw1(config-if)#switchport port-security ?
mac-address Secure mac address
maximum Max secure addresses
violation Security violation mode
<cr>
Sw1(config-if)#switchport port-security
Sw1(config-if)#switchport port-security maximum ?
<1-132> Maximum addresses
Sw1(config-if)#switchport port-security maximum 5
Sw1(config-if)#switchport port-security mac-address ?
H.H.H 48 bit mac address
sticky Configure dynamic secure addresses as sticky
Sw1(config-if)#switchport port-security mac-address sticky
Sw1(config-if)#end
```
dove in ordine:
- Abbiamo configurato la port security su un interfaccia (FastEthernet `fa 0/18`);
- Abbiamo configurato il numero massimo di indirizzi concessi sull'interfaccia;
- Abbiamo configurato quell'interfaccia come *sticky*.

Possiamo configurare anche la *switch security*, cioè le regole a livello di switch che usiamo per gestire le interfacce che hanno violato le regole di *port security*. Le politiche che possiamo configurare sono:
- *Protect*, ignora la violazione (senza allocare il MAC superfluo ricevuto nella tabella dei MAC);
- *Restrict*, incrementa un contatore di violazioni per l'interfaccia ed invia un messaggio di log;
- *Shutdown*, disabilita l'interfaccia completamente.

In [[Cisco IOS]] configurazione della sicurezza di switch si fa quindi come:
```
Sw1#configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
Sw1(config)#interface fa0/18
Sw1(config-if)#switchport mode access
Sw1(config-if)#switchport port-security
Sw1(config-if)#switchport port-security maximum 5
Sw1(config-if)#switchport port-security mac-address sticky
Sw1(config-if)#switchport port-security violation ?
protect Security violation protect mode
restrict Security violation restrict mode
shutdown Security violation shutdown mode
Sw1(config-if)#switchport port-security violation restrict
Sw1(config-if)#end
```
dove in ordine abbiamo:
- Configurato il numero massimo di MAC per porta a livello globale, e il tipo di indirizzi validi (come sticky);
- Configurato il tipo di gestione delle violazioni, come restrict.
Abbiamo quindi il comando `show port-security interface <interfaccia>` per visualizzare le impostazioni di sicurezza configurate su una singola porta.