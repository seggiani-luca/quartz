Dimostriamo qui un risultato riguardo a sistemi di riferimento rotanti che ci tornerà utile per descrivere un [[Sistema di riferimento in moto circolare]]. Il risultato, che riportiamo subito, è il seguente:

> [!cite] Formule di Poisson
> Se le coordinate di una terna di vettori $\vec{e}'_h$ formanti un [[Sistema di riferimento]] $\Sigma'$ sono funzioni derivabili del tempo $t$, e si ha un secondo riferimento $\Sigma$, allora esiste un’unica mappa $t \rightarrow \vec{\omega}(t)$, tale che:
> $$
> \frac{d}{dt} \vec{e}'_h \Bigg|_\Sigma = \vec{\omega} \times \vec{e}'_h, \quad 1 \leq h \leq 3
> $$

Il risultato, abbastanza verboso, si riferisce al fatto che un sistema di riferimento rotante visto da un secondo riferimento (preso fisso), ha vettori in base che derivati danno:
$$
\frac{d}{dt} \mathbf{e}'_h = \boldsymbol{\omega} \times \mathbf{e}'_h, \quad 1 \leq h \leq 3
$$
#### Sistemi di riferimento
Iniziamo col definire un [[Sistema di riferimento]] principale $\Sigma$, e un altro $\Sigma'$ che farà da sistema di riferimento rotante:
$$
\Sigma = O\hat{e}_1\hat{e}_2\hat{e}_3, \quad \Sigma' = O'\hat{e}'_1\hat{e}'_2\hat{e}'_3
$$
Useremo la terna formata da ogni [[Versore]] $\hat{e}_h$ per definire una base $B$, e analogamente useremo ogni vettore $\hat{e}_h'$ per definire una base $B'$. Notiamo che tutti questi versori stanno in $\mathbb{V}^3$. 
Ci riporteremo ai vettori in $\mathbb{R}^3$ prendendo la base $B$ come quella canonica, cioè i vettori $\mathbf{e}_h \in \mathbb{R}^3$ nella base $B$ come i classici:
$$
\mathbf{e}_1 = (1, 0,0), \ \mathbf{e}_2 = (0, 1, 0), \ \mathbf{e}_3 = (0, 0, 1) \in B
$$
I vettori $\mathbf{e}'_h \in \mathbb{R}^3$ nella base $B'$ prima saranno quindi l'espressione dei vettori $\vec{e}'_h$ attraverso gli $\mathbf{e}_h$ della base $B$.

#### Matrice di cambio di base
Prendiamo quindi la matrice del cambio di base da $B'$ a $B$:
$$
R^{B'}_B, \quad R_{ji} = \hat{e}'_i \cdot \hat{e}'_j
$$
da quanto detto riguardo alle proiezioni in [[Sistema di riferimento#Da punti a coordinate]]. 

Vediamo velocemente che $R$ appartiene alla classe delle [[Matrici ortogonali]], in quanto per come abbiamo preso i suoi componenti:
$$
\vec{e}_i \cdot \vec{e}_j = \vec{e}'_i \cdot \vec{e}'_j = \delta_{ij}, \quad 1 \leq i, j \leq 3
$$
dove $\delta_{i,j}$ è la delta di *Kronecker* che avevamo visto in [[Sistema di riferimento]], per cui:
$$
R^T R = R R^T = I
$$

Notiamo che presa questa matrice, vale riguardo ai vettori in $\mathbb{R}^3$:
$$
\mathbf{e}'_h = R \mathbf{e}_h
$$
affermazione che potrebbe sembrare poco intuitiva ($R$ porta $B'$ in $B$, non viceversa). Questo però viene dal fatto che gli $\mathbf{e}_h$ sono i $\hat{e}_h$ presi come vettori della base canonica, e gli $\mathbf{e}'_h$ sono i vettori in base $B'$ presi come espressione in tale base. Questo significa che prendere la trasformata di $\mathbf{e}_h$ significa portare un vettore dalla base $B'$ all'interno della base $B$: scegliere come vettore da trasportare un vettore in base canonica significa ricavare una delle espressioni in base canonica degli $\vec{e}'_h$ (cioè gli $\mathbf{e}'_h$).  Se questo fosse poco chiaro, basta vedere che per come è stata costruita $R$ l'espressione è verificata algebricamente.

#### Derivazione
Riprendiamo quindi l'espressione:
$$
\mathbf{e}'_h = R \mathbf{e}_h
$$
da questa vorremo ricavare un espressione per la derivata dei $\mathbf{e}'_h$, che sono i vettori in base del sistema di riferimento rotanti, nel sistema di riferimento fisso degli $\mathbf{e}_h$. Abbiamo già fissato il riferimento negli $\mathbf{e}_h$, prendendo $B$ come la base canonica, per cui deriviamo direttamente:
$$
\frac{d}{dt} \mathbf{e}'_h = \dot{R} \mathbf{e}_h = \dot{R} R^T R \mathbf{e_h} = \dot{R} R^T \mathbf{e}'_h
$$
grazie alle proprietà di $R$, che è ortogonale.

Abbiamo quindi ottenuto che le derivate degli $\mathbf{e}'_h$ dipendono da questi attraverso una matrice, che chiamiamo $\Omega$:
$$
\Omega = \dot{R} R^T , \quad \dot{R} = \Omega R
$$
La proprietà fondamentale di questa matrice $\Omega$ è che è *antisimmetrica*. Questo si dimostra dal fatto che:
$$
\frac{d}{dt} R R^T = \dot{R} R^T + R \dot{R^T} = 0 \implies \dot{R} R^T = - ( \dot{R} R^T)
$$
Una proprietà fondamentale delle matrici *antisimmetriche* è che esprimono il [[Prodotto vettoriale]] fissato il vettore sinistro, cioè esiste ed è unico un $\boldsymbol{\omega}$ tale che:
$$
\Omega \, \mathbf{r} = \boldsymbol{\omega} \times \mathbf{r}
$$
La dimostrazione si ha prendendo $\Omega$ come:
$$
\Omega = \begin{pmatrix}
0 & -\omega_3 & \omega_2 \\
\omega_3 & 0 & -\omega_1 \\
-\omega_2 & \omega_1 & 0
\end{pmatrix}
$$
Da questo segue la tesi:
$$
\frac{d}{dt} \mathbf{e}'_h = \Omega \, \mathbf{e}'_h = \boldsymbol{\omega} \times \mathbf{e}'_h
$$

Abbiamo quindi dimostrato l'affermazione all'inizio di questa nota. $\boldsymbol{\omega}$ è il *vettore velocità angolare* che useremo in [[Sistema di riferimento in moto circolare]], e qualsiasi vettore espresso in un sistema di riferimento rotante (dato dai $\mathbf{e}'_h$ in base), derivato, presenterà la componente data da $\boldsymbol{\omega} \times \mathbf{r}$ (per il fatto che si potrà esprimere come combinazione lineare degli $\mathbf{e}'_h$).