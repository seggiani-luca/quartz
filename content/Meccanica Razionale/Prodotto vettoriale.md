Il secondo operatore che vogliamo definire su uno spazio euclideo (vedere [[Spazio e tempo]]) è il **prodotto vettoriale**. Questo è una forma bilineare antisimmetrica del tipo:
$$
\times : \mathbb{V}^3 \times \mathbb{V}^3 \rightarrow \mathbb{V}^3
$$
cioè che porta due vettori in $\mathbb{V}^3$, ad un altro vettore in $\mathbb{V}$.

Del prodotto vettoriale richiediamo 3 proprietà:
1. **Antisimmetria**: 
   $$
   \vec{u} \times \vec{v} = -\vec{v} \times \vec{u}
   $$
   E questa è triviale;
2. **Regola del modulo**:
   $$
   \vec{u} \cdot \vec{v} = 0 \implies |\vec{v} \times \vec{u}| = |\vec{v}||\vec{u}|
   $$
   dove $\cdot$ rappresenta il comune [[Prodotto scalare]] in $\mathbb{V}^3$. Ricordiamo che prodotto scalare $\vec{u} \cdot \vec{v}$ nullo significa che $\vec{u}$ e $\vec{v}$ sono vettori *paralleli*. In questo il prodotto scalare restituisce un vettore che ha come modulo la superficie del parallelepipedo individuato dai due vettori;
3. **Conservazione del volume**: introduciamo la formula del **volume segnato** di un parallelepipedo individuato dai tre vettori $\vec{u}$, $\vec{v}$ e $\vec{w}$: 
   $$
   V_S = (\vec{u} \times \vec{v}) \cdot \vec{w}, \quad V_S \in \mathbb{R}
   $$
   Questa formula può essere approfondita in maniera interattiva su [Desmos](https://www.desmos.com/3d/m2l4v7geih). Perché la nostra definizione di prodotto vettoriale sia coerente, avremo bisogno che il volume $V_S$ del parallelepipedo, considerato qualsiasi ordinamento dei vettori che lo generano, dovrà essere conservato, cioè:
   $$
   (\vec{u} \times \vec{v}) \cdot \vec{w} = (\vec{u} \times \vec{w}) \cdot \vec{v} = (\vec{v} \times \vec{w}) \cdot \vec{u}
   $$
### Terne levogire e destrogire
Applicando la definizione di prodotto vettoriale, si può ricavare che nello spazio $\mathbb{V}^3$ ne esistono esattamente 2, che chiamiamo $\times'$ e $\times''$, il cui risultato differisce solo in termini di segno. Per la precisione, prese le 3 basi ortonormali $\hat{e}_1, \hat{e}_2, \hat{e}_3$, si ha:
$$
\begin{cases}
\hat{e}_1 \times' \hat{e}_2 = \hat{e}_3, \quad \hat{e}_2 \times' \hat{e}_3 = \hat{e}_1, \quad \hat{e}_3 \times' \hat{e}_1 = \hat{e}_2 \\
\hat{e}_1 \times'' \hat{e}_2 = -\hat{e}_3, \quad \hat{e}_2 \times'' \hat{e}_3 = -\hat{e}_1, \quad \hat{e}_3 \times'' \hat{e}_1 = -\hat{e}_2
\end{cases}
$$
Quindi generalmente $\vec{u} \times' \vec{v} = - \vec{u} \times'' \vec{v}$, e i vettori generati appartengono allo stesso span. Decidiamo di adottare terne di vettori base $\hat{e}_1, \hat{e}_2, \hat{e}_3$ *levogire*, e su queste terne di usare il prodotto vettoriale $\times'$.

### In $\mathbf{R}^3$
Abbiamo che le basi ortonormali $\hat{e}_1, \hat{e}_2, \hat{e}_3$ levogire scelte nello spazio $\mathbb{V}^3$ saranno:
$$
\hat{e}_1 =
\begin{pmatrix}
1 \\ 0 \\ 0
\end{pmatrix}, \quad
\hat{e}_2 =
\begin{pmatrix}
0 \\ 1 \\ 0
\end{pmatrix}, \quad
\hat{e}_3 =
\begin{pmatrix}
0 \\ 0 \\ 1
\end{pmatrix}, \quad
$$
per cui si potrà individuare un qualsiasi vettore $\vec{x}$ come:
$$
\vec{x} = x_1 \cdot \hat{e}_1 + x_2 \cdot \hat{e}_2 + 
x_3 \cdot \hat{e}_3 \in \mathbb{V}^3, \quad 
\mathbf{x}=
\begin{pmatrix}
x_1 \\ x_2 \\ x_3
\end{pmatrix} \in \mathbb{R}^3
$$
Dove la tripla $(x_1, x_2, x_3)$, dette *coordinate*, apparterrà a $\mathbb{R}^3$. In questo caso lo svolgimento del prodotto vettoriale $\vec{x} \times \vec{y}$ sarà dato dal determinante della matrice:
$$
\vec{x} \times \vec{y} =
\det
\begin{pmatrix}
\hat{e}_1 & \hat{e}_2 & \hat{e}_3 \\
x_1 & x_2 & x_3 \\
y_1 & y_2 & y_3
\end{pmatrix}
= (x_2 y_3 - x_3 y_2) \hat{e}_1 + (x_3 y_1 - x_1 y_3) \hat{e}_2 + (x_1 y_2 - x_2 y_1) \hat{e}_3
$$
da cui la classica formula mnemonica.
