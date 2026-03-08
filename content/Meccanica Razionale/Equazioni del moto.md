Abbiamo visto come effettuare la [[Descrizione del moto]] su un dato sistema di riferimento. In particolare, avevamo detto riguardo al *moto*:

> [!quote] [[Descrizione del moto]]
> Il **moto** di un punto $P \in \mathbb{E}^3$ è una mappa:
> $$
> t \rightarrow P(t) \in \mathbb{E}^3, \quad t \in \mathbb{R}
> $$
> cioè che associa ad ogni istante temporale la posizione del punto $P$ a tale istante.

Vediamo di legare tale moto al concetto di *forza* applicata ad un punto, per arrivare a descrivere un *sistema di punti* attraverso sistemi di equazioni differenziali del secondo grado.

### Sistemi di punti
Consideriamo un **sistema di punti**, cioè semplicemente un'insieme di $N$ punti $P_i \in \mathbb{E}^3$. Dati questi, definiamo anche i vettori delle *posizioni* e delle *velocità*:
$$
\vec{\mathbf{x}} = \left( \vec{x}_1, \, \vec{x}_2, \, ... , \vec{x}_N \right), \quad
\vec{\mathbf{v}} = \left( \vec{v}_1, \, \vec{v}_2, \, ... , \vec{v}_N \right)
$$
che in coordinate su un sistema di riferimento $\Sigma$ diventa:
$$
\mathbf{x} = \left( \mathbf{x}_1, \, \mathbf{x}_2, \, ... , \mathbf{x}_N \right), \quad
\mathbf{v} = \left( \dot{\mathbf{x}}_1, \, \dot{\mathbf{x}}_2, \, ... , \dot{\mathbf{x}}_N \right)
$$
### Forza
Leghiamo quindi il moto del sistema di punti al concetto di **forza**. Di base, la forza $\vec{F}_i$ sarà un vettore in $\mathbb{V}^3$ associato al punto $P_i$ del sistema, che prenderà in argomento la posizione e la velocità di ogni punto del sistema, nonché il tempo. Questo significa che si avrà una funzione:
$$
\vec{F}_i : \left( \mathbb{V}^3 \right)^N \times \left( \mathbb{V}^3 \right)^N
 \times \mathbb{R} \rightarrow \mathbb{V}^3
$$
che in coordinate su un sistema di riferimento $\Sigma$ diventa:
$$
\mathbf{F}_i : \left( \mathbb{R}^3 \right)^N \times \left( \mathbb{R}^3 \right)^N
 \times \mathbb{R} \rightarrow \mathbb{V}^3
$$
Nello specifico, sarà rispetto a $\mathbb{V}^3$ e quindi rispetto a $\mathbb{R}^3$ riferendoci al sistema di coordinate:
$$
\vec{F}_i = \vec{F}_i(\vec{x}_1, \, \vec{x}_2, \, ... , \vec{x}_N, \, \vec{v}_1, \, \vec{v}_2, \, ... , \vec{v}_N t ), \quad \mathbf{F}_i = \mathbf{F}_i(\mathbf{x}_1, \, \mathbf{x}_2, \, ... , \mathbf{x}_N, \dot{\mathbf{x}}_1, \, \dot{\mathbf{x}}_2, \, ... , \dot{\mathbf{x}}_N, \, t )
$$
e presi i vettori delle posizioni $\vec{\mathbf{x}}$ e delle velocità $\vec{\mathbf{v}}$ si avrà. in maniera più sintetica:
$$
\vec{F}_i = \vec{F}_i(\vec{\mathbf{x}}, \vec{\mathbf{v}}, t), \quad \mathbf{F}_i = \mathbf{F}_i(\mathbf{x}, \mathbf{v}, t)
$$
Avremo quindi che il valore della forza applicata al punto $P_i$ al tempo $t$ è completamente determinato dalle posizioni e le velocità di tutti gli altri punti $P_j$ più il tempo $t$, ovvero l'intero stato del sistema fino al secondo grado di derivazione sul tempo non compreso.

Veniamo quindi ad enunciare la **seconda legge di Newton**:

> [!quote] [[Leggi di Newton#Seconda legge di Newton]]
> Fra l'accelerazione $\vec{a}_i$ di un corpo di massa $m_i$ all'interno di un sistema di punti e la forza che gli viene applicata al tempo $t$, $\vec{F}_i$, vale la relazione:
> $$
> m_i \vec{a_i} = \vec{F}_i (\vec{\mathbf{x}}, \vec{\mathbf{v}}, t), \quad \forall i = 1, 2, ..., N
> $$

dove gli $\vec{\mathbf{x}}$, $\vec{\mathbf{v}}$ sono sempre i vettori delle velocità e delle posizioni del sistema dei punti $P_i$ (in sostanza ciò che ci interessa avere è una definizione della forza $\vec{F}_i$). Questo, in coordinate $\Sigma$, diventa:
$$
m_i \ddot{\mathbf{x}}_i = m_i \dot{\mathbf{v}}_i = \mathbf{F}_i (\mathbf{x}, \dot{\mathbf{x}}, t), \quad \forall i = 1, 2, ..., N
$$
Questo significa che l'intero stato dinamico di un sistema di $N$ punti $P_i \in \mathbb{E}^3$ in moto può essere espresso come il sistema di *Cauchy*:
$$
\begin{cases}
\dot{\mathbf{x}}_i = \mathbf{v}_i \\ 
\dot{\mathbf{v}}_i = \frac{\mathbf{F}_i (\mathbf{x}, \dot{\mathbf{x}}, t)}{m_i}
\end{cases}
$$
o più in generale, se denominiamo $\mathbf{F}$ il vettore delle *forze* per ogni punto $P_i$ e $m$ il vettore delle *masse*:
$$
\begin{cases}
\dot{\mathbf{x}} = \mathbf{v} \\ 
\dot{\mathbf{v}} = \frac{\mathbf{F} (\mathbf{x}, \dot{\mathbf{x}}, t)}{m}
\end{cases}
$$
sempre con riferimento al sistema di coordinate in $\Sigma$ (abbiamo usato tutti valori in $\mathbb{R}$ o $\mathbb{R}^3$).

Giusto per curiosità, vediamo che un affermazione di questo tipo della seconda legge di Newton racchiude anche la [[Leggi di Newton#Prima legge di Newton]]. In particolare, non vale altro che:
$$
\vec{F}_i = 0 \implies \vec{a}_i=0
$$
cioè un corpo non sottoposto a forze non è sottoposto neanche ad accelerazioni, e prosegue quindi il suo moto. Vedremo, in particolare, che questo è vero in un [[Sistema di riferimento inerziale]].