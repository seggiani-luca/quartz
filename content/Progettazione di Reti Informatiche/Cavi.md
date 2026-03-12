Gli [[Apparati di rete]] non potrebbero essere connessi se non attraverso **cavi**. Questi rappresentano quindi componenti importanti della rete, importanti al punto che simulatori come [[Cisco Packet Tracer]] ne supportano diverse tipologie adatte a diversi casi di applicazione.

### Cablaggio in rame
Lo standard Ethernet si è evoluto negli anni per supportare larghezze di banda sempre maggiori (sopratutto per fare competizione alle diverse altre tecnologie che sono state proposte nel tempo, fra cui ad esempio **ATM** (*Asynchronous Transfer Mode*). La maggior parte dei cavi che ha supportato nella sua evoluzione sono stati in **rame**.

![[ethernet_evol.png|800]]

I cavi Ethernet in rame sono terminati da connettori RJ45 (vedere [[Interfacce e porte#Connettività in Local Area Network]]), a 8 linee (4 **TP**, *Twisted Pair*), di cui a seconda dello standard vengono usate la metà o tutte per permettere la comunicazione full duplex (coppie Rx+,- e Tx+,-). A seconda di come vengono disposte le TP (i comuni doppini telefonici in rame) si distinguono i tipi:
- **UTP** (*Unshielded Twisted Pair*): formato da 4 doppini terminati da connettori RJ45. I doppini vengono avvolti da una guaina esterna (per solidità strutturale e un livello minimo di protezione);
- **STP** (*Shielded Twisted Pair*): in questo caso si dispongono 2 livelli di protezione aggiuntiva dall'interferenza elettromagnetica: una guaina metallica per le 4 coppie di cavi che formano il doppino, e una guaina per ogni doppino. Questo rende i cavi STP più affidabili e sicuri, ma anche più costosi e complicati da installare.
La IEEE si occupa di stabilire gli standard per il cablaggio in rame di Ethernet. In particolare, alcuni standard sono:

![[ethernet_cat.png|400]]

- Cavi *Categoria 3* (**Cat3**): doppini senza guaina interna, non avvolta;
- Cavi *Categoria 5/5e* (**Cat5/5e**): doppini avvolti (per maggiore riduzione del rumore in common mode);
- Cavi *Categoria 6* (**Cat6**): doppini avvolti con guaina per doppino.

### Cavi straight-through e cross-over
Per collegare fra di loro diversi [[Apparati di rete]], anche in simulatori come [[Cisco Packet Tracer]], dobbiamo fare attenzione alle tipologie di apparecchiatura che si va a collegare, e quindi ai cavi utilizzati. In particolare, esistono 2 tipologie di cavi in rame (Ethernet) pensate per scopi diversi:
- **Straight-through**: in questo caso i cablaggi dei due connettori RJ45 sono diretti. Visto che Ethernet è full duplex, quindi ha linee Rx e Tx sullo stesso cavo, questo significa che le linee Rx si collegano con le linee Rx e le linee Tx si collegano con le linee Tx. Ciò funziona per apparecchiature che si aspettano una tale configurazione, e quindi per collegare router a switch, o switch a dispositivi terminali, ecc...
- **Cross-over**: in questo caso i cablaggi dei due connettori RJ45 sono invertiti. Questo significa che le linee Rx si collegano con le linee Tx e le linee Tx si collegano con le linee Rx. Ciò funziona per collegare apparecchiature ad apparecchiature dello stesso tipo, e quindi per collegare router a router, switch a switch, ecc... Il funzionamento è sempre lo stesso: l'apparecchiatura A invia su Tx aspettando che l'altra stia ascoltando sulla stessa linea, mentre l'altra di default sarebbe pronta a scrivere sulla stessa linea. Invertendo le linee si manda il segnale di una all'Rx dell'altra, e così via.

### Cablaggio in fibra ottica
La **fibra ottica** permette di ottenere velocità di trasmissione molto più grandi di Ethernet su rame, anche se a costi maggiori. In questo caso, il segnale non viaggia su conduttori in rame ma sotto forma di segnali luminosi: questi possono viaggiare venendo riflessi dalle pareti del cavo, solitamente in vetro. Fra le altre cose, i segnali ottici sono completamente immuni all'interferenza elettromagnetica. 
Una conseguenza dell'uso della fibra è che ogni cavo è di default in modo simplex: per ottenere la comunicazione duplex abbiamo bisogno di affiancare due linee parallele (e quindi 2 connettori paralleli, vedere [[Interfacce e porte#Connettività in Wide Area Network]]).

![[fiber_single_multi.png|400]]

Esistono 2 tipologie di cavo in fibra ottica:
- **Single-mode**: lo spazio vuoto che conduce il segnale luminoso è molto piccolo (ordine dei 9 micron). Questo permette una grande focalizzazione del segnale, e quindi maggiori distanze di copertura, a costo di velocità ridotte. Per questo motivo vengono usati in link a lunghe distanze (sottomarini, inter-city);
- **Multi-mode**:  lo spazio vuoto che conduce il segnale luminoso è più grande (ordine dei 50 micron). Questo permette una grande velocità di trasmissione, a costo di minore distanza di copertura. Per questo motivo vengono usati in applicazioni ad alta frequenza (come ad esempio nei data center).