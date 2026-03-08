Il **moto** di un punto $P \in \mathbb{E}^3$ è una mappa:
$$
t \rightarrow P(t) \in \mathbb{E}^3, \quad t \in \mathbb{R}
$$
cioè che associa ad ogni istante temporale la posizione del punto $P$ a tale istante.
Una volta stabilito un [[Sistema di riferimento]] $O \hat{e}_1 \hat{e}_2 \hat{e}_3$, potremo descrivere le *leggi orarie* del moto $P(t)$ come segue:
- La legge oraria della **posizione** sarà:$$\vec{x}_P(t) = P(t) - O = \sum_{x=1}^3 x_i(t) \, \hat{e}_i$$o nel sistema di coordinate:$$\mathbf{x}_P(t) = \begin{pmatrix}x_1(t), \, x_2(t), \, x_3(t)\end{pmatrix}$$
- La legge oraria della **velocità** sarà:$$\vec{v}_P(t) = \frac{d}{dt} \left( P(t) - O \right) \Big|_\Sigma = \sum_{x=1}^3 \dot{x}_i(t) \, \hat{e}_i$$o nel sistema di coordinate:$$\mathbf{v}_P(t) = \begin{pmatrix}\dot{x}_1(t), \, \dot{x}_2(t), \, \dot{x}_3(t)\end{pmatrix}$$La legge oraria dell'**accelerazione** sarà:$$\vec{a}_P(t) = \frac{d^2}{dt^2} \left( P(t) - O \right) \Big|_\Sigma = \sum_{x=1}^3 \ddot{x}_i(t) \, \hat{e}_i$$o nel sistema di coordinate:$$\mathbf{a}_P(t) = \begin{pmatrix}\ddot{x}_1(t), \, \ddot{x}_2(t), \, \ddot{x}_3(t)\end{pmatrix}$$
Notiamo che la notazione con $\Sigma$ a pedice nelle derivate rispetto al tempo serve ad evidenziare il fatto che il valore delle derivate cambia sulla base del sistema di riferimento adottato. Questo ci servirà a spiegare fenomeni apparenti, che compaiono sulla base del sistema di riferimento adottato, come ad esempio l'*accelerazione centrifuga*.