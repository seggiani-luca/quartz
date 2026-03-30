Il **Link State** è una tipologia di algoritmi di [[Routing dinamico]]. Negli algoritmi di questo tipo ogni [[Router]] pubblicizza la sua topologia locale, e sulla base delle topologie locali agli altri nodi ricevute costruisce una mappa dell'intera rete. 

I pacchetti che vengono scambiati a questo stadio sono detti **LSP** (*Link State Packet*). Per ogni link, l'LSP specifica l'indirizzo del nodo vicino e una metrica associata al link necessario al raggiungimento di questo. 

Ogni router invia il suo LSP ai vicini, e riceve gli LSP generati dai vicini. Notiamo che questo procedimento può provocare il sovraccarico della rete: per questo si usano approcci di *gossiping* o *selective flooding*. In particolare, ogni router mantiene un database degli LSP: quando un LSP viene ricevuto, se non è presente nel database, oppure la copia nel database è più vecchia, lo memorizza l’LSP nel database e lo inoltra su tutte le interfacce tranne quella da cui è stato ricevuto. Altrimenti, se la copia nel database è uguale, lo ignora, o se addirittura la sua è più recente, la invia al mittente (che provvederà ad aggiornare il suo database).

Una volta ricevuti questi LSP, li usa per costruire un database di LSP da cui ricavare la topologia di rete completa. Su questa può essere eseguito un algoritmo (ad esempio Dijkstra), che genera i risultati che vanno a popolare la tabella di routing.

#### Proprietà del Link State
Vediamo quali sono le *qualità* del link state che potrebbero invogliarci ad usarlo. Di base, il link state viene preferito perché è un algoritmo a *grande stabilità*.
- Questa è innanzitutto data dal *basso tempo di convergenza* (nell'ordine di $C \log(N)$, dove $C$ è il numero di link ed $N$ il numero di nodi), e il fatto che i router calcolano la topologia (e quindi i percorsi minimi) in maniera indipendente l'uno dall'altro (impossibilità di avere *bottleneck*);
- Si ha poi che i link state reagisce molto velocemente ai *cambi di topologia*, come abbiamo detto sfruttando il *gossiping* e il *selective flooding*;
- Ha una bassa inclinazione a creare *cicli* nel grafo di routing, per via della proprietà di coerenza degli alberi dei cammini minimi. Si possono avere loop temporanei solo nel caso di scambio di LSP, che abbiamo detto sopra è comunque molto veloce. Non si hanno quindi i problemi di *counting* ad infinito degli algoritmi [[Link State]].