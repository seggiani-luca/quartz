Un **router** è un dispositivo di livello *network* (vedere [[Modello OSI]]) che si occupa dell'instradamento di pacchetti IP. In particolare è:
- Dispositivo di livello 3 (rete) del modello OSI;
- Collega reti diverse e instrada i pacchetti IP tra di esse;
- Usa tabelle di routing e protocolli (es. statico, dinamico);
- Può fare **NAT**, **DHCP**, e firewall di base (vedere [[Indirizzamento IP]]);
- Tipicamente collega le [[Local Area Network]] a Internet ([[Wide Area Network]]).

Nello specifico, i router sono i dispositivi che si trovano al confine delle [[Local Area Network]], e che si occupano quindi di connettere più [[Local Area Network]] fra di loro attraverso il cosiddetto processo di *routing*. I collegamenti che collegano i singoli router rispettano diversi protocolli, e sono di tipo *punto-punto*.

Abbiamo che i router sono a tutti gli effetti computer estremamente specializzati (specializzati ad inviare pacchetti sulla rete). Il loro compito, come anticipato dal corso di reti informatiche, è duplice:
- A livello **data plane**, quello di effettuare il *forwarding* dei pacchetti (ottenuti dalle porte di entrata) verso le loro destinazioni attraverso le porte di uscita;
- A livello **control plane**, eseguire un *algoritmo di routing* e quindi selezionare il percorso migliore per i pacchetti. Ricordiamo che il *control plane* può essere implementato in 2 modi: il metodo tradizionale è quello di implementare algoritmi di routing *distribuiti* (ad esempio **OSPF**, *Open Shortest Path First*, **RIP**, *Routing Information Protocol*, **BGP**, *Border Gateway Protocol*, ecc...); il secondo metodo è quello del cosiddetto **SDN** (*Software Defined Networking*), che si basa sull'esistenza di un sistema centralizzato di gestione delle tabelle di routing per tutti i router di un *autonomous system*.

Come tutti i computer, quindi, i router sono dotati di memoria, CPU, e loro particolarità, un sistema di I/O estremamente specializzato (ed estremamente veloce) composto dalle porte di ingresso e uscita (solitamente di tipo [[Ethernet]]) su cui viaggiano i pacchetti (a tal proposito, [[Interfacce e porte]]).  Vediamo ad esempio il *backplane* di un router Cisco serie 1800 per vedere il tipo di interfacce di cui ha bisogno:
![[router_backs.png|400]]

Su un router, per abilitare la sua operazione, è solitamente in esecuzione un *sistema operativo per router*, come ad esempio [[Cisco IOS]].