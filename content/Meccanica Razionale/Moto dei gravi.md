Vediamo come usare le [[Equazioni del moto]] per studiare il moto di un corpo sottoposto ad una certa *accelerazione di gravità*. Ricordiamo che in [[Sistemi meccanici]] abbiamo detto che esistono alcune leggi che non sono invarianti alle [[Sistema di riferimento inerziale#Trasformazioni di Galileo]], che consideriamo però comunque nei nostri sistemi meccanici. L'esempio più eclatante è quello della **gravità**, che privilegia la direzione $\hat{e}_3$ negativa. 
Poniamo quindi l'accelerazione gravitazionale:
$$
\ddot{\mathbf{x}}(t) = -g \hat{e}_3
$$
dove notiamo il versore $\hat{e}_3$ è rivolto verso il *basso*, assunto un certo sistema di riferimento $O\hat{e}_1\hat{e}_2\hat{e}_3$.
Integriamo quindi come descritto in [[Equazioni del moto]] per ricavare il vettore *velocità*:
$$
\dot{\mathbf{x}}(t) = \int_{t_0}^t -g\hat{e}_3 \, d\tau = \dot{\mathbf{x}}(t_0) + g t \hat{e}_3
$$
quindi integriamo di nuovo per ricavare il vettore *posizione*:
$$
\mathbf{x}(t) = \int_{t_0}^t \dot{\mathbf{x}}(t_0) + g t \hat{e}_3 = \mathbf{x}(t_0) + t \dot{\mathbf{x}}(t_0) + \frac{1}{2} g t^2 \hat{e}_3
$$
Questo è esattamente il moto di un *grave*, cioè di un corpo sottoposto unicamente all'accelerazione gravitazionale (ad esempio, un proiettile).