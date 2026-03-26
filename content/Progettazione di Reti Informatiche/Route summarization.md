Il processo di **route summarization** ("*riassunzione delle reti*") consiste nel combinare un numero di route *statiche* (vedere [[Routing statico]]) in un'unica route statica, che abbia a prefisso il prefisso comune delle route riassunte.

Questo processo, se si sfrutta uno schema di allocazione degli indirizzi gerarchico e ben sviluppato (vedere [[Pianificazione degli indirizzi]] e [[Indirizzamento IP]]), permette di includere molte meno route statiche nella [[Tabella di routing]] di un dato router. Si può anzi selezionare un piano di allocazione esplicitamente mirato a massimizzare il grado di *route summarization* raggiungibile.

Vediamo nel dettaglio:
- Se sfruttiamo un criterio di allocazione che dipende solo dalla *dimensioni* delle sottoreti (come ad esempio abbiamo presentato in [[Pianificazione degli indirizzi]]) otterremo chiaramente l'utilizzo migliore del blocco di indirizzi, ma a costo di capacità di route summarization variabile;
- Se sfruttiamo un criterio di allocazione che invece dipende anche dalla *topologia* della rete (cioè come i router sono disposti e collegati fra di loro), potremmo ottenere anche una maggiore capacità di route summarization (ma magari a costo di un utilizzo meno efficiente del blocco di indirizzi).

Notiamo che un altro *tradeoff* della route summarization è che si inoltrano pacchetti anche a sottoreti (router) che non necessariamente sono interessati, per cui si aumenta l'utilizzo complessivo della rete.