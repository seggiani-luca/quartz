Abbiamo che i [[Router]] sono interconnessi fra di loro e con gli altri [[Apparati di rete]] attraverso [[Cavi]], collegati a **porte** di determinate **interfacce** sul router. In [[Cisco IOS#Configurazione delle interfacce]] avevamo visto come configurare tali interfacce. 

### Connettività in [[Local Area Network]]
Approfondiamo quindi il tipo di connettori fisici che possiamo trovare nei *backplane* nella rete, prima per quanto riguarda la connettività nelle [[Local Area Network]] (quindi gli home network o le reti istituzionali, ecc..):
- *RJ45*: il connettore tipicamente usato per Ethernet su **TP** (*Twisted Pair*), straight-through o cross-over. Deriva da uno standard di origine telefonica (**RJ**, *Registered Jack*), di cui fanno parte anche *RJ11*, *RJ14*, e *RJ25* (rispettivamente per connessioni telefoniche su 1, 2 o 3 linee). ![[rj45.png|800]]
  RJ45 collega 8 linee (4 TP), di cui a seconda dello standard Ethernet vengono usate la metà o tutte per permettere la comunicazione full duplex (coppie Rx+,- e Tx+,-);

![[optic_connectors.png]]

- Connettori **ST** (*Straight Tip*): connettori per la fibra ottica vecchio stile, formati da una punta in ceramica e un sistema di chiusura ad anello. Vengono usati in vecchie installazioni Ethernet ma sono oggi soppiantati da SC e LC (che vediamo subito);
- Connettori **SC** (*Subscriber Connector*): è il connettore che ha soppiantato ST nelle telecomunicazioni (dagli anni '80), e quindi per le trasmissioni su lunghe distanze;
- Connettori **LC** (*Lucent Connector*): sviluppato per essere più compatto e avere minore perdita di SC, usato nelle applicazioni ad alta densità e nei data center (dagli anni '90 circa). 
Notiamo infine che nelle reti in fibra ottica, questi connettori sviluppano le diverse tipologie di cavi:
- *Single mode* per le lunghe distanze a bassa frequenza;
- *Multi mode* per le brevi distanze (e.g. data center) ad alta frequenza.
e le diverse tipologie di applicazione:
- *Simpex* per le comunicazioni in una sola direzione (quindi formati da una sola fibra ottica);
- *Duplex* per le comunicazioni in 2 direzioni simultanee (quindi formati da 2 fibre ottiche parallele). Solitamente questo tipo di connettori è formato da un unica assembly che unisce 2 connettori.

### Connettività in [[Wide Area Network]]
Per quando riguarda la connettività nelle [[Wide Area Network]], connettori per cavi in fibra ottica (o a volte anche Ethernet) vengono comunemente usati. Esistono anche alcuni tipi specifici di cavi usati per collegarsi alle WAN degli ISP:

![[wan_connectors.png]]

- *EIA/TIA-232*, *TIA-439* o *530*, *X.21*, *V.35*, e **HSSI** (*High Speed Serial Interface*): queste erano porte seriale usati in contesti dove esisteva una distinzione fra **DTE** (*Data Terminal Equipment*, sostanzialmente il router della LAN dell'utente) e **DCE** (*Data Communications Equipment*) per il collegamento alla rete dell'ISP. In questo caso, collegavano il router alla **CSU**/**DSU** (*Channel Service Unit* / *Data Service Unit*);
- *RJ11*: usato per i modem **DSL** (*Digital Subscriber Line*) per il collegamento delle home network a Internet sulla linea telefonica;
- *F*: il semplice connettore dell'antenna TV, usato nelle regioni dove c'era internet via cavo sulle linee televisive (ad esempio gli Stati Uniti).
Notiamo che comunque, in questo caso, si parla di reti legacy: la maggior parte delle connessioni Internet su lunga distanza oggi viene fatta in fibra (quindi con connettori come Lucent, Subscriber o Straight Tip) su cavi single-mode.