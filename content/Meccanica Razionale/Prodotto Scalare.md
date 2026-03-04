Come abbiamo detto, il primo operatore che vogliamo definire su uno spazio euclideo (vedere [[Spazio e tempo]]) è il **prodotto scalare**. Questo è una forma bilineare simmetrica del tipo:
$$
\cdot : \mathbb{R}^3 \times \mathbb{R}^3 \rightarrow \mathbb{R}
$$
cioè che porta due vettori in $\mathbb{R}^3$ (o ugualmente, una volta equipaggiato con il prodotto scalare stesso, $\mathbb{E}^3$), ad uno scalare in $\mathbb{R}$.

Del prodotto scalare richiediamo 3 proprietà:
1. **Simmetria**: $$\vec{u} \cdot \vec{v} = \vec{v} \cdot \vec{u}$$E questa è triviale;
2. **Bilinearità**: a sua volta composta da:
- *Omogeneità*, sinistra e destra: $$(\alpha \cdot \vec{u}) \cdot \vec{v} = \alpha \cdot (\vec{u} \cdot \vec{v}), \quad \vec{u} \cdot (\beta \cdot \vec{v}) = \beta \cdot (\vec{u} \cdot \vec{v})$$
- *Linearità*, sinistra e destra: $$(\vec{u} + \vec{v}) \cdot \vec{w} = (\vec{u} \cdot \vec{w}) + (\vec{v} \cdot \vec{w}), \quad \vec{u} \cdot (\vec{v} \cdot \vec{w}) = (\vec{u} \cdot \vec{v}) + (\vec{u} \cdot \vec{w})$$La definizione di *linearità* (quindi linearità solo a sinistra o a destra) basterebbe, ma visto che implicare simmetria e linearità in $\mathbb{E}^3$ significa implicare bilinearità, lo riportiamo per completezza;
3. **Definizione positiva**: $$\vec{u} \cdot \vec{u} = 0 \implies \vec{u} = 0$$dove per $0$ si intende il vettore nullo. Questo ha la conseguenza naturale che:$$\vec{u} \cdot \vec{u} > 0, \quad \forall \, \vec{u} \neq 0$$
### In $\mathbf{R}^3$
La definizione del prodotto scalare a partire da vettori:
$$
\vec{x} = (x_1, x_2, x_3)
$$
su basi ortonormali in $\mathbb{R}^3$ (vedere [[Prodotto Vettoriale]]) è triviale:
$$
\vec{x} \cdot \vec{y} = \sum_i^3 x_i y_i = x_1 y_1 + x_2 y_2 + x_3 y_3
$$
da cui la classica formula mnemonica *membro a membro*.