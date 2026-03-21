Riguardo a quanto detto in [[Descrizione del moto]], abbiamo che un moto $\vec{r}(t)$ è detto **rettilineo** se la traiettoria del punto $P$ è una retta. Equivalentemente, possiamo dire che il vettore velocità:
$$
\vec{v}(t) = \frac{d}{dt} \vec{r}(t)
$$
ha direzione costante. Inoltre, se il modulo della velocità $|\vec{v}(t)|$ è anch'esso costante, il moto si dice **rettilineo uniforme**. 

Vediamo anche la forma vettoriale scelto un certo [[Sistema di riferimento]] $O\hat{e}_1\hat{e}_2\hat{e}_3$:
$$
\mathbf{x}(t) = \mathbf{x}(t_0) + t \dot{\mathbf{x}}(t_0), \quad
\begin{cases}
x(t) = x(t_0) + t \dot{x}(t_0) \\
y(t) = y(t_0) + t \dot{y}(t_0) \\
z(t) = z(t_0) + t \dot{z}(t_0) \\
\end{cases}
$$

### Dalle equazioni del moto
Possiamo ricavare le equazioni del moto rettilineo uniforme applicando direttamente la [[Leggi di Newton#Seconda legge di Newton]] come visto in [[Equazioni del moto]]. In particolare, prendiamo la formulazione come equazione differenziale della seconda legge di Newton, applicata ad un singolo punto materiale, ed assunto un certo sistema di riferimento $O\hat{e}_1\hat{e}_2\hat{e}_3$:
$$
m \ddot{\mathbf{x}} = m_i \dot{\mathbf{v}} = \mathbf{F} (\mathbf{x}, \dot{\mathbf{x}}, t) = 0
$$
dove abbiamo posto $\mathbf{F} = 0$, cioè forza nulla (che sono le ipotesi del moto rettilineo uniforme). Questo ci porta a dire riguardo l'accelerazione:
$$
m\ddot{\mathbf{x}}(t) = 0 \implies \ddot{\mathbf{x}}(t) = 0
$$
Possiamo quindi provare a risolvere questa equazione, notando da [[Descrizione del moto]] che dobbiamo integrare. Integriamo quindi a partire dal vettore *velocità*:
$$
\dot{\mathbf{x}}(t) = \int_{t_0}^t 0 \, d\tau = \dot{\mathbf{x}}(t_0)
$$
cioè questo rimane costante. Integriamo allora di nuovo per ottenere il vettore *posizione*:
$$
\mathbf{x}(t) = \int_{t_0}^t \mathbf{x}(\tau) \, d\tau = \int_{t_0}^t \dot{\mathbf{x}}(t_0) \, d\tau = \mathbf{x}(t_0) +  t \dot{\mathbf{x}}(t_0)
$$
Questa è esattamente l'espressione del moto rettilineo uniforme fissato un sistema di riferimento che avevamo visto prima:
$$
\mathbf{x}(t) = \mathbf{x}(t_0) + t \dot{\mathbf{x}}(t_0), \quad
\begin{cases}
x(t) = x(t_0) + t \dot{x}(t_0) \\
y(t) = y(t_0) + t \dot{y}(t_0) \\
z(t) = z(t_0) + t \dot{z}(t_0) \\
\end{cases}
$$
dove notiamo che se $\dot{\mathbf{x}}(t_0) = 0$ allora otteniamo il moto stazionario di un punto in quiete. Questo corrisponde con quanto affermato dalla [[Leggi di Newton#Prima legge di Newton]], ovvero un corpo su cui non vengono applicate forze resta in quiete o in moto rettilineo uniforme.