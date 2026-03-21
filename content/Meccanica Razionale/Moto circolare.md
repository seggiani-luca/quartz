Riguardo a quanto detto in [[Descrizione del moto]], abbiamo che un moto $\vec{r}(t)$ è detto **circolare** se la traiettoria del punto $P$ è una circonferenza.  

### Moto circolare uniforme
Prendiamo la velocità angolare $\omega$ come costante. In questo caso, l'approccio migliore sarà imporre la traiettoria di $\vec{r}(t)$ e ricavare velocità e accelerazione di conseguenza. Stabiliamo quindi un sistema di riferimento $O\hat{e}_1\hat{e}_2\hat{e}_3$ centrato su una circonferenza di raggio $R$, e poniamo sullo spazio vettoriale $\mathbf{V}^3$:
$$
\mathbf{r}(t) = R \left( \cos(\omega t), \sin(\omega t), 0 \right)
$$
dove $\omega$ sarà la *velocità angolare* del punto $P$ in rotazione attorno al centro. Deriviamo quindi una volta per trovare il vettore *velocità*:
$$
\mathbf{v}(t) = \dot{\mathbf{r}}(t) = R \left( -\omega \sin(\omega t), \omega \cos(\omega t), 0 \right)
$$
e una volta ancora per trovare il vettore *accelerazione*:
$$
\mathbf{a}(t) = \ddot{\mathbf{r}}(t) = R \left( -\omega^2 \cos(\omega t), -\omega^2 \sin(\omega t), 0 \right) = -\omega^2 \mathbf{r}(t)
$$
ciò che abbiamo ricavato è l'espressione dell'*accelerazione centripeta* diretta verso il centro della circonferenza. Notiamo che un modo più chiaro di porla si ha definendo il versore $\hat{r}(t)$ normalizzando $\mathbf{r}(t)$ e quindi dicendo:
$$
\ddot{\mathbf{r}}(t) = - \omega^2 R \,\hat{r}(t) = -\frac{|\mathrm{v|}^2}{R} \hat{r}(t)
$$
dove $\mathrm{v}$ è la *velocità tangenziale* del punto $P$ sulla circonferenza, legata a $\omega$ da:
$$
\omega = \frac{|\mathrm{v}|}{R}, \quad \mathrm{v} = \dot{\mathbf{r}}(t)
$$
Questo si ha semplicemente da:
$$
\mathrm{v} = \dot{\mathbf{r}}(t) = R \left( -\omega \sin(\omega t), \omega \cos(\omega t), 0 \right) \implies |\mathrm{v}| = \sqrt{ \omega^2 R^2 ( \sin^2(\omega t) + \cos^2(\omega t) ) } = \omega R
$$

### Moto circolare non uniforme
Concediamo che la velocità angolare $\omega$ vari, cioè che esista una certa *accelerazione angolare* $\alpha$. In questo caso è utile prendere i parametri angolari come funzioni di $t$, e quindi definire:
- La *posizione angolare* $\theta (t)$;
- La *velocità angolare* $\omega (t) = \frac{d}{dt} \theta (t)$;
- L'*accelerazione angolare* $\alpha (t) = \frac{d}{dt} \omega (t) = \frac{d^2}{dt^2} \theta (t)$.
Vediamo quindi due modi per descrivere la situazione dal punto di vista matematico e ricavare un espressione dell'accelerazione complessiva $\mathbf{a}(t)$ sul punto.

#### Coordinate cartesiane
Definiti i parametri angolari, e stabilito un sistema di riferimento $O\hat{e}_1\hat{e}_2\hat{e}_3$ centrato su una circonferenza di raggio $R$, poniamo sullo spazio vettoriale $\mathbf{V}^3$ la solita funzione del moto:
$$
\mathbf{r}(t) = R \left( \cos(\theta(t)), \cos(\sin(t)), 0 \right)
$$
Deriviamo quindi una volta per trovare il vettore *velocità*:
$$
\mathbf{v}(t) = \dot{\mathbf{r}}(t) 
= R \left( 
-\dot{\theta}(t) \sin(\theta(t)), 
\dot{\theta}(t) \cos(\theta(t)), 
0
\right)
= \omega(t) R \left( 
-\sin(\theta(t)), 
\cos(\theta(t)), 
0
\right)
$$
e una volta ancora per trovare il vettore *accelerazione*:
$$
\mathbf{a}(t) = \ddot{\mathbf{r}}(t)
= R \left(
-\alpha(t) \sin(\theta(t)) - \omega^2(t) \cos(\theta(t)),
\alpha(t) \cos(\theta(t)) - \omega^2(t) \sin(\theta(t)),
0
\right)
$$
$$
= \alpha(t) R \left( -\sin(\theta(t)), \cos(\theta(t)), 0 \right)
- \omega^2(t) R \left( \cos(\theta(t)), \cos(\sin(t)), 0 \right)
$$
In questa espressione abbiamo tutti i termini di cui abbiamo bisogno per descrivere le forze a cui è soggetto un punto in moto circolare arbitrario (abbiamo anche una simulazione numerica in questo [Desmos](https://www.desmos.com/3d/eieujizo24)), ma risultano abbastanza scomode da leggere. Vediamo quindi un approccio che ci permette di scrivere la stessa cosa in maniera più sintetica.

#### Con versori
Potrebbe essere utile denominare il versore $\hat{\theta}(t)$ come quello rivolto in direzione tangenziale alla circonferenza su cui ci troviamo. Questo sarà definito come:
$$
\hat{\theta}(t) = (-\sin(\theta), \cos(\theta))
$$
A questo punto l'espressione del vettore velocità sarà semplice, preso $\boldsymbol{\omega}(t)$ come il *vettore velocità angolare* un vettore allineato all'asse di rotazione con modulo pari a $\omega(t)$:
$$
\mathbf{v}(t) = \boldsymbol{\omega}(t) R \, \hat{\theta}(t)
$$
Notiamo poi che, per come abbiamo definito i nostri versori, vale:
$$
\mathbf{v}(t) = \boldsymbol{\omega}(t) \times R \, \hat{r}(t) = \boldsymbol{\omega}(t) \times \mathbf{r}(t)
$$
Ricavare l'accelerazione è quindi facile:
$$
\mathbf{a}(t) = \frac{d}{dt} \mathbf{v}(t) = \frac{d}{dt} \left( \boldsymbol{\omega}(t) \times \mathbf{r}(t) \right) 
= \frac{d}{dt} \boldsymbol{\omega}(t) \times \mathbf{r}(t) + \boldsymbol{\omega}(t) \times \frac{d}{dt} \mathbf{r}(t)
$$
$$
 =
\boldsymbol{\alpha}(t) \times \mathbf{r}(t) + \boldsymbol{\omega}(t) \times (\boldsymbol{\omega}(t) \times \mathbf{r}(t))
$$
dove $\boldsymbol{\alpha}(t)$ è il *vettore accelerazione angolare*, definito come il vettore velocità angolare ma con modulo $\alpha(t)$. Questa espressione, riportandosi ai versori, dà:
$$
\mathbf{a}(t) = \alpha(t) R \, \hat{\theta} - \omega^2(t) R \, \hat{r} = \mathbf{a}_\mathrm{tan}(t) + \mathbf{a}_\mathrm{rad}(t)
$$
cioè abbiamo scomposto l'accelerazione in una componente tangenziale data dall'accelerazione angolare:
$$
\mathbf{a}_\mathrm{tan}(t) =
\alpha(t) R \, \hat{\theta}
$$
e in una componente radiale data dall'accelerazione centripeta, uguale al caso uniforme:
$$
\mathbf{a}_\mathrm{rad}(t) =
-\omega^2(t) R \, \hat{r}
$$

![[rotating_point.png|800]]

Un esempio numerico dei calcoli fatti in questi ultimi paragrafi, che mette in evidenza la componente tangenziale dell'accelerazione, è disponibile nel seguente [Desmos]([Desmos](https://www.desmos.com/3d/yx6rmeq7ts)). 