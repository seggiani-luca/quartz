Definiamo i seguenti vettori:

> [!cite] Quantità di moto
> Il vettore:
> $$\vec{Q}_i = m v_i$$
> viene detto *quantità di moto* del punto con velocità $v_i$.

> [!cite] Momento della quantità di moto
> Il vettore:
> $$K_i(A) = (P_i - A) \times \vec{Q}_i$$
> viene detto *momento della quantità di moto* del punto $P_i$, con quantità di moto $\vec{Q}_i$, rispetto al polo $A$.

Notiamo che valgono le seguenti proprietà:
- La derivata temporale della quantità di moto equivale alla forza applicata al corpo, per cui: 
  $$ \dot{\vec{Q}}_i = \vec{R}_i $$
  Questo risultato è banale in quanto:
  $$ \dot{\vec{Q}}_i = \frac{d}{dt} m v_i = m a_i = \vec{F}_i + \vec{\Phi}_i $$
  come visto in [[Reazioni vincolari]].
- La derivata temporale del momento della quantità di moto equivale alla seguente espressione:
  $$ \dot{\vec{K}}_i(A) = -\vec{v}_A \times \vec{Q}_i + \vec{M}_i(A) $$
  cioè un termine dipendente dalla velocità del polo stesso (motivo per cui preferiamo talvolta prendere poli a velocità nulla), e il momento della forza applicata al corpo. Questo si dimostra svolgendo il calcolo:
  $$ \dot{\vec{K}}_i(A) = \frac{d}{dt} \left( (P_i - A) \times \vec{Q}_i \right) = (\vec{v}_i - \vec{v}_a) \times \vec{Q}_i + (P_i - A) \times \dot{\vec{Q}_i} = -\vec{v}_A \times \vec{Q}_i + \vec{M}_i(A) $$
  in quanto $\vec{v}_i \times \vec{Q}_i = 0$ (sono vettori paralleli), e $\dot{\vec{Q}}_i$ era già noto.

### Quantità di moto e momento della quantità di moto complessivi
Si possono definire grandezze che racchiudono la quantità di moto complessiva di un sistema:

> [!cite] Quantità di moto di un sistema
> Il vettore:
> $$\vec{Q} = \sum_i \vec{Q}_i = \sum_i m v_i$$
> viene detto *quantità di moto* del sistema di punti $P_i$.

> [!cite] Momento della quantità di moto di un sistema
> Il vettore:
> $$K(A) = \sum_i K_i(A) = \sum_i (P_i - A) \times \vec{Q}_i$$
> viene detto *momento della quantità di moto* del sistema di punti $P_i$.

Si possono dimostrare le proprietà analoghe a quelle viste per i singoli punti:
$$
\begin{cases}
\dot{\vec{Q}}_i = \sum_{i = 1}^N \vec{R}_i \\
\dot{\vec{K}}(A) = - \vec{v}_A \times \vec{Q} + \sum_i \vec{M}_i(A)
\end{cases}
$$
Queste equazioni si ottengono sommando quelle ottenute per i singoli punti, e vengono dette **equazioni cardinali della dinamica**. Notiamo che queste equazioni riducono il numero di equazioni della dinamica che possiamo avere a 6 (in quanto $\vec{Q}$ e $\vec{K}(A)$ sono vettori tridimensionali). Non sono però ancora soddisfacenti, in quanto le sommatorie:
$$
\sum_{i = 1}^N \vec{R}_i, \quad \sum_i \vec{M}_i(A)
$$
sono riferite a *tutte* le forze agenti sui punti del sistema, incluse le forze *interne* al sistema stesso (praticamente impossibili da calcolare). Ciò che vogliamo mostrare è che vale:
$$
\sum_{i = 1}^N \vec{R}_i = \sum_{i = 1}^N \vec{R}^{est}_i, \quad \sum_i \vec{M}_i(A) = \sum_i \vec{M}^{est}_i(A)
$$
dove con l'$est$ ad apice intendiamo che consideriamo solo le forze *esterne* al sistema. La dimostrazione si fa ponendo che la forza agente su ogni punto del sistema sarà espressa come:
$$
\vec{F}_i = \vec{F}_i^{int} + \vec{F}_i^{est}
$$
cioè una componente interna ed una componente esterna. Ora, per la [[Leggi di Newton#Terza legge di Newton]], ad ogni azione corrisponde una reazione uguale in modulo ed opposta in verso,  cioè per ogni $\vec{F}_i^{int}$ avremo una $\vec{F}_j^{int}$ uguale in modulo ed opposta in verso all'interno del sistema stesso. Ciò che accadrà è quindi che la sommatoria:
$$
\sum_i \vec{F}_i = \sum_i \vec{F}_i^{est}
$$
in quanto tutti i termini interni si cancellano.