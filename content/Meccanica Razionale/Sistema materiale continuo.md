Abbiamo visto la definizione di [[Sistema materiale discreto]]. La generalizzazione ragionevole da fare è quella di estendere il numero di punti ad infinito e realizzare quindi un **sistema materiale continuo**.

### Densità di massa
Abbiamo quindi che un sistema materiale continuo è un insieme di punti materiali la cui distribuzione è descritta da una funzione *densità di massa*:
$$
\rho : S \rightarrow [0, + \infty] , \quad ( \rho(P) > 0 )
$$
dove $S$ è il sottoinsieme dei punti dello spazio euclideo $\mathbb{E}$ che corrisponde con l'estensione del corpo:
$$
S \subset \mathbb{E}
$$
Presa una regione $V$ sottoinsieme di $S$, cioè $V \subset S$, la *massa* contenuta nella regione $V$ sarà data dall'integrale della densità di massa:
$$
m(V) = \int_V \rho(P) \, d \mu_s(P)
$$
dove $\mu_s(P)$ è la *misura* dell'elemento infinitesimo $P$ (per quanto ci riguarda, in 3 dimensioni, è l'elemento di volume $dV$. La massa dell'intero corpo sarà quindi data dall'integrale su $S$:
$$
m = m(S) = \int_S \rho(P) \, d \mu_s(P)
$$

### Sistemi omogenei
La definizione di [[Sistema materiale discreto#Sistemi omogenei]] vale anche per i sistemi materiali continui, e si applica a corpi $S$ che hanno densità di massa su $S$ costante:
$$
\rho(P) = \rho_0 \ \text{costante}
$$
Questo chiaramente semplifica l'integrale:
$$
m(V) = \rho_0 \int_V d\mu_s(P)
$$

### Centro di massa
Il *centro di massa* di un sistema materiale continuo può essere calcolato estendendo a distribuzioni di masse infinite quanto detto per un [[Sistema materiale discreto]]:
$$
G - A = \frac{1}{m} \int_S (P(s) - A) \rho(s) \, ds
$$
nel caso non omogeneo, e:
$$
G - A = \frac{\rho_0}{m} \int_S (P(s) - A) \, ds = \frac{1}{l(S)} \int_S (P(s) - A) \, ds
$$
nel caso omogeneo, dove $l(S)$ è una misura del *supporto* del sistema.