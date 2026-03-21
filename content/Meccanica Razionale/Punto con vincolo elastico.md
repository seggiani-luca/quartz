Consideriamo un punto $P$ di massa $m$ vincolato all'origine $O$ di un opportuno sistema di riferimento $O\hat{e}_1\hat{e}_2\hat{e}_3$ da una molla elastica. Assumiamo di descrivere la molla con la legge di *Hooke* (e di assumerla a riposo a lunghezza nulla):
$$
\vec{F} = -k (P - O) = -k \vec{r}
$$
dove $k$ è la costante di *Hooke*.

In forma vettoriale in $\mathbb{V}^3$ e quindi scalare questo sarà semplicemente:
$$
m \ddot{\vec{r}}(t) = -k\vec{r}(t, \quad
\begin{cases}
\ddot{x}(t) = -\frac{k}{m}x(t) \\
\ddot{y}(t) = -\frac{k}{m}y(t) \\
\ddot{z}(t) = -\frac{k}{m}z(t) \\
\end{cases}
$$
Questo rappresenterà un sistema di *equazioni differenziali lineari* omogenee di secondo grado. Prendiamo ad esempio la prima:
$$
\ddot{x}(t) = -\frac{k}{m}x(t),\quad \ddot{x}(t) + \frac{k}{m}x(t) = 0
$$
Possiamo risolvere tale equazione riportandoci al *polinomio caratteristico* (per chiarimenti consultare i testi di analisi), cioè prendendo:
$$
x(t) = e^{\lambda t}
$$
e quindi sostituendo per ricavare l'equazione di $lambda$:
$$
\lambda^2 + \frac{k}{m} = 0, \quad \lambda^2 = - \frac{k}{m} \implies \lambda = \pm i \sqrt{\frac{k}{m}}
$$
dove diciamo $\sqrt{\frac{k}{m}} = \omega$, *pulsazione*. La soluzione generale sarà quindi data prendendo:
$$
x(t) = \alpha \cos \left( \sqrt{\frac{k}{m}} t \right) + \beta \sin \left( \sqrt{\frac{k}{m}} t \right) = A \cos \left( \sqrt{\frac{k}{m}} t + \phi \right)
$$
dalle solite proprietà delle equazioni differenziali di secondo grado, dove ci riportiamo ad una forma con *ampiezza* $A$ e *fase* $\phi$. Abbiamo quindi che la pulsazione di un corpo vincolato da una molla attorno all'origine è data da:
$$
\omega = \sqrt{\frac{k}{m}}, \quad f = \frac{\omega}{2 \pi} = \frac{1}{2\pi}\sqrt{\frac{k}{m}}
$$
