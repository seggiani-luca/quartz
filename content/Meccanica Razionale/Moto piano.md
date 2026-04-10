Un [[Corpo rigido]] si dice **piano** se tutti i suoi punti giacciono su un piano (e.g. un'asta, una lamina, ecc...). Un **moto rigido piano** è quindi un moto rigido (di un corpo rigido) tale che le velocità di tutti i punti cadono su uno stesso piano fisso $\Gamma$, detto *piano del moto*.

### Sistema di riferimento
Per un moto rigido piano scegliamo il sistema fisso $\Sigma$ e il sistema solidale $\Sigma'$ come segue. Per $\Sigma$:
- $O$ appartenente al piano del moto $\Gamma$;
- $\vec{e}_1$ e $\vec{e}_2$ paralleli a $\Gamma$;
- $\vec{e}_3$ perpendicolare a $\Gamma$.
Mentre per $\Sigma'$:
- $O'$ un punto del corpo rigido $C$;
- $\vec{e}'_1$ e $\vec{e}'_2$ paralleli $\Gamma$;
- $\vec{e}'_3 = \vec{e}_3$

### Velocità angolare
La *velocità angolare* $\vec{\omega}$ di un corpo rigido che compie un moto piano è sempre perpendicolare al piano del moto, e non abbiamo bisogno di usare le [[Formule di Poisson]]. Scegliamo il sistema fisso e solidale $\Sigma$ e $\Sigma'$ come da sezione precedente. Se $\vec{e}'_1$ si ottiene da $\vec{e}_1$ mediante una rotazione antioraria di angolo $\phi(t) > 0$, ovvero si può esprimere $\vec{e}'_1$ come:
$$
\vec{e}'_1 = \cos \left( \phi(t) \right) \, \vec{e}_1 + \sin \left( \phi(t) \right) \, \vec{e}_2
$$
allora vale riguardo a $\vec{\omega}$:
$$
\vec{\omega}(t) = \frac{d}{dt} \phi(t) \, \vec{e}_3
$$
Questo si ha dal fatto che le [[Formule di Poisson]] assumevano la mappa:
$$
\frac{d}{dt} \vec{e}'_h \Bigg|_\Sigma = \vec{\omega} \times \vec{e}'_h, \quad 1 \leq h \leq 3
$$
con $\vec{e}'_h$ vettori in base di $\Sigma'$ solidale al corpo. Ora, derivando ad esempio $\vec{e}'_1$ si ottiene:
$$
\frac{d}{dt} \vec{e}'_1 = - \phi'(t) \sin\left(\phi(t)\right) \vec{e}_1 + \phi'(t) \cos\left(\phi(t)\right) \vec{e}_2 = \frac{d}{dt} \phi(t) \left( -\sin\left(\phi(t)\right) \vec{e}_1 + \cos\left(\phi(t)\right) \vec{e}_2 \right)
$$
ci basterà quindi dimostrare che $\vec{e}_3 \times \vec{e}'_1$ è uguale al fattore a destra, in quanto il fattore $\frac{d}{dt} \phi(t)$ è già comparso. Per calcolare il prodotto vettoriale scegliamo una rappresentazione in base ortonormale fissa su $\mathbb{R}^3$. Ad esempio, prendiamo $\mathbf{e}'_1$ sul piano $xy$ e $\mathbf{e}_3$ uguale alla terza base canonica $(0, 0, 1)$. In tal caso si ha:
$$
\begin{cases}
\mathbf{e}'_1 = (\cos\left(\phi(t\right), \sin\left(\phi(t\right), 0) \\
\mathbf{e}_e = (0, 0, 1)
\end{cases}
$$
e quindi il calcolo diventa:
$$
\mathbf{e}_3 \times \mathbf{e}'_1 =
\det \begin{pmatrix}
\vec{e}_1 & \vec{e}_2 & \vec{e}_3 \\
0 & 0 & 1 \\
\cos(\phi(t)) & \sin(\phi(t)) & 0
\end{pmatrix} = 
-\sin\left(\phi(t\right) \vec{e}_1 + \cos\left(\phi(t\right) \vec{e_2}
$$
che è la tesi.