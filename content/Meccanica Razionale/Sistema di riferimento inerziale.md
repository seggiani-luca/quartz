Vediamo l'espressione della **prima legge di Newton** nella formulazione del moto vista in [[Equazioni del moto]].

> [!quote] [[Leggi di Newton#Prima legge di Newton]]
> Un corpo in moto con velocità $\vec{v}$ all'interno di un sistema di punti resta, se non gli viene applicata alcuna forza, nello stesso moto. In simboli:
> $$
> \vec{F}_i = 0 \implies \vec{a}_i=0
> $$

Quest'espressione è naturalmente vera definito il vettore forza $\vec{F}_i$ e assunto nullo. Abbiamo però che  l'affermazione vale solamente se si considera un [[Sistema di riferimento]] **inerziale**.

### Trasformazioni di Galileo
Consideriamo l'insieme $\mathcal{G}$ delle trasformazioni affini dello spazio-tempo di Galileo:
$$
\mathbb{G} = \mathbb{E}^3 \times \mathbb{R}
$$
visto in [[Spazio e tempo]]. Queste trasformazioni vengono dette trasformazioni di *Galileo* e rispettano le seguenti proprietà:
1. Gli *intervalli* di tempo fra due eventi vengono conservati;
2. L'*orientazione* fra eventi simultanei viene conservata;
3. La *distanza* fra eventi simultanei viene conservata.

Notiamo che, fissato un certo sistema di riferimento $\Sigma$, lo spazio di Galileo $\mathbb{G}$ è isomorfo allo spazio:
$$
\mathbb{G} \cong \mathbb{R}^3 \times \mathbb{R}
$$
per cui possiamo portare avanti i nostri calcoli vettoriali in $\mathbb{R}^3$ senza preoccuparci dello spazio affine.  Dal punto di vista matematico, quindi, i principi enunciati prima equivalgono a dire che ogni elemento $g \in \mathcal{G}$ è una trasformazione affine che può essere espressa come somma di:
1. Il *moto rettilineo uniforme* con velocità $\mathbf{u}$:
   $$
   g_1(\mathbf{x}, t) = (\mathbf{x} + t \mathbf{u}, t), \quad \mathbf{u} \in \mathbb{R}^3
   $$

2. La *traslazione dell'origine* di uno scostamento spaziale $\mathbf{y}$ e uno scostamento temporale $s$:
   $$
   g_2(\mathbf{x}, t) = (\mathbf{x} + \mathbf{y}, \, t + s). \quad \mathbf{y} \in \mathbb{R}^3, \ s \in \mathbb{R}
   $$

3. L'*isometria spaziale* attraverso una certa matrice $G$, che appunto deve essere isometrica. Le matrici isometriche in $\mathbb{R}$ sono le [[Matrici ortogonali]], e quindi ne sceglieremo una appartenente ad $O(3)$:
   $$
   g_3(\mathbf{x}, t) = (G \mathbf{x}, t), \quad G \in O(3)
   $$
### Principio di relatività di Galileo
%% completare %%
