Avevamo visto la definizione di [[Sistema di riferimento inerziale]] come un sistema di riferimento dove si applicava il *principio di relatività galileiana*, ovvero dove le [[Leggi di Newton]] erano invarianti alle [[Sistema di riferimento inerziale#Trasformazioni di Galileo]] (traslazione costante o rettilinea uniforme dello spazio, scostamento temporale, e trasformazione ortogonale costante dello spazio).

Esistono però sistemi di riferimento utili, ma dove non si applica il principio di relatività galileiana. Un esempio semplice è quello di un sistema di riferimento accelerato, mentre uno più complesso è quello di un [[Sistema di riferimento in moto circolare]].

### Riportarsi ad un sistema inerziale
Nella meccanica classica ogni volta che si incontra un sistema di riferimento non inerziale ci si può riportare ad un sistema di riferimento inerziale. Di base, un sistema di riferimento non è inerziale rispetto a un sistema inerziale che lo contiene. Basterà allora trasformare tutte le coordinate del sistema non inerziale in coordinate del sistema inerziale.

Ad esempio, prendiamo il caso di un sistema di riferimento non inerziale (chiamiamolo $\mathrm{non}$) dove gli assi restano paralleli ad un secondo sistema di riferimento, inerziale (chiamiamolo $\mathrm{in}$). In altre parole, la matrice di trasformazione $G$ sarà costante nel tempo, ma la trasformazione presenterà una componente scostamento di posizione $\vec{r}_o$ che varia nel tempo.

Possiamo riportare il vettore posizione ($\vec{r}_\mathrm{non}$), il vettore velocità ($\vec{v}_\mathrm{non}$) e il vettore accelerazione ($\vec{a}_\mathrm{non}$), non inerziali, al sistema inerziale:
$$
\begin{cases}
\vec{r}_\mathrm{in} = \vec{r}_\mathrm{non} + \vec{r}_o \\
\vec{v}_\mathrm{in} = \vec{v}_\mathrm{non} + \vec{v}_o = \vec{v}_\mathrm{non} + \frac{d}{dt} \vec{r}_o \\
\vec{a}_\mathrm{in} = \vec{a}_\mathrm{non} + \vec{a}_o = \vec{a}_\mathrm{non} + \frac{d^2}{dt^2} \vec{r}_o \\
\end{cases}
$$
Ovvero dovremmo introdurre i componenti dati dalla traslazione, dalla velocità e dall'accelerazione dell'origine del sistema di riferimento.

### Forze apparenti
Spesso l'approccio di riportarsi ad un sistema di riferimento inerziale non è pratico per gestire il moto in un sistema di riferimento inerziale.

> [!quote] Evitare le forze apparenti
> *A simple way of dealing with this problem is, of course, to transform all coordinates to an inertial system. This is, however, sometimes inconvenient. Suppose, for example, we wish to calculate the movement of air masses in the earth's atmosphere due to pressure gradients. We need the results relative to the rotating frame, the earth, so it is better to stay within this coordinate system if possible. This can be achieved by introducing fictitious (or "non-existent") forces which enable us to apply Newton's Laws of Motion in the same way as in an inertial frame.*
> 
> -  Peter Ryder, _Classical Mechanics_, pag. 78-79

Possiamo quindi riportarci ad un sistema a cui siamo abituati (se vogliamo "*semi-inerziale*") modificando la [[Leggi di Newton#Seconda legge di Newton]] in modo da far combaciare i risultati all'interno del sistema di riferimento non inerziale con il comportamento nel sistema inerziale di riferimento. 

> [!quote] [[Leggi di Newton#Seconda legge di Newton]]
> Fra l'accelerazione $\vec{a}_i$ di un corpo di massa $m_i$ all'interno di un sistema di punti e la forza che gli viene applicata al tempo $t$, $\vec{F}_i$, vale la relazione:
> $$
> m_i \vec{a_i} = \vec{F}_i (\vec{\mathbf{x}}, \vec{\mathbf{v}}, t), \quad \forall i = 1, 2, ..., N
> $$

Modifichiamo la legge introducendo dei nuovi termini, che chiamiamo **forze apparenti** o *forze fittizie*, che saranno forze non realmente esistenti, ma subite all'interno del sistema di riferimento non inerziale.
$$
m_i \vec{a}_\mathrm{non} = \vec{F}_i (\vec{\mathbf{x}}_\mathrm{non}, \vec{\mathbf{v}}_\mathrm{non}) + \vec{F}_a (\vec{\mathbf{x}}_\mathrm{non}, \vec{\mathbf{v}}_\mathrm{non}), \quad \forall i = 1, 2, ..., N
$$

Esempi di forze apparenti che compaiono in sistemi non inerziali sono la forza di *Coriolis*, la forza di *Eulero*, e la forza *centrifuga*. In generale, queste si calcolano a partire dal moto del sistema di riferimento. Ad esempio, nell'esempio precedente, avevamo:
$$
\vec{a}_\mathrm{in} = \vec{a}_\mathrm{non} + \vec{a}_o  \\
$$
Potremmo tradurre questa $\vec{a}_o$ in una forza, ovvero dire:
$$
m \vec{a}_\mathrm{in} = m \vec{a}_\mathrm{non} + m\vec{a}_o, \quad \vec{a}_\mathrm{non} = \frac{1}{m} \left( \sum_i \vec{F}_i - \vec{F}_a \right) \\
$$
dove $\sum_i \vec{F}_i$ è la somma delle forze agenti sul generico punto $P$ nel sistema di riferimento inerziale, e $\vec{F}_a$ è la forza apparente che introduciamo, ovvero:
$$
\vec{F}_a = m\vec{a}_o
$$
Abbiamo quindi visto come si introduce una forza apparente per rendere un sistema di riferimento non inerziale (solo nella traslazione dell'origine, e non nella rotazione degli assi) coerente con le [[Leggi di Newton]].
Vedremo nel dettaglio un esempio di sistema non inerziale (comprensivo non solo di traslazione, ma anche di rotazione) in [[Sistema di riferimento in moto circolare]].