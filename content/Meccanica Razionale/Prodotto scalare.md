Come abbiamo detto, il primo operatore che vogliamo definire su uno spazio euclideo (vedere [[Spazio e tempo]]) è il **prodotto scalare**. Questo è una forma bilineare simmetrica del tipo:
$$
\cdot : \mathbb{V}^3 \times \mathbb{V}^3 \rightarrow \mathbb{V}
$$
cioè che porta due vettori in $\mathbb{V}^3$, ad uno scalare in $\mathbb{R}$.

Del prodotto scalare richiediamo 3 proprietà:
1. **Simmetria**: 
$$
\vec{u} \cdot \vec{v} = \vec{v} \cdot \vec{u}
$$
   E questa è triviale;
2. **Bilinearità**: a sua volta composta da:
- *Omogeneità*, sinistra e destra: 
$$
(\alpha \cdot \vec{u}) \cdot \vec{v} = \alpha \cdot (\vec{u} \cdot \vec{v}), \quad \vec{u} \cdot (\beta \cdot \vec{v}) = \beta \cdot (\vec{u} \cdot \vec{v})
$$
- *Linearità*, sinistra e destra:
$$
(\vec{u} + \vec{v}) \cdot \vec{w} = (\vec{u} \cdot \vec{w}) + (\vec{v} \cdot \vec{w}), \quad \vec{u} \cdot (\vec{v} \cdot \vec{w}) = (\vec{u} \cdot \vec{v}) + (\vec{u} \cdot \vec{w})
$$
   La definizione di *linearità* (quindi linearità solo a sinistra o a destra) basterebbe, ma visto che implicare simmetria e linearità in $\mathbb{E}^3$ significa implicare bilinearità, lo riportiamo per completezza;
1. **Definizione positiva**:
$$
\vec{u} \cdot \vec{u} = 0 \implies \vec{u} = 0
$$
   dove per $0$ si intende il vettore nullo. Questo ha la conseguenza naturale che:
$$
\vec{u} \cdot \vec{u} > 0, \quad \forall \, \vec{u} \neq 0
$$
### In $\mathbf{R}^3$
La definizione del prodotto scalare a partire da vettori:
$$
\vec{x} = (x_1, x_2, x_3)
$$
su basi ortonormali in $\mathbb{R}^3$. Questo era già stato messo in chiaro riguardo al prodotto vettoriale.
> [!quote] [[Prodotto vettoriale]]
> Abbiamo che le basi ortonormali $\hat{e}_1, \hat{e}_2, \hat{e}_3$ levogire scelte nello spazio $\mathbb{V}^3$ saranno:
> $$
> \hat{e}_1 =
> \begin{pmatrix}
> 1 \\ 0 \\ 0
> \end{pmatrix}, \quad
> \hat{e}_2 =
> \begin{pmatrix}
> 0 \\ 1 \\ 0
> \end{pmatrix}, \quad
> \hat{e}_3 =
> \begin{pmatrix}
> 0 \\ 0 \\ 1
> \end{pmatrix}, \quad
> $$
> per cui si potrà individuare un qualsiasi vettore $\vec{x}$ come:
> $$
> \vec{x} = x_1 \cdot \hat{e}_1 + x_2 \cdot \hat{e}_2 + 
> x_3 \cdot \hat{e}_3 \in \mathbb{V}^3, \quad 
> \mathbf{x}=
> \begin{pmatrix}
> x_1 \\ x_2 \\ x_3
> \end{pmatrix} \in \mathbb{R}^3
> $$
> Dove la tripla $(x_1, x_2, x_3)$, dette *coordinate*, apparterrà a $\mathbb{R}^3$.

Il calcolo esplicito è quindi triviale:
$$
\vec{x} \cdot \vec{y} = \sum_i^3 x_i y_i = x_1 y_1 + x_2 y_2 + x_3 y_3
$$
da cui la classica formula mnemonica *membro a membro*.