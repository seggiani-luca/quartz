L'algoritmo **OSPF** (*Open Shortest Path First*) è un algoritmo di routing di tipo [[Link State]] aperto, e ampiamente impiegato nelle reti di router.

### AS
Un singolo dominio di routing all'interno di OSPF viene detto **AS** (*Autonomous System*). 
- Su Internet, ogni AS viene identificato da un numero centralmente assegnato. 
- Ad ogni router dentro un AS, quindi, assegniamo una stringa di 32 bit univoca, detta *router id* (che notiamo *non* è l'indirizzo IP). 
- Per supportare la scalabilità dell'operazione, quindi, ogni AS può essere ulteriormente partizionato in *aree*. Un area include un sottoinsieme di router dell'AS e le annesse interfacce. Un router appartiene ad un area se ha almeno un interfaccia connessa a tale area. Ogni area è individuata da una sua stringa di 32 bit univoca, detta *area id*.
OSPF lavora in maniera gerarchica: in ogni area il routing è gestito in maniera autonoma, e vengono definiti meccanismi per l'interscambio di informazioni fra diverse aree. Per la nostra trattazione semplificata, assumiamo che ogni AS sia formato da unica area.

### Tipi di router
I router all'interno degli AS di OSPF possono avere 2 ruoli sulla base delle loro interfacce:
- **Router interno**: tutte le interfacce nella stessa area;
- **Router di confine** dell’AS: almeno un’interfaccia collegata a un altro AS.

### Tipi di rete
Inoltre, si possono distinguere le reti in OSPF secondo la funzione che svolgono per quanto riguarda il routing. In particolare, una rete può formare:
- Uno **stub network**, cioè una rete che non ha connessioni ad altri router (e può essere solo destinataria o origine di pacchetti);
- Un **transit network**, cioè una rete che collega più router fra di loro. Questa potrà portare pacchetti diretti anche a router diversi da quelli che direttamente coinvolge (appunto, *transitare*);
- Una rete di *broadcast*, che collega fra di loro sia stub network che transit network. Nel caso di reti di broadcast, vengono designati il **DR** (*Designated Router*) e il **BDR** (*Backup Designated Router*);
- Una rete di *confine*, nel caso in cui contenga un router di confine per un AS esterno (ad esempio, il router di allaccio all'ISP).
In ogni caso, in una rete che sfrutta OSPF vengono decisi due router particolari:
- Il **DR**, *Designated Router*, che si occupa di rappresentare quella rete negli scambi (le *adiacenze*) OSPF;
- Il **BDR**, *Backup Designated Router*, che fa da backup per il DR.

### Flooding
L'algoritmo OSPF, è di tipo *Link State* (impiega Dijkstra dopo aver raccolto una descrizione della topologia di rete). Oltre a quanto detto prima riguardo agli *AS* su come questa topologia di rete è effettivamente rappresentata da OSPF, notiamo che questo usa un meccanismo di *flooding* per la diffusione delle informazioni sulla topologia fra router adiacenti. In particolare, vedremo, il flooding in OSPF è *selective*, e si svolge solo su un determinato sottoinsieme di router (*backbone*).

### Operazione di OSPF
All'avvio, il protocollo OSPF forma delle *adiacenze* coi router vicini per scambiare informazione di routing. Queste adiacenze sono scoperte in 4 fasi:
- **Scoperta dei vicini**: stabilita e mantenuta tramite lo scambio di pacchetti Hello (vedere [[Pacchetto OSPF]]). I pacchetti Hello sono inviati in multicast all’indirizzo *AllSPFRouters* (`224.0.0.5`, sta per *All Shortest Path First Routers*);
- **Comunicazione bidirezionale**: si realizza quando due vicini includono reciprocamente i rispettivi Router ID nei pacchetti Hello;
- **Sincronizzazione del database**: vengono scambiati pacchetti per garantire che entrambi i vicini abbiano informazioni identiche nei rispettivi database di stato dei link (ancora, vedere i tipi di pacchetti in [[Pacchetto OSPF]]). Ai fini di questo processo, un vicino assume il ruolo di master e l’altro di slave;
- **Adiacenza completa**: è il punto in cui lo stato di vicinanza viene promosso ad adiacenza vera e propria. Notiamo che una vicinanza può diventare adiacenza solo quando uno dei due router coinvolti è **DR** (*Designated Router*) di una rete, o **BDR** (*Backup Designated Router*), oppure quando i router fanno parte di una rete point-to-point o point-to-multipoint. Notiamo qui che per indirizzare i DR delle aree esiste l'indirizzo multicast riservato (come avevamo ALLSPFRouters per tutti i router) *ALLDRouters* (`224.0.0.6`, sta per *All Designated Routers*).

### Configurazione OSPF
Per la configurazione del protocollo e l'algoritmo OSPF nei router Cisco con [[Cisco IOS]] in esecuzione, si hanno a disposizione una serie di utility `ospf`. 

Inizialmente, per avviare il processo `ospf` si usa il comando, da ambiente di configurazione:
```
Router(config)#router ospf <process-id>
```
dove il `<process-id>` è l'indice che assegniamo al processo che stiamo per mandare in esecuzione.

Dopo aver aperto il processo `ospf` dovremmo assegnare un router ID al nostro router (che notiamo non è a priori legato all'indirizzo IP). Di base l'ordine in cui vengono controllate le sorgenti per il router ID è:
- L'indirizzo configurato col comando `router-id`;
- Il più alto fra gli indirizzi delle sue interfacce di loopback. Qui conviene fare un approfondimento su cosa è di preciso l'interfaccia di loopback.
  Nel protocollo IP un blocco di indirizzi viene allocato alle cosiddette *interfacce di loopback*, che sono interfacce virtuali gestite interamente all'interno di un singolo dispositivo. I pacchetti inviati dal dispositivo all'interfaccia di loopback vengono gestiti dallo stack di rete fino al dispatch, quindi immaginati come ricevuti dal dispositivo, e quindi gestiti nuovamente dallo stack di rete fino a tornare al livello application.
  Talvolta nei router conviene creare interfacce virtuali con indirizzi non di loopback. Condividere gli indirizzi di tali interfacce attraverso protocolli come OSPF permette ai router di pubblicizzare un indirizzo costante, non dipendente dalle interfacce (ricordiamo che un [[Router]] ha un indirizzo per interfaccia).
- Il più alto fra gli indirizzi delle sue interfacce fisiche in stato `up`.

L'uso di OSPF viene fatto dal router selettivamente sulle interfacce, sulla base della configurazione data. Per questo è predisposto il comando `network`:
```
Router(config-router)#network <network-address> <wildcard-mask> area <area-id>
```
Questo comando determina quali interfacce, per area, partecipano al processo di routing OSPF. Ogni interfaccia che ha un indirizzo corrispondente a `network-address` contribuirà al protocollo OSPF inviando e ricevendo pacchetti OSPF, e la rete specificata parteciperà agli aggiornamenti di routing OSPF.
La maschera `wildcard-mask` è il complemento a 1 della maschera di rete dell'indirizzo fornito. Si usa la `wildcard-mask` anziché la comune `subnet-mask` in quanto i primi bit della maschera potrebbero essere alternativamente a 1.
