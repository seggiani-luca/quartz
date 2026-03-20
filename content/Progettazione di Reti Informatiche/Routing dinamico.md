Abbiamo visto come la [[Tabella di routing]] di un [[Router]] può essere disposta attraverso il [[Routing statico]]. Quello che vogliamo accada in verità è che un algoritmo di routing in esecuzione sul router sia quello che popola la tabella di routing. Notiamo che questa non è sempre la soluzione migliore, in quanto abbiamo già detto i pregi del [[Routing statico]], e inoltre:
- Un protocollo di routing può compromettere la tabella;
- Generalmente, si vuole evitare il routing dinamico in situazioni dove la sicurezza è critica;
- Quando un protocollo di routing dinamico è in piedi, bisogna definire *accordi* sul servizio fornito fra **AS** (*Autonomous Systems*) (ad esempio fra le reti di più ISP collegate da **BGP**, *Border Gateway Protocol*), e mettere in piedi anche meccanismi di *load balancing*.

