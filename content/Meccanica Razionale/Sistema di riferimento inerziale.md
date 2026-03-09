Vediamo l'espressione della **prima legge di Newton** nella formulazione del moto vista in [[Equazioni del moto]].

> [!quote] [[Leggi di Newton#Prima legge di Newton]]
> Un corpo in moto con velocità $\vec{v}$ all'interno di un sistema di punti resta, se non gli viene applicata alcuna forza, nello stesso moto. In simboli:
> $$
> \vec{F}_i = 0 \implies \vec{a}_i=0
> $$

Quest'espressione è naturalmente vera definito il vettore forza $\vec{F}_i$ e assunto nullo. Abbiamo però che  l'affermazione vale solamente se si considera un [[Sistema di riferimento]] **inerziale**.

### Trasformazioni di Galileo
Consideriamo l'insieme $\mathcal{G}$ delle trasformazioni affini dello spazio-tempo di Galileo:
$$
\mathbb{G} = \mathbb{E}^3 \times \mathbb{R}
$$
visto in [[Spazio e tempo]]. Queste trasformazioni vengono dette trasformazioni di *Galileo* e rispettano le seguenti proprietà:
1. Gli *intervalli* di tempo fra due eventi vengono conservati;
2. L'*orientazione* fra eventi simultanei viene conservata;
3. La *distanza* fra eventi simultanei viene conservata.

Notiamo che, fissato un certo sistema di riferimento $\Sigma$, lo spazio di Galileo $\mathbb{G}$ è isomorfo allo spazio:
$$
\mathbb{G} \cong \mathbb{R}^3 \times \mathbb{R}
$$
per cui possiamo portare avanti i nostri calcoli vettoriali in $\mathbb{R}^3$ senza preoccuparci dello spazio affine.  Dal punto di vista matematico, quindi, i principi enunciati prima equivalgono a dire che ogni elemento $g \in \mathcal{G}$ è una trasformazione affine che può essere espressa come somma di:
1. Il *moto rettilineo uniforme* con velocità $\mathbf{u}$:
   $$
   g_1(\mathbf{x}, t) = (\mathbf{x} + t \mathbf{u}, t), \quad \mathbf{u} \in \mathbb{R}^3
   $$

2. La *traslazione dell'origine* di uno scostamento spaziale $\mathbf{y}$ e uno scostamento temporale $s$:
   $$
   g_2(\mathbf{x}, t) = (\mathbf{x} + \mathbf{y}, \, t + s). \quad \mathbf{y} \in \mathbb{R}^3, \ s \in \mathbb{R}
   $$

3. L'*isometria spaziale* attraverso una certa matrice $G$, che appunto deve essere isometrica. Le matrici isometriche in $\mathbb{R}$ sono le [[Matrici ortogonali]], e quindi ne sceglieremo una appartenente ad $SO(3)$:
   $$
   g_3(\mathbf{x}, t) = (G \mathbf{x}, t), \quad G \in SO(3)
   $$

Verifichiamo che la composizione di $g_1$, $g_2$ e $g_3$ formano l'intero spazio delle trasformazioni affini che rispettano le condizioni richieste. Innanzitutto prendiamo la generica trasformazione affine $\Phi$ dello spazio di Galileo $\mathbb{G}$:
$$
\Phi \begin{pmatrix} \mathbf{x} \\ t \end{pmatrix} = 
A \begin{pmatrix} \mathbf{x} \\ t \end{pmatrix} + \mathbf{b} , \quad A = \begin{pmatrix} G & \mathbf{u} \\ \mathbf{w}^T & a \end{pmatrix}, \quad \mathbf{b} = \begin{pmatrix} \mathbf{y} \\ s \end{pmatrix}
$$
che svolgendo i calcoli diventa:
$$
\Phi \begin{pmatrix} \mathbf{x} \\ t \end{pmatrix} =
\begin{pmatrix} G \mathbf{x} + t\mathbf{u} + \mathbf{y}  \\ \mathbf{w}^T \mathbf{x} + ta + s \end{pmatrix}
$$
1. Se vogliamo mantenere costanti gli *intervalli* di tempo, non possiamo trasformare $t$ sulla base di $\mathbf{x}$ né introdurre un fattore di scala, per cui in $\mathbf{w}^T \mathbf{x} + a t + s$ dovrà essere $\mathbf{w}^T = 0$ e $|a| = 1$ (notiamo che $t = -1$ va più che bene: questo ha implicazioni interessanti nella meccanica, cioè si può invertire il tempo);
2. Se vogliamo mantenere la *distanza* fra eventi simultanei (punto 3 delle condizioni stabilite all'inizio di questo paragrafo), dovremmo avere che $G$ è un isometria, per cui diremo che $G \in O(3)$ appartiene all'insieme delle [[Matrici ortogonali]];
3. Siccome vogliamo conservare anche l’orientazione dello spazio (punto 2), data dalla scelta del sistema di riferimento, ci restringeremo alle trasformazioni con:
   $$
   G \in SO(3)
   $$
   cioè alle [[Matrici ortogonali]] con $\det{G} = 1$ (che avevamo detto [[Matrici di rotazione]]).

Si verifica facilmente che l’insieme $\mathcal{G}$, col prodotto di composizione, è un sottogruppo del gruppo delle trasformazioni affini di $\mathbb{E}^4$, che chiameremo *gruppo di Galileo*. 

### Principio di relatività di Galileo
Possiamo estendere le trasformazioni di Galileo dello spazio $\mathcal{G}$ dallo spazio dei vettori in $\mathbb{R}^3$ a quello dei *moti* (a tal riguardo vedere [[Descrizione del moto]]) dei [[Equazioni del moto#Sistemi di punti]] $P_i$:
$$
t \rightarrow P_i(t) \in \mathbb{E}^3, \quad t \in \mathbb{R}
$$
che fissato un sistema di riferimento $\Sigma$ diventa:
$$
t = \mathbf{x}_i(t) \in \mathbb{R}^3
$$
In questo le 3 componenti fondamentali delle trasformazioni di Galileo diventano:
1. Il *moto rettilineo uniforme* con velocità $\mathbf{u}$:
   $$
   g_1(\mathbf{x}_i(t)) =\mathbf{x}_i(t) + t \mathbf{u}
   $$

2. La *traslazione dell'origine* di uno scostamento spaziale $\mathbf{y}$ e uno scostamento temporale $s$:
   $$
   g_2(\mathbf{x}_i(t)) = \mathbf{x}_i(t + s) + \mathbf{y}
   $$

3. L'*isometria spaziale* attraverso una certa matrice $G \in SO(3)$:
   $$
   g_3(\mathbf{x}_i(t)) = G \mathbf{x}_i(t)
   $$

Ricordiamo quindi le leggi di *Newton* del moto (viste in [[Equazioni del moto]]), che legavano forza $\mathbf{F}_i$, massa $m_i$ ed accelerazione $\mathbf{a}_i$ dei punti del sistema:

> [!quote] [[Leggi di Newton#Seconda legge di Newton]]
> Fra l'accelerazione $\vec{a}_i$ di un corpo di massa $m_i$ all'interno di un sistema di punti e la forza che gli viene applicata al tempo $t$, $\mathbf{F}_i$, vale la relazione:
> $$
> m_i \ddot{\mathbf{x}}_i(t) = \mathbf{F}_i (\mathbf{x}(t), \dot{\mathbf{x}}(t), t), \quad \forall i = 1, 2, ..., N
> $$

Il **principio di relatività di Galileo** affermerà quindi che:

> [!cite] Principio di relatività di Galileo
> Un sistema di riferimento **inerziale** è tale per cui le leggi di Newton sono invarianti alle trasformazioni di Galileo in $\mathcal{G}$.

Dove per *invarianza* ci riferiamo al fatto che le soluzioni della legge del moto di Newton sono invarianti alle trasformazioni in $\mathcal{G}$, cioè applicare una trasformazione $g \in \mathcal{G}$ ad una soluzione la porta in un'altra soluzione, o in simboli:
$$
t \rightarrow \mathbf{x}(t) = ( \mathbf{x}_1(t), ..., \mathbf{x}_N(t) ) \text{ soluzione} \Rightarrow t \rightarrow g \, \mathbf{x}(t) = ( g\, \mathbf{x}_1(t), ..., g \, \mathbf{x}_N(t) ) \text{ soluzione} 
$$
Notiamo che questo principio ha delle importanti importanti implicazioni per quanto riguarda l'espressione della forza stessa nella legge del moto di Newton. In particolare:
1. La forza dovrà essere *invariante nel tempo*. Questo viene dal fatto che la seconda componente delle trasformazioni di Galileo $g_2$ rappresenta uno scostamento temporale $s$, per cui dovrà valere:
   $$
   \mathbf{F}_i (\mathbf{x}(t), \dot{\mathbf{x}}(t), t) = 
   \mathbf{F}_i (\mathbf{x}(t + s), \dot{\mathbf{x}}(t + s), t)
   $$
   che è valido se $\mathbf{F}_i$ non dipende da $t$, cioè:
   $$
   \mathbf{F}_i = \mathbf{F}_i(\mathbf{x}(t), \dot{\mathbf{x}}(t))
   $$

2. La forza dovrà essere *relativistica nello spazio*. Questo significherà che gli argomenti di $\mathbf{F}_i$ per una sua qualsiasi espressione potranno essere qualsiasi combinazione di posizioni e velocità relative ad, o in simboli:
   $$
   \mathbf{F}_i = \mathbf{F}_i((\mathbf{x}_j - \mathbf{x}_k )_{j \neq k}, (\dot{\mathbf{x}}_j - \dot{\mathbf{x}}_k )_{j \neq k})
   $$
   Questo dipende dal fatto che la prima componente delle trasformazioni di Galileo $g_1$ ci permette di introdurre una velocità qualsiasi, mentre la seconda $g_2$ ci permette di introdurre uno scostamento spaziale qualsiasi. Questo significa che se si assume una certo punto $P_l$ in moto inerziale, e un istante temporale arbitrario $\tau$, si può applicare con la prima componente $g_1$:
   $$
   \mathbf{u} = -\dot{\mathbf{x}}_{k_1}(\tau) \implies \mathbf{F}_i = \mathbf{F}_i(\mathbf{x}_1(t), \, ..., \mathbf{x}_N(t), \dot{\mathbf{x}}_1(t) - \dot{\mathbf{x}}_{k_1}(t), \, ..., 0, \, ..., \dot{\mathbf{x}}_N(t) - \dot{\mathbf{x}}_{k_1}(t) )
   $$
   e quindi ottenere $\mathbf{F}_i$ in relazione a $P_{k_1}$ sulla velocità. Quindi, possiamo fare la stessa cosa con la seconda componente $g_2$:
   $$
   \begin{gather*}
   \mathbf{y} = -\mathbf{x}_{k_1}(\tau), \quad s = 0 \implies \\
   \mathbf{F}_i = \mathbf{F}_i(\mathbf{x}_1(t) - \mathbf{x}_{k_1}(t), \, ..., 0, \, ..., \mathbf{x}_N(t) - \mathbf{x}_{k_1}(t), \dot{\mathbf{x}}_1(t) - \dot{\mathbf{x}}_{k_1}(t), \, ..., 0, \, ..., \dot{\mathbf{x}}_N(t) - \dot{\mathbf{x}}_{k_1}(t) )
   \end{gather*}
   $$
   cioè siamo riusciti ad esprimere $\mathbf{F}_i$ in relazione al punto $P_k$, in breve:
   $$
   \mathbf{F}_i = \mathbf{F}_i((\mathbf{x}_j(t) - \mathbf{x}_{k_1} (t))_{i=1,..,N}, (\dot{\mathbf{x}}_j(t) - \dot{\mathbf{x}}_{k_1} (t))_{i=1,..,N})
   $$
   Possiamo ripetere questo processo indeterminate volte per ottenere la prima equazione di questo paragrafo, e quindi prendere qualsiasi combinazione di velocità e posizioni relativi. Notiamo infine che la relazione rispetto ad un singolo punto $P_{k_1}$ all'interno di una formulazione $\mathbf{F}_i$ equivale alla relazione rispetto ad arbitrari punti $P_k$ che variano, sempre all'interno della stessa formulazione $\mathbf{F}_i$. Questo funziona perché si può sempre esprimere tutto in funzione di un altro punto (diciamo $P_1$) che fa in qualche modo da *ancora* per tutte le altre velocità relative ($\dot{\mathbf{x}}_j(t) - \dot{\mathbf{x}}_k(t)$) e posizioni relative ($\mathbf{x}_j(t) - \mathbf{x}_k(t)$). Questo è cementato dal fatto che:
   $$
   \mathbf{x}_j - \mathbf{x}_k = (\mathbf{x}_j - \mathbf{x}_1) - (\mathbf{x}_k - \mathbf{x}_1), \quad \dot{\mathbf{x}}_j - \dot{\mathbf{x}}_k = (\dot{\mathbf{x}}_j - \dot{\mathbf{x}}_1) - (\dot{\mathbf{x}}_k - \dot{\mathbf{x}}_1)
   $$

3. La forza dovrà essere *isotropica*, cioè invariante a rotazioni nello spazio:
   $$
   m_i G \ddot{\mathbf{x}}_i(t) = G\mathbf{F}_i((\mathbf{x}_j - \mathbf{x}_k )_{j \neq k}, (\dot{\mathbf{x}}_j - \dot{\mathbf{x}}_k )_{j \neq k}) = \mathbf{F}_i(G(\mathbf{x}_j - \mathbf{x}_k )_{j \neq k}, G(\dot{\mathbf{x}}_j - \dot{\mathbf{x}}_k )_{j \neq k})
   $$
   Questo deriva direttamente dalla terza componente delle trasformazioni di Galileo $g_3$, in quanto una matrice di trasformazione $G \in SO(3)$ dovrà potersi applicare sia all'espressione di $\mathbf{F}_i$ che ai suoi argomenti, ovvero:
   $$
   G\mathbf{F}_i((\mathbf{x}_j - \mathbf{x}_k )_{j \neq k}, (\dot{\mathbf{x}}_j - \dot{\mathbf{x}}_k )_{j \neq k}) = \mathbf{F}_i(G(\mathbf{x}_j - \mathbf{x}_k )_{j \neq k}, G(\dot{\mathbf{x}}_j - \dot{\mathbf{x}}_k )_{j \neq k})
   $$
