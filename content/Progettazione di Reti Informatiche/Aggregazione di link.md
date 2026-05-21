Uno dei punti chiave delle reti che abbiamo sollevato in [[Reti informatiche]] è quello della *affidabilità e alta disponibilità*. Un modo per implementare affidabilità e alta disponibilità è quello di usare meccanismi di **aggregazione** dei link L2.

### Aggregazione di banda
L'aggregazione dei link di livello 2 permette a diverse porte switch di essere combinate in maniera da ottenere un throughput più alto fra switch.
- Si prendono quindi paia di porte *adiacenti* su ogni switch, e si collegano fra di loro, in maniera da raddoppiare la banda (almeno in via teorica) fra gli switch.
- Inoltre, questo permette di ottenere maggiore affidabilità in quanto nel caso di fallimento di un link, l'altro rimane attivo.

Di base però non si possono solo collegare due porte adiacenti fra di loro in quanto il protocollo **STP** ([[Spanning Tree Protocol]]) elimina i cicli nella topologia di rete L2, e quindi lascia solo il pregio dell'affidabilità di questa operazione (sarà disposto a usare l'altro link solo quando il primo fallisce, e non in normale operazione).

Ci viene quindi in aiuto il meccanismo della **link aggregation**, che permette di creare un singolo link *logico* a partire da più link *fisici*. 
- La tecnologia proprietaria di Cisco che implementa la link aggregation è la *EtherChannel* (ne esistono altre fornite da altri produttori). La tipologia di pacchetto usato per EtherChannel, come abbiamo visto in [[Cisco Packet Tracer]], è **PAgP** (*Port Aggregation Protocol*);
- La specifica standard IEEE è la *802.1AX-2008*. Consente di raggruppare più porte fisiche (fino a 8) per formare un singolo canale logico. Usa i pacchetti **LACP** *Link Aggregation Control Protocol* per negoziare dinamicamente l’aggregazione automatica dei link. Prevede quindi:
	- Un meccanismo di keep-alive per verificare l’appartenenza dei link al gruppo.
	- Bilanciamento del carico; 
	- Gestione del failover. 
  *LACP* prevede 2 modalità:
	- Active: richiede attivamente se il dispositivo remoto parteciperà all'aggregazione;
	- Passive: attende passivamente richieste dall'altro lato.
  Oltre alle modalità offerte da LACP, poi, due link possono essere in aggregazione statica (senza LACP).

### Configurazione della link aggregation
Su un router Cisco i tipi di interfaccia che partecipano ad un link aggregato non possono essere mescolate. I gruppi di interfacce che possono essere aggregate consistono in 1-8 porte Ethernet, che *devono* condividere la stessa configurazione. Si può quindi specificare un gruppo come:
```
S1(config)#interface range FastEthernet0/1-2 # porte FastEthernet da 1 a 2
S1(config-inf-range)# channel-group 1 mode active
```

