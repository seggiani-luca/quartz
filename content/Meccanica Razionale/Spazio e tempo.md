Iniziamo dalle definizioni preliminari degli **spazi** in uso.

### Spazio euclideo
Si considera **spazio ambiente** lo spazio *euclideo* tridimensionale, indicato da $\mathbb{E}^3$ . Uno spazio euclideo non è altro che uno spazio vettoriale associato ad un prodotto interno detto [[Prodotto Scalare]]:
$$
\mathbb{E}^3 \, := \, \mathbb{R}^3 \quad \textit{(spazio vettoriale)}, \ \cdot : \mathbb{R}^3 \times \mathbb{R}^3 \rightarrow \mathbb{R} \quad \textit{(prodotto scalare)}
$$
Come vedremo, all'interno di uno spazio euclideo definiremo anche un [[Prodotto Vettoriale]], che affianca il prodotto scalare ma restituisce vettori anziché scalari.

Come nota interessante, abbiamo visto che lo spazio euclideo è una specializzazione di uno spazio vettoriale (in verità lo si può ricavare anche dai *postulati* euclidei), equipaggiato di un prodotto scalare. Si può generalizzare lo spazio euclideo allo spazio di *Hilbert*, che permette di avere dimensioni infinite (e quindi avere vettori che non sono solo membri di uno spazio vettoriale $\mathbb{R}^n, \, n \in \mathbb{N}$, ma anche funzioni $f(x)$, ecc...)

### Spazio-tempo di Galileo
Per avere uno spazio che descriva anche l'aspetto temporale si prende lo spazio dato dal prodotto dello spazio euclideo $\mathbb{E}^3$ e $\mathbb{R}$:
$$
\mathbb{G} \, := \, \mathbb{E}^3 \times \mathbb{R}
$$
denominiamo tale spazio spazio-tempo di *Galileo*. Un elemento di questo spazio viene detto **evento**. Chiaramente, ogni elemento di questo sarà un vettore quadridimensionale del tipo:
$$
(x, y, z, t) \in \mathbb{G}, \quad (x,y,z) \in \mathbb{E}^3, \quad t \in \mathbb{R}
$$
dove il vettore *posizione* $(x,y,z)$ appartiene allo spazio euclideo $\mathbb{E}$ e il *tempo* $t$ appartiene a $\mathbb{R}$.

Possiamo intendere lo spazio-tempo come un fascio di spazi euclidei distinti da $t$, cioè prendere:
$$
\mathbb{E}^3 \times \{t\}, \quad t \in \mathbb{R}
$$
e ottenere infiniti spazi euclidei individuati dal parametro temporale $t$, rappresentanti situazioni nello spazio ambiente  "*congelate*" nel tempo.