Avevamo visto un sottoinsieme particolare delle [[Matrici ortogonali]], che rappresentava le **rotazioni** attorno ad un *asse di rotazione*:

> [!quote] [[Matrici ortogonali#Matrici di rotazione]]
> Notiamo che lo spazio delle matrici di rotazione $SO(3)$ non è altro che un sottoinsieme dello spazio delle matrici ortogonali $O(3)$. In particolare, si ottiene imponendo alle matrici $A$ in $O(3)$ la seguente condizione:
> $$
> SO(3) = \{ A \in O(3) \ \text{t.c.} \ \det(A) = 1\}
> $$
> per cui consideriamo le sole matrici ortogonali che preservano il volume positivo. Facendo ciò, escludiamo le matrici che implicavano un operazione di *riflessione* e quindi otteniamo le matrici di rotazione attorno ad un asse detto *asse di rotazione*.

Approfondiamo come mai questo è il caso, e cerchiamo di trovare una forma generalizzare che esprime in maniera semplice la rotazione di un certo angolo attorno ad un asse qualsiasi.

### Dimostrazione
Vediamo nel dettaglio come mai lo spazio $SO(3)$ esprime le rotazioni. Per ogni matrice in $SO(3)$, dato che ogni elemento dello spazio delle matrici ortogonali $O(3)$ è unimodulare, varrà che gli autovalori hanno modulo unitario, cioè:
$$
A \in O(3), \quad |A| = 1 \implies |\lambda| = 1
$$
Inoltre, nello specifico per matrici $R \in SO(3)$ vale:
$$
\det(R - I) = \det R^T (R - I) = \det (R^T(R - I)) = \det(I - R^T) = \det (I - R)
$$
E se $R$ è di ordine 3, vale:
$$
\det (-R) = (-1^{3}) \det(R) = -\det(R)
$$
per cui si può dire:
$$
\det(R - I) = - \det(I - R), \quad \det(R - I) = \det(I - R) \implies \det(R - I) = 0
$$
e quindi $\lambda_1 = 1$ è un autovalore di $R$. Dalle proprietà degli autovalori si avrà quindi:
$$
\lambda_1 \cdot \lambda_2 \cdot \lambda_3 = 1, \quad \lambda_1 = 1 \implies \lambda_2 \lambda_3 = 1, \quad |\lambda_2| = |\lambda_3| = 1
$$
per cui abbiamo 3 casi possibili:
1. $\lambda_2 = \lambda_3 = 1$. In questo caso si ha che la matrice $R$ equivale all'identità in quanto non trasforma lungo nessuno dei suoi autovettori, per cui siamo nel caso di rotazione nulla. Notiamo che se per assurdo fosse $R \neq I$, significherebbe che l'autospazio $V_1$ associato a $\lambda_1$ avrebbe dimensione $\neq 1$, anzi $=2$. Infatti, significherebbe che potremmo completare la base dei 2 autovettori $\{\mathbf{x}_1, \mathbf{x}_2 \}$ nell'autospazio $V_1$ con un terzo autovettore $\mathbf{x}_3$, e per le proprietà delle matrici diagonalizzabili $R$ sarebbe diagonale in tale base. Nello specifico, si avrebbero i coefficienti della matrice diagonale:
   
   $$
   d_{ij} =\mathbf{x}_i \cdot R \mathbf{x}_j = \mathbf{x}_i \cdot \mathbf{x}_j = \begin{cases}1, \quad i = j \\ 0, \quad i \neq j\end{cases}
   $$

   che per $i \neq j = 0$, $1$ altrimenti (visto che $R$ è unitaria per i suoi autovettori). Segue che $R = I$ sulla base $\{\mathbf{x}_1, \mathbf{x}_2, \mathbf{x}_3 \}$ (o su qualsiasi altra)
   
   $$
   R_1 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{pmatrix}
   $$

   e questo va contro l'assunzione fatta ($R \neq I$). Inoltre, cosa anche più importante, questo significa che per qualsiasi $R \in SO(3)$ esiste un luogo dei punti che restano invariati, (l'autospazio di $\lambda_1$) di dimensione 1, quindi una retta. Questa retta non sarà altro che l'*asse di rotazione* della trasformazione $R$;

2. $\lambda_2 = \lambda_3 = -1$. In questo caso si ha che la matrice $R$ equivale alla rotazione di $\pi$ attorno all'asse di rotazione, in quanto si ha capovolgimento sugli autovettori perpendicolari all'asse. In particolare, si ha che l'autospazio $V_{-1}$ associato a $\lambda_2$ ha dimensione $=2$. Questo si ricava dal fatto che l'autovettore $\mathbf{x}_1$ associato a $\lambda_1$ è perpendicolare all'autovettore $\mathbf{x}_2$ associato a $\lambda_2$, in quanto:$$\mathbf{x}_1 \cdot \mathbf{x}_2 = R^T R \mathbf{x_1} \cdot \mathbf{x}_2 = R \mathbf{x}_1 \cdot R \mathbf{x}_2 = \mathbf{x}_1 \cdot - \mathbf{x}_2 = 0$$Come prima, possiamo completare la base dei 2 autovettori $\{\mathbf{x}_1, \mathbf{x}_2 \}$ nell'autospazio $V_{-1}$ con un terzo autovettore $\mathbf{x}_3$. Secondo procedimenti analoghi a prima (vedere l'equazione per $d_{ij}$), e visto che $\lambda_2 = -1$, si avrà che tale rotazione sulla base $\{\mathbf{x}_1, \mathbf{x}_2, \mathbf{x}_3 \}$ sarà:
   
   $$
   R_{-1} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & -1\end{pmatrix}
   $$

   dove $\mathbf{x}_1$ è l'asse di rotazione e quindi come abbiamo detto la rotazione è di $\pi$ attorno a tale asse;

3. $\lambda_3 = \bar{\lambda}_2$, con $\lambda_2 \in \mathbb{C}$, e nello specifico $\lambda_2 = u + iv$, per cui complessivamente:

   $$
   \lambda_2 = u + iv, \quad \lambda_3 = u - iv
   $$

   Visto che ad autovalori complessi coniugati corrispondono autovettori complessi coniugati, si avrà:
   
   $$
   \mathbf{x}_2 = \mathbf{a} + i \mathbf{b}, \quad \mathbf{x}_2 = \mathbf{a} - i \mathbf{b}
   $$

   con $\mathbf{a}$, $\mathbf{b}$ ortogonali a $\mathbf{x}_1$. Questo si ottiene dal fatto che $\lambda_2 \mathbf{x}_2 \cdot \mathbf{x}_1 = \mathbf{x}_2 \cdot \mathbf{x}_1$, e quindi:
   
   $$
   \left( u (\mathbf{a} \cdot \mathbf{x}_1) - v  (\mathbf{b} \cdot \mathbf{x}_1)\right) + i \left( v(\mathbf{a} \cdot \mathbf{x}_1) + u (\mathbf{b} \cdot \mathbf{x}_1) \right) = (\mathbf{a} \cdot \mathbf{x}_1) + i (\mathbf{b} \cdot \mathbf{x}_1)
   $$

   che uguagliando parti reali e immaginarie è:
   
   $$
   \begin{cases}(u - 1)(\mathbf{a} \cdot \mathbf{x}_1) - v(\mathbf{b} \cdot \mathbf{x}_1) = 0 \\ v(\mathbf{a}\cdot \mathbf{x}_1) - (u - 1)(\mathbf{b} \cdot \mathbf{x}_1) = 0 \end{cases}
   $$

   che non sarà mai vero in quanto $(u-1)^2+v^2\neq 0$. Possiamo quindi porre la matrice di rotazione sulla base $\{ \mathbf{x}_1, \mathbf{b}, \mathbf{a} \}$ come:
   
   $$
   R_\theta = \begin{pmatrix} 1 & 0 & 0 \\ 0 & u - i v & 0 \\ 0 & 0 & u + iv \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & u & -iv \\ 0 & iv & 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & \cos\theta & -\sin\theta \\ 0 & \sin\theta & \cos\theta \end{pmatrix}
   
   $$
   sfruttando la forma canonica di matrici con autovalori complessi per il primo passaggio, e riportandoci alla forma in coordinate polari su angolo $\theta$ (il modulo $\rho$ è nullo in quanto si parla di autovalori di unimodulari) degli autovalori $\lambda_2$, $\lambda_2$.
   
### Forma generale
Una volta trovata l'espressione della matrice di rotazione $R_\theta$ attorno all'asse $\mathbf{x}_1$ sulla base $\{ \mathbf{x}_1, \mathbf{b}, \mathbf{a} \}$, vediamo come effettuare un cambio di base dalle basi canoniche $\{ \hat{e}_1, \hat{e}_2, \hat{e}_3 \}$ a queste per ricavare la matrice di rotazione attorno ad un asse qualsiasi. Notiamo che il metodo descritto viene implementato nel seguente [Desmos](https://www.desmos.com/3d/shuxvakfym).

![[rotation.png | center | 400]]

Ciò che vogliamo calcolare è una matrice di rotazione $R$ che sia funzione di 2 parametri:
- L'*asse di rotazione* $\mathbf{x}_1$;
- L'*angolo di rotazione* $\theta$.
Abbiamo già trovato la matrice che ruota attorno all'asse $\mathbf{x}_1$ di un angolo $\theta$, espressa sulla base $\{ \mathbf{x}_1, \mathbf{b}, \mathbf{a} \}$:$$R_\theta = \begin{pmatrix} 1 & 0 & 0 \\ 0 & \cos\theta & -\sin\theta \\ 0 & \sin\theta & \cos\theta \end{pmatrix}$$
L'obiettivo sarà quindi di:
1. Trovare 2 vettori $\mathbf{a}$, $\mathbf{b}$ ortogonali a $\mathbf{x}_1$;
2. Trovare la matrice di cambio di base $Q$, dalla base $\{ \mathbf{x}_1, \mathbf{b}, \mathbf{a} \}$ alla base $\{ \hat{e}_1, \hat{e}_2, \hat{e}_3 \}$;
3. Svolgere le composizioni fra $Q$, $R_\theta$ e $Q^{-1}$ in modo che si abbia:
   $$
   R = Q \, R_\theta \, Q^{-1}
   $$
   cioè la matrice di rotazione $R$ complessiva.

Vediamo quindi i passaggi in ordine:
1.  Quello di trovare una base ortogonale (cioè due vettori ortogonali $\mathbf{a}$, $\mathbf{b}$) a partire da un dato asse $\mathbf{x}_1 = \{ x, y, z\}$ è un problema largamente discusso nel campo dell'algebra lineare e della computer. Qui si è scelto di usare il metodo dovuto a [Frisvad, 2012](https://backend.orbit.dtu.dk/ws/portalfiles/portal/126824972/onb_frisvad_jgt2012_v2.pdf):
   
   $$
   a=-\frac{1}{ \operatorname{sign}(z) + z} , \quad b = x \cdot y \cdot a
   $$
   $$
   \begin{cases} \mathbf{a} =\left(1 + \operatorname{sign}(z) \cdot x^{2} \cdot a,\ \operatorname{sign}(z) \cdot b,\ -\operatorname{sign}(z) \cdot x\right) \\ \mathbf{b} = \left(b,\ \operatorname{sign}(z) + y^{2} \cdot a,\ -a\cdot y\right) \end{cases}
   $$

2. La matrice del cambio di base $Q$, una volta trovata la base ortogonale $\{ \mathbf{x}_1, \mathbf{a}, \mathbf{b} \}$, è banale:
   
   $$
   Q = \begin{pmatrix} \mathbf{x}_1, \mathbf{b}, \mathbf{a} \end{pmatrix}
   $$
   
   Notiamo che questa ha l'inversa facile, in quanto la base che rappresenta è ortogonale, per cui $Q$ è ortogonale e vale:
   
   $$
   Q Q^T = I, \quad Q Q^{-1} = I  \implies Q^{-1} = Q^T
   $$
   
   cioè basta trasporre la matrice;

3. A questo punto siamo arrivati al risultato finale, in quanto basta prendere:
   
   $$
   R = Q \, R_\theta \, Q^{-1}
   $$
   
   cioè la matrice di rotazione $R$ complessiva. Questa rappresenterà, come volevamo, la matrice di rotazione di un angolo $\theta$ attorno all'asse arbitrario $\mathbf{x}_1$.
