Sia $\mathcal{M}_\mathbb{R}(n)$ l'insieme delle matrici quadrate di ordine $n \in \mathbb{N}$. Per noi, chiaramente, sarà $n = 3$. Definiamo quindi l'insieme:
$$
O(3) = \{ A \in \mathcal{M}_\mathbb{R}(n) \ \text{t.c.} \ A A^T = A^T A = I \}
$$
cioè $A$ è **ortogonale**. Chiameremo infatti questo spazio *spazio delle matrici ortogonali*, di dimensione 3. Matrici di questo tipo hanno la proprietà:
$$
A \in O(3) \implies \det(A A^T) = \det(A)^2 = 1
$$
per cui il determinante di $A$ può essere $\pm 1$ e quindi la matrice è *unimodulare*. Inoltre:
$$
|A| = \frac{|A\mathbf{x}|}{|\mathbf{x}|}, \quad A \mathbf{x} \cdot A \mathbf{x} = A A^T \mathbf{x} \cdot \mathbf{x} = \mathbf{x} \cdot \mathbf{x} \implies |A \mathbf{x}| = |\mathbf{x}|
$$
per cui le matrici ortogonali hanno modulo unitario e sono quindi **isometrie**. In verità, in $\mathbb{R}^3$, si ha che lo spazio delle isometrie corrisponde allo spazio delle matrici ortogonali, per qui data un'isometria esiste una matrice ortogonale che la rappresenta. 
Questo significa che le matrici ortogonali fungono da trasformazioni dello spazio che conservano i volumi e, per le proprietà delle trasformazioni lineari, il parallelismo delle rette nello spazio di arrivo. Trasformazioni di questo tipo per quanto ci riguarda sono:
- L'*identità*;
- Le *rotazioni*;
- Le *riflessioni*.

### [[Matrici di rotazione]]
Notiamo che lo spazio delle matrici di rotazione $SO(3)$ non è altro che un sottoinsieme dello spazio delle matrici ortogonali $O(3)$. In particolare, si ottiene imponendo alle matrici $A$ in $O(3)$ la seguente condizione:
$$
SO(3) = \{ A \in O(3) \ \text{t.c.} \ \det(A) = 1\}
$$
per cui consideriamo le sole matrici ortogonali che preservano il volume positivo. Facendo ciò, escludiamo le matrici che implicavano un operazione di *riflessione* e quindi otteniamo le matrici di rotazione attorno ad un asse detto *asse di rotazione*.