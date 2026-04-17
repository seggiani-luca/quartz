Abbiamo visto la definizione dei [[Sistemi meccanici]]. Un sistema meccanico (o *materiale*) si dice **discreto** se è formato da un numero finito o numerabile di punti materiali $P_i$:
$$
S = \{ P_1, ..., P_n \}
$$
con relative masse:
$$
m_1, ..., m_n
$$

### Centro di massa
Dato un sistema materiale discreto $S$ di N punti, si può calcolare il centro di massa come il punto $G$ definito da:
$$
G - A = \frac{1}{\sum_{i=1}^N m_i} \sum_{i=1}^N m_i(P_i - A)
$$
dove $A$ è un punto arbitrario dello spazio scelto a riferimento. Notiamo che questo non deve essere per forza l'origine di un sistema di riferimento (sotto lo assumeremo come tale in un [[Sistema di riferimento]] cartesiano). Questo si nota a partire dal fatto che, $\forall A$, l'equazione risulta verificata (lo si scopre semplicemente svolgendo i calcoli, o notando che il termine $\frac{1}{\sum_{i=1}^N m_i} \sum_{i=1}^N m_i(- A)$ restituisce per forza $-A$ a sinistra dell'uguaglianza).

### Sistemi omogenei
Se il sistema è **omogeneo**, si ha che tutte le masse sono uguali:
$$
m_i = m_j, \quad \forall i,j = 1,...,N
$$
In questo caso nel'equazione del centro di massa scompaiono le masse e possiamo semplicemente prendere la media aritmetica dei vettori scostamento dal riferimento:
$$
G - A = \frac{1}{N} \sum_{i=1}^N (P_i - A)
$$

### In coordinate cartesiane
Sia $\Sigma = O\hat{i}\hat{j}\hat{k}$ un [[Sistema di riferimento]] cartesiano. Visto che possiamo esprimere il generico punto $P_i$ del sistema discreto come:
$$
P_i - O = x_i \hat{i} + y_i \hat{j} + z_i \hat{k}
$$
allora, scegliendo $A = O$ come riferimento, si ottiene:
$$
G - O = \frac{1}{\sum_{i=1}^N m_i} \sum_{i=1}^N m_i(P_i - O)
$$
che esteso nelle 3 dimensioni di $\mathbb{R}^3$ dà la forma per le coordinate del punto materiale:
$$
\begin{cases}
x_G = \frac{1}{\sum_{i=1}^N m_i} \sum_{i=1}^N m_i x_i \\
y_G = \frac{1}{\sum_{i=1}^N m_i} \sum_{i=1}^N m_i y_i \\
z_G = \frac{1}{\sum_{i=1}^N m_i} \sum_{i=1}^N m_i z_i
\end{cases}
$$