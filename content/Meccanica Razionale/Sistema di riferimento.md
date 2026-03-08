Per individuare la posizione di un punto $P$ all'interno di uno spazio euclideo $\mathbb{E}^3$ abbiamo bisogno di un **sistema di riferimento** che ci riporti a coordinate in $\mathbb{R}^3$. Infatti avevamo detto:

> [!quote] [[Spazio e tempo]]
> Il fatto che lo spazio euclideo è sostanzialmente uno spazio affine significa che i suoi elementi sono **punti**, e non vale la dualità *punto*/*vettore*. Per riportarci ad uno spazio vettoriale con origine nota e su cui i punti possono essere trattati come vettori avremo bisogno di un [[Sistema di riferimento]].

Formalmente, un sistema di riferimento è una mappa che associa un istante temporale ad un origine $O$ e 3 vettori che indicano le direzioni degli assi, $\hat{e}_1$, $\hat{e}_2$, $\hat{e}_3$:
$$
t \rightarrow \Sigma(t) = \left( O(t), \hat{e}_1(t), \hat{e}_2(t), \hat{e}_3(t) \right) \in \mathbb{E}^3 \times \left( \mathbb{V^3} \right)^3
$$
dove notiamo che la mappa è continua e dipende da $t$ (la posizione dell'origine $O$ e i 3 assi  $\hat{e}_1$, $\hat{e}_2$, $\hat{e}_3$ possono variare nel tempo).
Per i 3 assi vogliamo assicurare l'indipendenza lineare (in modo che questi possano fare da basi di uno spazio $\mathbb{V}^3$ fissata l'origine $O$ in $\mathbb{E}^3$, per cui diremo che obbediscono:
$$
\hat{e}_1(t) \cdot \hat{e}_2(t) = \delta_{ij}, \quad \forall i,j = 1,2,3, \ \forall t \in \mathbb{R}
$$
dove $\delta_{ij}$ rappresenta la delta di *Kronecker*, definita come:
$$
\delta_{ij} = 
\begin{cases}
	1, \quad i = j \\
	0, \quad i \neq j
\end{cases}
$$
Concludiamo dicendo che per brevità, ci riferiamo ai sistemi di riferimento come $O \hat{e}_1 \hat{e}_2 \hat{e}_3$, o solo $\Sigma$.

### Rappresentazione in coordinate
Una volta definito un sistema di riferimento $O \hat{e}_1 \hat{e}_2 \hat{e}_3$, vorremmo esplicitare come si passa dal punto qualsiasi:
$$
P \in \mathbb{E}^3
$$
nello spazio di Eulero, alla sua rappresentazione come vettore nello spazio $\mathbb{V}^3$ vettoriale associato al sistema di riferimento:
$$
\vec{x}_P = P - O = \sum_{i = 1}^3 x_i \hat{e}_i \in \mathbb{V}^3, \quad P, O \in \mathbb{E}^3$$
o analogamente alla rappresentazione in coordinate (già introdotte in [[Prodotto vettoriale]]) nello spazio $\mathbb{R}^3$ rispetto al sistema di riferimento:
$$
\mathbf{x}_P = 
\begin{pmatrix}
x_1 \\ x_2 \\ x_3
\end{pmatrix}
\in \mathbb{R}^3
$$
dove gli $x_1$, $x_2$, $x_3$ sono quelli della formula precedente.

### Da punti a coordinate
Vediamo quindi di riassumere un ultima volta il processo di conversione da un punto $P$ nello spazio euclideo $\mathbb{E}^3$, rappresentato in maniera affine (quindi senza sistema di riferimento), alla sua rappresentazione $\mathbf{x}_P$ come coordinate in $\mathbb{R}^3$, rispetto ad un dato sistema di riferimento $O \hat{e}_1 \hat{e}_2 \hat{e}_3$. 

![[ref_system.png|400]]

1. Abbiamo che innanzitutto dobbiamo  prendere l'elemento dello spazio di traslazione che rappresenta lo scostamento di $P$ dall'origine $O$, cioè:    $$
   \vec{x}_P = P - O \in \mathbb{V}^3
   $$
2. Questo dovrà quindi essere riportato alla tripla $(x_1, x_2, x_3)^T \in \mathbb{R}^3$ attraverso la proiezione di sui 3 assi $\hat{e}_1$, $\hat{e}_2$, $\hat{e}_3$ del punto $\vec{x}_P$, cioè:
   $$
   \vec{x}_P = \sum_{i = 1}^3 x_i \hat{e}_i, \quad x_i = \, < \vec{x}_P, \hat{e}_i >
   $$
   e quindi:
   $$
   \mathbf{x}_P = \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} = \begin{pmatrix} < \vec{x}_P, \hat{e}_1 > \\ < \vec{x}_P, \hat{e}_2 > \\ < \vec{x}_P, \hat{e}_3 > \end{pmatrix}
   $$
Con questo processo, quindi, ci saremo ricondotti al vettore $\mathbf{x}_P \in \mathbb{R}^3$. Una visualizzazione si può trovare su [Desmos](https://www.desmos.com/3d/dvhybnaggx). Notiamo che questa visualizzazione *"bara"* in quanto in un sistema calcolatore è sostanzialmente impossibile rappresentare uno spazio veramente affine, e sicuramente lo è in Desmos. Per questo motivo sia $O$ che $P$ sono in verità espressi sempre in *coordinate* come vettori di $\mathbb{R}^3$ (e quindi rispetto all'origine nulla). Quindi, scelti i 3 assi $\hat{e}_1$, $\hat{e}_2$ e $\hat{e}_3$ si va a calcolare $x_1$, $x_2$ e $x_3$ usando le solite formule di proiezione su vettore:
$$
p_{roj}\left(\vec{u},\vec{v}\right)=\frac{\vec{u}\cdot \vec{v}}{\left|\vec{v}\right|}
$$
Questo è comunque quello che fanno la maggior parte dei motori fisici in commercio.
