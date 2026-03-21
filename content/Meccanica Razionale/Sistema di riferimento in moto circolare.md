Ci interroghiamo adesso riguardo a cosa accade nel caso in cui si prende un sistema di riferimento $O\hat{e}_1\hat{e}_2\hat{e}_3$ rotante, cioè la cui origine $O$ si sposta di moto circolare, e i cui versori $\hat{e}_1\hat{e}_2\hat{e}_3$ restano allineati alla traiettoria circolare descritta. Questo sarà un [[Sistema di riferimento non inerziale]].

### Riferimento non inerziale
Abbiamo visto la definizione di [[Moto circolare]] (uniforme e non, per adesso prendiamo il caso più generale), e in particolare abbiamo ricavato le espressioni dei vettori: posizione $\vec{r}(t)$, velocità $\vec{v}(t)$, e accelerazione $\vec{a}(t)$:

> [!quote] [[Moto circolare]]
> Un moto $\vec{r}(t)$ è detto **circolare** se la traiettoria del punto $P$ è una circonferenza. Stabiliamo quindi un sistema di riferimento $O\hat{e}_1\hat{e}_2\hat{e}_3$ centrato su una circonferenza di raggio $R$, e poniamo sullo spazio vettoriale $\mathbf{V}^3$:
> $$
> \begin{cases}
> \mathbf{r}(t) = R \, \hat{r} \\
> \mathbf{v}(t) = \omega(t) R \, \hat{\theta} \\
> \mathbf{a}(t) = \alpha(t) R \, \hat{\theta} - \omega^2(t) R \, \hat{r}
> \end{cases}
> $$

Inoltre, abbiamo dato la definizione di un [[Sistema di riferimento inerziale]], notando che questo era dato da sistemi invarianti a particolari trasformazioni affini:

> [!quote] [[Sistema di riferimento inerziale#Trasformazioni di Galileo]]
>  Prendiamo la generica trasformazione affine $\Phi$ dello spazio di Galileo $\mathbb{G}$:
> $$
> \Phi \begin{pmatrix} \mathbf{x} \\ t \end{pmatrix} = 
> A \begin{pmatrix} \mathbf{x} \\ t \end{pmatrix} + \mathbf{b} , \quad A = \begin{pmatrix} G & \mathbf{u} \\ \mathbf{w}^T & a \end{pmatrix}, \quad \mathbf{b} = \begin{pmatrix} \mathbf{y} \\ s \end{pmatrix}
> $$
> che svolgendo i calcoli diventa:
> $$
> \Phi \begin{pmatrix} \mathbf{x} \\ t \end{pmatrix} =
> \begin{pmatrix} G \mathbf{x} + t\mathbf{u} + \mathbf{y}  \\ \mathbf{w}^T \mathbf{x} + ta + s \end{pmatrix}
> $$
> perché questai trasformazione sia galileiana, poniamo $w^T = 0$ e $a = 1$, per cui:
> $$
> \Phi \begin{pmatrix} \mathbf{x} \\ t \end{pmatrix} =
> \begin{pmatrix} G \mathbf{x} + t\mathbf{u} + \mathbf{y}  \\  t + s \end{pmatrix}
> $$

Visto che stavamo un sistema di riferimento $O\hat{e}_1\hat{e}_2\hat{e}_3$ rotante, cioè la cui origine $O$ si sposta di moto circolare uniforme, e i cui versori $\hat{e}_1\hat{e}_2\hat{e}_3$ restano allineati alla traiettoria circolare descritta. Notiamo che in questo caso, la matrice di trasformazione $G$ non sarà più costante (gli assi cambiano nel tempo), per cui dovremo porre:
$$
G \rightarrow G(t)
$$
Allora, il sistema descritto non sarà più inerziale (cioè rappresenterà un [[Sistema di riferimento non inerziale]]), e dovremo introdurre delle accelerazioni (date da *forze apparenti*) che rendano il sistema di riferimento coerente con le [[Leggi di Newton]].

### Relazioni di Galileo
Vediamo cosa intendiamo nel dettaglio. Per un normale [[Sistema di riferimento]] inerziale (chiamiamolo $\mathrm{in}$) le *relazioni di Galileo* che ci portavano dai vettori posizione, velocità ed accelerazione di un punto $P$ in un sistema di riferimento fisso esterno, ai vettori posizione, velocità ed accelerazione nel riferimento $P_\mathrm{in}$, erano:
$$
\begin{cases}
\mathbf{x}(t) = G \mathbf{x}_\mathrm{in}(t) + t \mathbf{u} + \mathbf{y} \\
\dot{\mathbf{x}}(t) = G \dot{\mathbf{x}}_\mathrm{in}(t) + \mathbf{u}\\
\ddot{\mathbf{x}}(t) = G \ddot{\mathbf{x}}_\mathrm{in}(t) 
\end{cases}
$$
ottenute semplicemente derivando $\mathbf{x}(t)$ in velocità ed accelerazione. Se prendiamo $G \rightarrow G(t)$, come nel riferimento in moto circolare uniforme, la situazione invece cambia. Prendiamo infatti il riferimento rotante (chiamiamolo $\mathrm{rot}$):
$$
\begin{cases}
\mathbf{x}(t) = G(t) \mathbf{x}_\mathrm{rot}(t) + t \mathbf{u} + \mathbf{y} \\
\dot{\mathbf{x}}(t) = \dot{G}(t) \mathbf{x}_\mathrm{rot}(t) + G(t) \dot{\mathbf{x}}_\mathrm{rot}(t) + \mathbf{u} \\
\ddot{\mathbf{x}}(t) = G(t) \ddot{x}_\mathrm{rot} (t) + \ddot{G}(t) \mathbf{x}_\mathrm{rot} (t) + 2 \dot{G}(t) \mathbf{x}_\mathrm{rot}(t)
\end{cases}
$$
dove $\mathbf{a}_a$:
$$
\mathbf{a}_0 = \ddot{G}(t) \mathbf{x}_\mathrm{rot} (t) + 2 \dot{G}(t) \mathbf{x}_\mathrm{rot}(t)
$$
conterrà tutte le nostre accelerazioni date da [[Sistema di riferimento non inerziale#Forze apparenti]], che ci apprestiamo a calcolare.

### Forze apparenti
Troviamo quindi le equazioni per le forze apparenti del moto circolare. Prima, mettiamoci in una situazione semplificata dove fissiamo l'origine $O$ del sistema non inerziale all'asse della rotazione, che assumiamo fermo nel tempo. Prenderemo quindi [[Matrici di rotazione]] del riferimento $R(t)$ (la $G(t)$ del paragrafo precedente), e lo scostamento dall'origine $\mathbf{y}$ e la velocità dall'origine $\mathbf{u}$ come nulle. Questo non ci disturba in quanto possiamo semplicemente comporre un moto circolare con un moto di traslazione per ritrovare tutte le forze apparenti (alla seconda derivata sia $\mathbf{y}$ che $\mathbf{u}$ sono spariti comunque).

Abbiamo quindi, partendo dal *vettore posizione*:
$$
\mathbf{x}(t) = R(t) \mathbf{x}_\mathrm{rot} (t)
$$
dove $R(t)$ sarà la matrice di rotazione attorno all'origine con velocità angolare $\omega(t)$ variabile nel tempo. 

Deriviamo una volta per ottenere il *vettore velocità*:
$$
\mathbf{v}(t) = \dot{R}(t) \mathbf{x}_\mathrm{rot}(t) + R(t) \dot{\mathbf{x}}_\mathrm{rot}(t) = \boldsymbol{\omega}(t) \times R(t) \mathbf{x}_\mathrm{rot}(t) + R(t) \mathbf{v}_\mathrm{rot}(t)
$$
dove $\boldsymbol{\omega}(t)$ è il *vettore velocità angolare* incontrato per la prima volta in [[Moto circolare]]. La derivazione formale di come quel termine appare si basa sulle [[Formule di Poisson]]. Qui ci basti dire che la derivata della matrice di trasformazione del sistema rotante $R(t)$ vista nel sistema di riferimento fisso ha una componente $\Omega (t)$, antisimmetrica. Da questo vale direttamente:
$$
\Omega (t) \, \mathbf{r} = \boldsymbol{\omega}(t) \times \mathbf{r}, \quad
\dot{R}(t) \, \mathbf{r} = \boldsymbol{\omega}(t) \times R(t) \, \mathbf{r}
$$
in quanto le matrici antisimmetriche esprimono il [[Prodotto vettoriale]] fisso a sinistra.
La $\mathbf{v}_\mathrm{rot}(t)$ è invece la velocità misurata nel sistema di riferimento rotante, cioè semplicemente la $\dot{\mathbf{x}}_\mathrm{rot}(t)$. Abbiamo quindi ottenuto due componenti:
$$
\mathbf{v}(t) = \boldsymbol{\omega}(t) \times R(t)\mathbf{x}_\mathrm{rot}(t) + R(t) \mathbf{v}_\mathrm{rot}(t) = \mathbf{v}_\mathrm{tan}(t) + R(t) \mathbf{v}_\mathrm{rot}(t)
$$
Vediamoli nel dettaglio.
- Abbiamo la *velocità tangenziale* data dalla rotazione, invisibile nel riferimento rotante:
$$
\mathbf{v}_\mathrm{tan}(t) = \boldsymbol{\omega}(t) \times R(t) \mathbf{x}_\mathrm{rot}(t)
$$
- Quindi abbiamo la velocità $\mathbf{v}_\mathrm{rot}(t)$ all'interno del sistema rotante stesso, chiaramente trasformata da $R(t)$.

Deriviamo allora un'ultima volta per ottenere il *vettore accelerazione*:
$$
\mathbf{a}(t) = \frac{d}{dt} \boldsymbol{\omega}(t) \times R(t) \mathbf{x}_\mathrm{rot}(t) + \boldsymbol{\omega}(t) \times \frac{d}{dt} R(t) \mathbf{x}_\mathrm{rot}(t) + \boldsymbol{\omega}(t) \times R(t)\mathbf{v}_\mathrm{rot}(t) + R(t) \mathbf{a}_\mathrm{rot} (t) =
$$
$$
\boldsymbol{\alpha}(t) \times \mathbf{x}_\mathrm{rot}(t) + \boldsymbol{\omega}(t) \times \left( \boldsymbol{\omega}(t) \times R(t) \mathbf{x}_\mathrm{rot}(t) + R(t) \mathbf{v}_\mathrm{rot}(t) \right) + \boldsymbol{\omega}(t) \times R(t)\mathbf{v}_\mathrm{rot}(t) + R(t) \mathbf{a}_\mathrm{rot} (t)
$$
$$
= \boldsymbol{\alpha}(t) \times \mathbf{x}_\mathrm{rot}(t) - \boldsymbol{\omega}^2(t) R(t) \mathbf{x}_\mathrm{rot}(t) + 2 \boldsymbol{\omega}(t) \times R(t) \mathbf{v}_\mathrm{rot}(t) + R(t) \mathbf{a}_\mathrm{rot} (t)
$$
Innanzitutto respiriamo. Quindi notiamo di aver ricavato 3 termini, consistenti con quello che proviamo dal punto di vista fisico:
$$
\mathbf{a}(t) = \mathbf{a}_\mathrm{eulero}(t) + \mathbf{a}_\mathrm{centrifuga}(t) + \mathbf{a}_\mathrm{coriolis}(t) + R(t) \mathbf{a}_\mathrm{rot}(t)
$$
Vediamo questi termini nel dettaglio.
- La componente tangenziale dato dalla *accelerazione angolare*, che avevamo incontrato anche in [[Moto circolare]], e che chiamiamo **forza di Eulero**:
$$
\mathbf{a}_\mathrm{eulero}(t) =  \boldsymbol{\alpha}(t) \times \mathbf{x}_\mathrm{rot}(t)
$$
- La componente di **forza centrifuga**, anche questa nota dal [[Moto circolare]]:
$$
\mathbf{a}_\mathrm{centrifuga}(t) = - \boldsymbol{\omega}^2(t) R(t) \mathbf{x}_\mathrm{rot}(t)
$$
- Una componente che non avevamo ancora incontrato, data dalla velocità del corpo in moto visto nel sistema di riferimento inerziale, e che chiamiamo **forza di Coriolis**:
$$
\mathbf{a}_\mathrm{coriolis}(t) = 2 \boldsymbol{\omega}(t) \times R(t) \mathbf{v}_\mathrm{rot}(t) 
$$
- Infine, l'accelerazione locale al riferimento rotante, chiaramente trasformata da $R(t)$.