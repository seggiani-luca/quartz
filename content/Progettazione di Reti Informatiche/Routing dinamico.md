Abbiamo visto come la [[Tabella di routing]] di un [[Router]] può essere disposta attraverso il [[Routing statico]]. Quello che vogliamo accada in verità è che un algoritmo di routing in esecuzione sul router sia quello che popola la tabella di routing. Notiamo che questa non è sempre la soluzione migliore, in quanto abbiamo già detto i pregi del [[Routing statico]], e inoltre:
- Un protocollo di routing può compromettere la tabella;
- Generalmente, si vuole evitare il routing dinamico in situazioni dove la sicurezza è critica;
- Quando un protocollo di routing dinamico è in piedi, bisogna definire *accordi* sul servizio fornito fra **AS** (*Autonomous Systems*) (ad esempio fra le reti di più ISP collegate da **BGP**, *Border Gateway Protocol*), e mettere in piedi anche meccanismi di *load balancing*.

### Tipologie di routing dinamico
Distinguiamo quindi i diversi tipi di routing che possiamo incontrare:
#### Routing dinamico centralizzato
Se si usa l'approccio del routing dinamico **centralizzato**, i calcoli che producono le tabelle di routing attraverso un determinato algoritmo (di *routing*) vengono svolti in maniera centralizzata da una singola unità, che quindi comunica ai router le tabelle che dovranno installare. 
#### Routing dinamico isolato
In questo caso ogni router costruisce la propria tabella di routing in maniera autonoma, senza interagire con gli altri. Questo potrebbe sembrarci un approccio poco valido al routing, ma notiamo che è ad esempio l'approccio usati dagli [[Switch]] [[Ethernet]]: solo osservando i pacchetti e leggendo gli indirizzi MAC, lo switch deduce quale deve essere la sua tabella di routing (più propriamente *switching table*).
#### Routing dinamico distribuito
Sicuramente il caso più interessante, consiste in un algoritmo di routing *distribuito*, che esegue simultaneamente su tutti i router della rete. I router si scambiano informazioni riguardanti la topologia della rete, e sulla base di questa costruiscono autonomamente le loro tabelle di routing.

### Algoritmi di routing dinamico
Esistono diverse tipologie di *algoritmi* che eseguono il routing dinamico, nel caso di routing distribuiti. In particolare questi sono [[Link State]] e [[Distance Vector]].