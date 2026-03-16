Il **moto** di un punto $P \in \mathbb{E}^3$ è una mappa (in particolare una *funzione vettoriale*, che chiameremo anche $\vec{u}(t)$):
$$
t \rightarrow P(t) \in \mathbb{E}^3, \quad t \in \mathbb{R}
$$
cioè che associa ad ogni istante temporale la posizione del punto $P$ a tale istante.  Esempi di moto sono il [[Moto rettilineo]] e il [[Moto circolare]].

### Continuità
Diciamo che tale mappa è *continua* attraverso la classica definizione:
$$
\lim_{t \rightarrow t_0} \vec{u}(t) = \vec{u}(t_0)
$$

Una volta stabilito un [[Sistema di riferimento]] $O \hat{e}_1 \hat{e}_2 \hat{e}_3$, possiamo esprimere $P(t)$ come:
$$
\mathbf{P}(t) = P_1(t) \hat{e}_1 + P_2(t) \hat{e}_2 + P_3(t) \hat{e}_3
$$
cioè sulle componenti del riferimento. In questo caso, la continuità e rispecchiata nelle singole componenti, cioè:
$$
\lim_{t \rightarrow t_0} \vec{u}(t) = \vec{u}(t_0) \, \Leftrightarrow \, \lim_{t \rightarrow t_0} u_i(t) = u_i(t_0) \quad \forall i = \{1,2,3\}
$$
Notiamo che la *traiettoria* descritta dall'estremo libero di una funzione vettoriale continua come il moto è una *curva* in $\mathbb{E^3}$ (o $\mathbb{R^3}$ fissate coordinate).

### Derivabilità
Diciamo che tale mappa è *derivabile* attraverso un'altra classica definizione, cioè quella che:
$$
\lim_{t \rightarrow t_0} \frac{\vec{u}(t) - \vec{u}(t_0)}{t -t_0}
$$
esista e sia finito. In tal caso definiamo tale limite come *derivata* in $t_0$ di $\vec{u}$:
$$
\frac{d\vec{u}}{dt}(t_0) = \lim_{t \rightarrow t_0} \frac{\vec{u}(t) - \vec{u}(t_0)}{t -t_0}
$$
Notiamo che a volte useremo anche la notazione di Newton per le derivate ($\dot{u}$, $\ddot{u}$). Inoltre, vediamo che $\frac{d\vec{u}}{dt}(t_0)$ è un vettore diviso uno scalare, per cui anch'esso è un vettore.

Come prima, stabilito un [[Sistema di riferimento]] $O \hat{e}_1 \hat{e}_2 \hat{e}_3$, possiamo esprimere la derivata sulle componenti scalari nel sistema di riferimento di $\vec{u}(t)$. In particolare:
$$
\frac{d\vec{u}}{dt}(t_0) = \lim_{t \rightarrow t_0} \frac{\vec{u}(t) - \vec{u}(t_0)}{t -t_0} = \sum_{i=1}^3 \frac{u_i(t) - u_i(t_0)}{t -t_0} \hat{e}_i = \sum_{i=1}^3 \frac{d u_i}{dt}(t_0) \hat{e}_i
$$
per cui la derivabilità in $\mathbb{R}^3$ decade nella derivabilità di ogni componente scalare, e la derivata assume il valore del vettore con componenti derivate dei componenti scalari.

Notiamo che per le funzioni vettoriali valgono le stesse regole di derivazione delle funzioni scalari. In particolare, la regola di Leibniz per il prodotto di due funzioni vale sia con il [[Prodotto scalare]] che con il [[Prodotto vettoriale]], e.g. in $\mathbb{R}^3$:
$$
\begin{cases}
\frac{d}{dt} \left( \mathbf{u}(t) \cdot \mathbf{v}(t) \right) = \dot{\mathbf{u}}(t) \cdot \mathbf{v}(t) + \mathbf{u}(t) \cdot \dot{\mathbf{v}}(t) \\
\frac{d}{dt} \left( \mathbf{u}(t) \times \mathbf{v}(t) \right) = \dot{\mathbf{u}}(t) \times \mathbf{v}(t) + \mathbf{u}(t) \times \dot{\mathbf{v}}(t)
\end{cases}
$$

### Leggi orarie
Infine, potremo descrivere le *leggi orarie* del moto $P(t)$ come segue:
- La legge oraria della **posizione** sarà:
   $$
   \vec{x}_P(t) = P(t) - O = \sum_{x=1}^3 x_i(t) \, \hat{e}_i
   $$
   o nel sistema di coordinate:
   $$
   \mathbf{x}_P(t) = \begin{pmatrix}x_1(t), \, x_2(t), \, x_3(t)\end{pmatrix}
   $$
- La legge oraria della **velocità** sarà:
   $$
   \vec{v}_P(t) = \frac{d}{dt} \left( P(t) - O \right) \Big|_\Sigma = \sum_{x=1}^3 \dot{x}_i(t) \, \hat{e}_i
   $$
   o nel sistema di coordinate:
   $$
   \mathbf{v}_P(t) = \begin{pmatrix}\dot{x}_1(t), \, \dot{x}_2(t), \, \dot{x}_3(t)\end{pmatrix}
   $$
- La legge oraria dell'**accelerazione** sarà:
   $$
   \vec{a}_P(t) = \frac{d^2}{dt^2} \left( P(t) - O \right) \Big|_\Sigma = \sum_{x=1}^3 \ddot{x}_i(t) \, \hat{e}_i
   $$
   o nel sistema di coordinate:
   $$
   \mathbf{a}_P(t) = \begin{pmatrix}\ddot{x}_1(t), \, \ddot{x}_2(t), \, \ddot{x}_3(t)\end{pmatrix}
   $$

Notiamo che la notazione con $\Sigma$ a pedice nelle derivate rispetto al tempo serve ad evidenziare il fatto che il valore delle derivate cambia sulla base del sistema di riferimento adottato. Questo ci servirà a spiegare fenomeni apparenti, che compaiono sulla base del sistema di riferimento adottato, come ad esempio l'*accelerazione centrifuga*.
