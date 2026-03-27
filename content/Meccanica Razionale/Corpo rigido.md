Un **corpo rigido** $C$ è un insieme (finito od infinito) di punti materiali $P$ le cui distanze reciproche rimangono costanti nel tempo, indipendentemente dal moto di $C$. Questa astrazione ci permette di trattare non più di singoli punti materiale (che avevamo ampiamente discusso a partire da [[Sistema di riferimento]] e [[Descrizione del moto]]), ma di *corpi* con una loro estensione nello spazio.

Chiamiamo la proprietà di costanza delle distanze fra i punti materiali **costante di rigidità**. Abbiamo infatti che per ogni coppia di punti $P$ e $Q$ che compongono il corpo, vale:
$$
|P(t) - Q(t)| = |P(0) - Q(0)| = k, \quad \forall t \in \mathbb{R}
$$
secondo la definizione di distanza data in [[Spazio e tempo#Definizione di distanza]].

### Sistema di riferimento solidale
Un [[Sistema di riferimento]] **solidale** è un sistema di riferimento cartesiano:
$$
\Sigma' = O' \hat{e}'_1\hat{e}'_2\hat{e}'_3
$$
tale che ogni punto $P$ di un certo corpo rigido $C$ ha coordinate $(x'_1, x'_2, x'_3)$ costanti nel tempo, cioè:
$$
\vec{v}'_P(t) = 0
$$
Questo significa che il sistema di riferimento solidale si muove assieme al corpo rigide. Notiamo che, di base, i sistemi di riferimento solidali ad un corpo rigido sono infiniti.

#### Costruzione per punti non allineati
Per costruire un sistema di riferimento solidale consideriamo un corpo rigido $C$ con almeno tre punti $P_1$, $P_2$ e $P_3$ non allineati. Esempi sono solidi e lamine indeformabili. Indichiamo con $S$ il piano generato dai vettori $P_2 - P_1$ e $P_3 - P_1$. In tal caso otteniamo un sistema $\Sigma'$ solidale a $C$ scegliendo:
- $O' = P_1$.
- $\hat{e}'_1 = \frac{ P_2 - P_1 }{ | P_2 - P_1 | }$.
- $\hat{e}'_3$ sarà uno dei due versori ortogonali al piano $S$ (normale negativa o positiva);
- $\hat{e}'_2 = \hat{e}'_3 \times \hat{e}'_1$, in maniera tale che $\Sigma'$ sia un sistema *levogiro* (come già detto in [[Prodotto vettoriale#Terne levogire e destrogire]]).

#### Costruzione per punti allineati
Consideriamo invece il caso con 3 punti tutti allineati. In tal caso basterà prendere una coppia di punti $P_1$ e $P_2$. In tal caso otteniamo un sistema $\Sigma'$ solidale a $C$ scegliendo:
- $O' = P_1$.
- $\hat{e}'_1 = \frac{ P_2 - P_1 }{ | P_2 - P_1 | }$.
- $\hat{e}'_3$ sarà uno qualsiasi degli infiniti vettori perpendicolari a $\hat{e}'_1$.
- - $\hat{e}'_2 = \hat{e}'_3 \times \hat{e}'_1$, in maniera tale che $\Sigma'$ sia un sistema *levogiro* (come già detto in [[Prodotto vettoriale#Terne levogire e destrogire]]).
Cioè, in altre parole, basta prendere una qualsiasi terna ortonormale $\{ \hat{e}'_1, \hat{e}'_2, \hat{e}'_3 \}$ con un vettore parallelo a $P_2 - P_1$.

### Velocità angolare
Il motivo per cui costruiamo i sistemi di riferimento solidali è quello di dare il seguente teorema:

> [!cite] Velocità angolare di un corpo rigido
> Sia $\Sigma$ un sistema di riferimento $O \hat{e}_1 \hat{e}_2 \hat{e}_3$ fisso. Ogni punto di un corpo rigido $C$ visto da un sistema di riferimento solidale al corpo $\Sigma'$ avrà la stessa velocità angolare $\vec{\omega}$ visto dal riferimento $\Sigma$.

cioè l'intero sistema di riferimento solidale $\Sigma'$ ha un'unica velocità angolare $\vec{\omega}$ rispetto al sistema di riferimento $\Sigma$. Vale anche il seguente teorema riguardo ai punti:

> [!cite] 
> Sia $\Sigma$ un sistema di riferimento fisso r $C$ un corpo rigido. Per ogni coppia di punti $P$ e $Q$ del corpo $C$ vale:
> $$
> \vec{v}_P = \vec{v}_Q + \vec{\omega} \times (P - Q)
> $$
> dove $\vec{\omega}$ è la velocità angolare di $C$ rispetto a $\Sigma$.

Questo significa la velocità di $P$ rispetto al sistema $\Sigma$ sarà uguale alla velocità di $Q$ rispetto a $\Sigma$, più il contributo dato dalla velocità angolare prendendo la distanza:
$$
\vec{r} = P - Q
$$
come raggio per le [[Formule di Poisson]]:
$$
\vec{v}_P = \vec{v}_Q + \vec{\omega} \times \vec{{r}}
$$

Questo teorema si ricava riprendendo le [[Formule di Poisson]] (come visto in [[Sistema di riferimento non inerziale]] e [[Sistema di riferimento in moto circolare]]), con un termine aggiuntivo di velocità:
$$
\vec{v}_P = \vec{v}_{O'} + \vec{\omega} \times (P - O') + \vec{v}'_P
$$
ora, se il sistema di riferimento $\Sigma'$ scelto è solidale a $C$, sarà per definizione:
$$
\vec{v}'_P = 0
$$
Prendiamo quindi la stessa formula per entrambi i punti $P$ e $Q$ appartenenti al corpo $C$:
- $\vec{v}_P = \vec{v}_{O'} + \vec{\omega} \times (P - O')$
- $\vec{v}_Q = \vec{v}_{O'} + \vec{\omega} \times (Q - O')$
Sottraendo membro a membro, otteniamo:
$$
\vec{v}_P - \vec{v}_Q = \vec{v}_{O'} + \vec{\omega} \times (P - O') - \vec{v}_{O'} - \vec{\omega} \times (Q - O') = \vec{\omega} \times (P - Q)
$$
che portando $\vec{v}_Q$ a destra ci dà esattamente la formula del teorema.