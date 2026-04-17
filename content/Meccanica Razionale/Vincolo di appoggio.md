Un **vincolo di appoggio** impone che un punto $A$ di un corpo rigido $C$ resti da un lato di una curva $\gamma$ di equazione $f(x, y) = 0$ senza attraversarla. La condizione di vincolo sarà:
$$
f(x_A, y_A) \geq 0
$$
Lo intendiamo con il fatto che il corpo può *appoggiarsi* su una curva, collidendo, prima di attraversarla.

Questo vincolo è simile al [[Carrello]]. In verità, quando il corpo sta sulla curva $\gamma$, diventa equivalente al carrello con $f(x_A, y_A) = 0$.

### Reazione vincolare
Un *appoggio ideale* (che non produce attrito) genera, ad ogni punto $A$ di contatto del corpo rigido $C$ con la guida $\gamma$, una reazione normale unilaterale:
$$
\vec{\phi}_A = \phi_A \vec{N}_A, \quad \phi_A \geq 0
$$
dove $\vec{N}_A$ è un vettore normale a $\gamma$ nel punto $A$, orientato verso la regione del piano accessibile al corpo rigido. Quando il punto $A$ cessa di essere un punto di contatto, la reazione si annulla:
$$
\vec{\phi}_A = 0
$$

Osserviamo quindi che anche la reazione vincolare è simile alla [[Carrello#Reazione vincolare]] di un carrello: tuttavia, nel caso dell'appoggio (che è un vincolo unilatero) si impone la condizione di unilateralità $\phi_A \geq 0$ (restringiamo il corpo ad una parte del piano).