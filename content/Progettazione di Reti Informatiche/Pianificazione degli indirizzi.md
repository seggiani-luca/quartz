Abbiamo visto in [[Indirizzamento IP]] che almeno in IPv4 abbiamo a disposizione $2^{32}$ indirizzi, di cui alcuni riservati, che dobbiamo organizzare *gerarchicamente* per coprire tutti i dispositivi (a meno di non usare NAT) di una o più [[Local Area Network]] (ad esempio in un istituzione). 

Vediamo quindi come si fa ad allocare il blocco di indirizzi IPv4 (o decidere dove dividere le sottorete e collegarle attraverso [[Router]]) per accomodare il numero di host richiesti da ogni rete.

Il problema sarà sostanzialmente di ottimizzazione a due obiettivi, cioè vogliamo:
- Accomodare *tutti* i possibili host;
- Usare il blocco di indirizzi più *piccolo* possibile.

Questo problema si risolve con un automatismo che consiste sostanzialmente in:
- Trovare tutte le sottoreti e disporle dalla più grande alla più piccola;
- Allocare il blocco di dimensione più piccola ad ogni sottorete.
Per fare ciò si può usufruire di tabelle come quelle riportate in [[Indirizzamento IP#Classless InterDomain Routing]].