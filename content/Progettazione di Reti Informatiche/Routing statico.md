Abbiamo visto le specifiche del *routing* e di come è disposta la [[Tabella di routing]] di un router. Abbiamo che a volte vogliamo configurare manualmente le entrate della tabella di routing, cioè definire le cosiddette **route statiche**. Questo può essere utile in quanto:
- Il routing statico definisce esplicitamente le route su cui devono passare i pacchetti (ad esempio è utile);
- Permette di costringere il traffico a passare attraverso middlebox come *firewall*;
- Permette ai pacchetti di viaggiare attraverso zone sicure della rete;
Per questo è indicato quando si progettano parti che devono restare fisse della rete, o ad esempio quando si collegano le [[Local Area Network]] dei clienti ad un ISP (i cosiddetti *stub network*, che non collegano ad altro). Di contro, collegare una route arbitraria ad uno stub network sarebbe probabilmente un errore, in quanto forzerebbe il traffico verso un vicolo cieco.

### Design delle route statiche
Nel caso si decida di usare il routing statico su una rete, bisogna svolgere i seguenti passaggi:
1. *Progettare* il cosiddetto **piano di routing**, cioè decidere (noti gli IP allocati o le interfacce dei router) quali saranno le route vere e proprie che definiranno la rete. Questo può essere fatto in svariati modi, noto che l'obiettivo finale è quello di ottimizzare i percorsi dei pacchetti su un grafo. Notiamo che in questo caso è fondamentale progettare il piano di routing perché non vi siano *cicli*: se un algoritmo di [[Routing dinamico]] è capace di rilevare i cicli, il routing statico non lo è, e i pacchetti bloccati in un ciclo restano nel ciclo finché non viene annullato il loro **TTL** (*Time To Live*). Quindi nella realtà questi vengono scartati;
2. *Configurare* i router sulla rete con le route statiche della rete. Anche qui valgono tutti gli accorgimenti noti in [[Cisco IOS]] e riguardo alla [[Tabella di routing]] per visualizzare e modificare la tabella di routing. In particolare, vediamo sotto come introdurre una nuova route statica nella [[Tabella di routing]] di un router.

### Configurazione di route statiche
Il tipo più semplice di percorso che possiamo configurare in un router è un percorso **statico**. Questo è un'associazione fissa fra l'indirizzo IP della sottorete destinataria e la porta di uscita del router, senza alcun tipo di TTL.

Per configurare route statiche fra router, quindi accediamo alla modalità di configurazione globale e aggiungiamo il percorso specificando:
- La *sottorete* di destinazione, e quindi anche la sua maschera (usata per il longest prefix matching);
- L'indirizzo di *next hop* per l'accesso a tale sottorete. Questo verrà quindi tradotto in una porta fisica, situata sempre sullo stesso router, corrispondente ad una delle sue porte di uscite (che ricordiamo configuriamo con `config terminal`, e quindi `interface`).

Il comando nel complesso ha quindi una sintassi simile alla seguente:
```
Router_A(config)#ip route 223.223.223.0 255.255.255.0 111.111.111.2
Router_B(config)#ip route 222.222.222.0 255.255.255.0 111.111.111.1
```

### Evitare i cicli
I cicli sono garantiti essere evitati se viene utilizzato l'albero dei cammini minimi (*shortest-path tree*) verso ogni rete di destinazione per ciascun router. Per grafi orientati con pesi non negativi, l'albero dei cammini minimi è calcolato tramite l'*algoritmo di Dijkstra* (quello che usano algoritmi di routing come **OSPF**, *Open Shortest Path Fist*). Se vengono definiti alcuni vincoli aggiuntivi sulla rete (ad esempio: non utilizzare un certo collegamento per i percorsi primari, ecc...) la situazione si complica. Viene allora definito e risolto (mediante opportune euristiche) un albero dei cammini minimi vincolato (*constrained shortest-path tree*)..