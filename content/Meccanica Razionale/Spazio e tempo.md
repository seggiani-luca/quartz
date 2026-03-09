Iniziamo dalle definizioni preliminari degli **spazi** in uso.

### Spazio euclideo
Si considera **spazio ambiente** lo spazio *euclideo* tridimensionale, indicato da $\mathbb{E}^3$ . Uno spazio euclideo non è altro che uno spazio affine $\mathbb{E}^3$, a cui è associato uno spazio vettoriale $\mathbb{V}^3$ detto spazio vettoriale delle *traslazioni*. Questo sarà dotato di prodotto interno detto [[Prodotto scalare]]. Quindi, riassumendo, uno spazio euclideo è composto da:
$$
\begin{cases}
\mathbb{E^3} \quad \text{(spazio affine)} \\ \mathbb{V}^3 \quad \text{(spazio vettoriale)} \\ \cdot : \mathbb{V}^3 \times \mathbb{V}^3 \rightarrow\mathbb{R} \quad \text{(prodotto scalare)}
\end{cases}
$$
### Definizione di vettore in V3
All'interno dello uno spazio vettoriale $\mathbb{V}^3$ vale la definizione *"fisica"* di vettore, cioè quella che intende un vettore come un segmento orientato con:
- *Direzione*;
- *Verso*;
- *Modulo*.
Indichiamo i vettori $\vec{v} \in \mathbb{V}^3$ di questo tipo con la notazione a *freccia*. Definiamo inoltre il vettore $0$ (o $\vec{0}$) come vettore di modulo nullo e verso e direzione qualsiasi.

Le operazioni definite in $\mathbb{V}^3$ sono le comuni:
- *Moltiplicazione* per scalare: 
  $$
   \vec{u} = \lambda \vec{v}, \quad \vec{u}, \vec{v} \in \mathbb{V}^3, \ \lambda \in \mathbb{R}
   $$
- *Somma* fra vettori:
  $$
   \vec{w} = \vec{u} + \vec{v}, \quad \vec{u}, \vec{v}, \vec{w} \in \mathbb{V}^3
   $$

Abbiamo già visto come in uno spazio vettoriale definiamo un prodotto interno detto [[Prodotto scalare]]. Come vedremo, all'interno dello spazio vettoriale $\mathbb{V}^3$ definiremo anche il [[Prodotto vettoriale]]:
$$
\times : \mathbb{V}^3 \times \mathbb{V}^3 \rightarrow \mathbb{V}^3
$$
Questo affianca il prodotto scalare ma restituisce vettori anziché scalari.

Potrebbe essere utile annotare che lo spazio vettoriale $\mathbb{V}^3$ equivale sostanzialmente (o meglio, è isomorfo a) lo spazio $\mathbb{R}^3$. In particolare diciamo che $\mathbb{R}^3$ è $\mathbb{V}^3$ fissate le basi canoniche:
$$
V^3 \cong \mathbb{R}^3
$$
Adottiamo questa distinzione per separare la concezione *"fisica"* di vettore appena vista, dalla concezione di vettore come insieme di coordinate. Useremo quindi $\mathbb{V}^3$ quando parliamo di vettori in genere, e $\mathbb{R}^3$ quando ci riferiremo esplicitamente a coordinate all'interno di un [[Sistema di riferimento]] .

Notiamo quindi che per ogni vettore possiamo ricavare i relativo [[Versore]] positivo e negativo.
### Definizione di punto in E3
Il fatto che lo spazio euclideo è sostanzialmente uno spazio affine significa che i suoi elementi sono **punti** (per questi usiamo le lettere maiuscole), e non vale la dualità *punto*/*vettore*. Per riportarci ad uno spazio vettoriale con origine nota e su cui i punti possono essere trattati come vettori avremo bisogno di un [[Sistema di riferimento]]. Formalizzando, abbiamo che scelti due punti $P$, $Q$ nello spazio $\mathbb{E}^3$ si ha:
$$
P - Q = \vec{v} \in \mathbb{V}^3, \quad P, Q \in \mathbb{E}^3
$$
cioè si ottiene il vettore di *traslazione* dallo spazio di *traslazione* $\mathbb{V}^3$. Ricordiamo che la somma:
$$
P + Q 
$$
non ha significato in $\mathbb{E}^e$. 
### Definizione di distanza
Abbiamo visto come ricavare il vettore di *traslazione* in $\mathbb{V}^3$ di una coppia $P$, $Q$ di punti in $\mathbb{E}^3$. Vediamo che inoltre, definita una norma basata sul [[Prodotto scalare]]:
$$
|\vec{v}| = \sqrt{\vec{v} \cdot \vec{v}}
$$
si potrà definire la **distanza** fra due punti $P$, $Q$ in uno spazio euclideo come:
$$
d(P, Q) = | P - Q |, \quad P, Q \in \mathbb{E}^3
$$
cioè semplicemente la norma della differenza di due punti in $\mathbb{E}^3$, che abbiamo visto nella scorsa sezione esiste ed è un vettore di traslazione in $\mathbb{V}^3$.

Come nota interessante, abbiamo visto che lo spazio euclideo è basato su uno spazio vettoriale (in verità lo si può ricavare anche dai *postulati* euclidei), equipaggiato di un prodotto scalare. Si può generalizzare lo spazio euclideo allo spazio di *Hilbert*, che permette di avere dimensioni infinite (e quindi avere vettori che non sono solo membri di uno spazio vettoriale $\mathbb{V}^n, \, n \in \mathbb{N}$, ma anche funzioni $f(x)$, ecc...).

### Spazio-tempo di Galileo
Per avere uno spazio che descriva anche l'aspetto temporale si prende lo spazio dato dal prodotto dello spazio euclideo $\mathbb{E}^3$ e $\mathbb{R}$:
$$
\mathbb{G} \, := \, \mathbb{E}^3 \times \mathbb{R}
$$
denominiamo tale spazio spazio-tempo di *Galileo*. Un elemento di questo spazio viene detto **evento**. Chiaramente, ogni evento sarà un oggetto del tipo:
$$
(P, t) \in \mathbb{G}, \quad P\in \mathbb{E}^3, \quad t \in \mathbb{R}
$$
dove il *punto* $P$ appartiene allo spazio euclideo $\mathbb{E}$ e il *tempo* $t$ appartiene a $\mathbb{R}$.

Possiamo intendere lo spazio-tempo come un fascio di spazi euclidei distinti da $t$, cioè prendere:
$$
\mathbb{E}^3 \times \{t\}, \quad t \in \mathbb{R}
$$
e ottenere infiniti spazi euclidei individuati dal parametro temporale $t$, rappresentanti situazioni nello spazio ambiente  "*congelate*" nel tempo. Le nozioni di differenza fra punti $P$, $Q$ nello spazio euclideo $\mathbb{E}^3$ e di distanza fra tali punti restano valide in $\mathbb{G}$ se si lavora all'interno di tali spazi.