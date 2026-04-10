Supponiamo che un [[Corpo rigido]] $C$ compia un moto piano con velocità angolare $\vec{\omega}$ e che ad un certo istante $t$ valga la condizione di [[Moto rototraslatorio]], cioè $\vec{\omega} \neq 0$. Allora esiste uno e un solo punto $c(t)$ solidale al corpo la cui velocità all'istante $t$ è nulla:
$$
\vec{v}_c (t) = 0
$$
Tale punto $c$ viene detto **centro di istantanea rotazione** del corpo rigido e la sua posizione si può ricavare attraverso la formula:
$$
c(t) - P(T) = \frac{ \vec{\omega}(t) \times \vec{v}_P(t) }{|\vec{\omega}(t)|^2}
$$
dove $P(t)$ e $\vec{v}_P(t)$ sono rispettivamente la posizione e la velocità di un punto $P$ qualsiasi solidale al corpo. Poiché il moto è piano, vale che:
$$
\vec{\omega} = \omega \vec{e}_3
$$
dalle assunzioni fatte sul sistema di riferimento $\Sigma$ in [[Moto piano]]. Cerchiamo quindi un punto $c$ solidale al corpo che abbia velocità nulla in $\Sigma$. Imponiamo quindi per la legge delle velocità del corpo rigido:
$$
0 = \vec{v}_c = \vec{v}_P + \vec{\omega} \times (c - P) = \vec{\omega} \times \vec{v}_P + \vec{\omega} \times \left( \vec{\omega} \times (c - P) \right) = \vec{\omega} \times \vec{v}_P - |\omega|^2 (c -P)
$$
da cui si ricava direttamente la tesi, passando dai punti ai moti in $t$. Osserviamo che questa formula permette di calcolare il centro di istantanea rotazione conoscendo la velocità di un punto $P$ solidale al corpo rigido e la velocità angolare del corpo. A questo punto, il centro di istantanea rotazione $c$ non è necessariamente un punto appartenente al corpo rigido (ma è sicuramente solidale).

### Geometria della legge delle velocità
Definito il centro di istantanea rotazione $c(t)$ possiamo dare un'altra interpretazione della *legge di velocità* dei corpi rigidi:

> [!cite] Legge di velocità di un corpo rigido
> Sia $\Sigma$ un sistema di riferimento fisso e $C$ un corpo rigido. Per ogni punto $P$ del corpo $C$ vale:
> $$
> \vec{v}_P(t) = \vec{\omega}(t) \times (P(t) - c(t))
> $$
> dove $\vec{\omega}$ è la velocità angolare di $C$ rispetto a $\Sigma$, e $c(t)$ la posizione del centro di istantanea rotazione.

Notiamo che questo è valido direttamente dalla legge di velocità, noto il fatto che $c(t)$ è solidale a $C$, e che la sua velocità $\vec{v}_C$ è nulla, per cui:
$$
\vec{v}_P(t) = \vec{v}_C + \vec{\omega}(t) \times (P(t) - c(t)) = \vec{\omega}(t) \times (P(t) - c(t))
$$
Osserviamo quindi che $\vec{v}_P$ sarà sempre perpendicolare a $P(t) - c(t)$, cioè la velocità sara *tangenziale* alla circonferenza di raggio $P(t) - c(t)$ (in questo il centro di istantanea rotazione è centro della rotazione, vedere [[Moto circolare]]). Inoltre, il modulo della velocità è proporzionale alla distanza da $c(t)$:
$$
|\vec{v}_P(t)| = |\vec{\omega}(t)| |P(t) - c(t)|
$$
Questo è sempre in accordo con [[Moto circolare]], dove avevamo detto che la velocità di un punto $P$ generico in moto circolare non uniforme era:
$$
\vec{v}_P(t) = 
\omega(t) R \left( 
-\sin(\theta(t)), 
\cos(\theta(t)), 
0
\right) \implies
|\vec{v}_P(t)| = |\vec{\omega}(t)| R
$$
con $R = P(t) - c(t)$, che è quanto si assumeva.

### Polare fissa
L'insieme dei centri di istantanea rotazione al variare di $t$:
$$
\Gamma = \{ c(t) : t \in \mathbb{R} \}
$$
forma una curva, detta curva **polare fissa** del corpo rigido.