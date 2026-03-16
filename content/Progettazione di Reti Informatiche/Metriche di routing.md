Per i diversi percorsi memorizzati nella [[Tabella di routing]] di un [[Router]] è opportuno definire una qualche sorta di **metrica** che valuta la convenienza o meno di un dato percorso (e quindi dell'hop che porta tale percorso). Le metriche più comuni sono:
- Il **numero di hop**, la metrica più diffusa, che mira solamente a minimizzare i router che il pacchetto attraversa. Questa metrica viene ad esempio usata dal protocollo **RIP** (*Routing Information Protocol*);
- La **larghezza di banda** sul percorso, data dalla larghezza di banda dei singoli link;
- Il **carico** sul link che porta a un dato router: questo ci porterebbe a preferire alternativamente percorsi meno più o meno congestionati a seconda del carico corrente;
- Il **ritardo** temporale per il raggiungimento di un router, o per il tempo che questo richiede ad elaborare un pacchetto (in questo ricordiamo che ci sono diversi modelli logici per l'implementazione dei router, che si sono evoluti per minimizzare questi ritardi);
- L'**affidabilità** di un dato percorso, cioè la sicurezza che abbiamo che il nostro pacchetto, dopo l'hop, arrivi effettivamente al destinatario (ricordiamo, come abbiamo detto in [[Introduzione a Progettazione di Reti Informatiche#Internet, contratti]], che Internet è *best-effort*).

### Distanza amministrativa
La **distanza amministrativa** (AD, *Administrative Distance*) è una metrica di routing assegnata dal [[Router]] ad un percorso sulla base del tipo di protocollo che ha appreso tale percorso. Più è piccola, più si preferisce quel percorso. Vediamo quali sono i valori dell'AD di default dei router Cisco:
- Connected: 0;
- Static: 1;
- EIGRP (interno): 90;
- IGRP: 100;
- OSPF: 110;
- IS-IS: 115;
- RIP: 120;
- EIGRP esterno: 170;
- BGP (esterno): 20;
- BGP (interno): 200;