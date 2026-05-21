Uno dei punti chiave delle reti che abbiamo sollevato in [[Reti informatiche]] è quello della *affidabilità e alta disponibilità*. Il meccanismo del *default gateway* viola in principio il concetto di *affidabilità*, in quanto nel caso di fallimento del [[Router]] al primo hop, si ha che gli host sono incapaci di raggiungere Internet.

Lato ISP, però, nulla ci vieta di avere più di un router connesso ad Internet. Infatti, i protocolli di routing in esecuzione sulla loro rete rileveranno automaticamente se una delle porte dei nostri router fallisce, e reindirizzeranno il traffico ad una porta valida dello stesso o di un altro router.

Il problema sta quindi nel come comunicare agli host sulla rete la presenza di uno o più router gateway di backup rispetto al default gateway. L'idea è di usare un **router virtuale**, cioè di permettere a più router di rispondere a richieste allo stesso gateway. Chiaramente avremo bisogno di un protocollo di negoziazione fra router potenziali gateway, e inoltre dovremmo prevedere problemi al livello *ARP* dati dal fatto che la posizione effettiva del default gateway cambia (a scapito delle tabelle ARP).
- Per risolvere il secondo di questi problemi, notiamo che esiste la possibilità di inviare un *gratuitous ARP*, cioè un pacchetto ARP che non derivi da una richiesta ARP, ma abbia il solo compito di modificare le tabelle ARP negli [[Switch]] collegati ai [[Router]];

### Protocolli di routing virtuale
Vediamo quindi i protocolli di routing virtuale più diffusi.
#### Virtual Router Redundancy Protocol (VRRP)
Rappresenta uno standard aperto (RFC 5798), versione 3, per IPv4 e IPv6. La messaggistica del protocollo è tramite datagrammi multicast IPv4 (o IPv6). Rappresenta un protocollo di *elezione*: un router viene eletto come master del router virtuale, gli altri agiscono come router di backup. Supporta anche il bilanciamento del carico.
#### Hot Standby Router Protocol (HSRP)
Protocollo proprietario Cisco aperto (RFC 2281), versione 2, per IPv4 e IPv6. Anche qui la messaggistica del protocollo è tramite datagrammi multicast IPv4 (o IPv6). Un insieme di router forma un gruppo HSRP (o gruppo standby); un router viene eletto come router attivo (l’unico responsabile dell’inoltro dei pacchetti), un altro viene eletto come router di standby.
#### Gateway Load Balancing Protocol (GLBP)
Protocollo proprietario Cisco, per IPv4 e IPv6. Aggiunge il supporto al bilanciamento del carico.