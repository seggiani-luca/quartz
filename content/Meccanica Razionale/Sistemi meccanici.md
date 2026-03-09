Definiamo, note le definizioni di [[Leggi di Newton]] (approfondite in maniera analitica nelle [[Equazioni del moto]], da cui riprendiamo la nozione di [[Equazioni del moto#Sistemi di punti]]), il concetto di **sistema meccanico**:

> [!cite] Sistema meccanico
> Consideriamo un insieme di $N$ punti materiali $P_i$, con $i = 1, \, . . . , N$,
di masse $m_i$, su cui agiscono delle forze $\mathbf{F}_i$ assegnate a priori in un sistema di riferimento $\Sigma$. Diciamo che questo è un sistema meccanico classico (discreto,
non vincolato) se il moto dei punti soddisfa le [equazioni di Newton](Equazioni%20del%20moto).

Questa definizione potrà essere approfondita se ricordiamo le definizioni di [[Sistema di riferimento inerziale]] (in particolare di [[Sistema di riferimento inerziale#Trasformazioni di Galileo]]), introducendo il concetto di *sistema meccanico* **galileiano**:

> [!cite] Sistema meccanico galileiano
> Prendiamo un **sistema meccanico**. Se nel riferimento $\Sigma$ scelto nel sistema le [equazioni di Newton](Equazioni%20del%20moto) sono invarianti per l’azione del gruppo $\mathcal{G}$ (cioè il riferimento considerato è *inerziale*), parleremo di sistema meccanico galileiano.

### Gradi di libertà
Definiamo **gradi di libertà** le dimensioni attraverso le quali sono liberi di muoversi i punti di un sistema meccanico. Il **numero** di *gradi di libertà* del sistema sarà quindi dato dalla dimensione dello spazio vettoriale $\mathbb{R}^n$ attraverso il quale i punti possono muoversi. Negli spazi (vedere [[Spazio e tempo]]) che abbiamo considerato finora questo è $\mathbb{R}^3$, e quindi si possono avere al massimo $3N$ gradi di libertà (3 per ogni punto).

Infine, notiamo che esistono alcune leggi che non sono invarianti alle trasformazioni di Galileo, che considereremo però comunque nei nostri sistemi meccanici. L'esempio più eclatante è quello della **gravità**, che privilegia la direzione $\hat{e}_3$ negativa. Abbiamo infatti che vale:
$$
m \ddot{\mathbf{x}} = - m g \hat{e}_3
$$
che assolutamente non rispetta le trasformazioni del gruppo $\mathcal{G}$.