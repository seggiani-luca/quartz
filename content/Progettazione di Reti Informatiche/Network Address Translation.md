Il **NAT** (*Network Address Translation*) è un meccanismo sviluppato per far fronte al ristretto spazio di indirizzamento fornito da IPv4. Sostanzialmente, si fa la *traduzione* degli indirizzi da uno spazio ad un altro, sia in entrata che in uscita su una certa porta del router.

Esistono 2 approcci possibili al NAT:
- **BNAT** (*Basic NAT*): consiste nel semplice mapping trasparente degli indirizzi IP;
- **NAPT** (*Network Address Port Translation*): consiste nel mapping degli indirizzi IP *e* dei numeri di porta TCP/UDP.

### Terminologia
Nel NAT distinguiamo fra:
- **Inside network**: la rete i cui indirizzi vengono tradotti. Viene detto *inside local IP* l'indirizzo assegnato ad un host sull'inside network, che deve essere privato e unico nell'organizzazione. L'*inside global IP* è invece l'indirizzo dell'host come appare all'outside network;
- **Outside network**: tutti le altre reti esterne all'*inside network*. Viene detto *outside local IP* l'indirizzo di un host esterno, come appare all'inside network. L'*outside global IP* è invece l'indirizzo IP assegnato ad un host nell'outside network.

Esistono blocchi riservati per gli indirizzi privati (cioè gli inside local IP) che possono essere usati in maniera non ristretta sulle reti private, finché non vengono inoltrati sull'Internet pubblica (i router degli ISP sono configurati per scartarli). Questi sono divisi sulla base dell [[Indirizzamento IP#Classless InterDomain Routing]]:

| Classe | Range                           | Prefisso CIDR    |
| ------ | ------------------------------- | ---------------- |
| A      | `10.0.0.0`-`10.255.255.255`     | `10.0.0.0/8`     |
| B      | `172.16.0.0`-`172.31.255.255`   | `172.16.0.0/12`  |
| C      | `192.168.0.0`-`192.168.255.255` | `192.168.0.0/16` |

Questi range di indirizzi sono utili in quanto sono gratuiti e liberi da usare su una [[Local Area Network]], ma chiaramente hanno il contro di richiedere il NAT quando ci si vuole connettere a reti esterne.

### Tipologie di NAT
Esistono 2 tipologie principali di NAT:
- **Static NAT**: la mappa da indirizzi inside local e inside global è definita staticamente, preconfigurata. Utile quando un host nell'inside network (solitamente un server) deve essere accessibile da fuori la rete;
- **Dynamic NAT**: l'associazione fra indirizzi inside local e inside global è definita in maniera dinamica, temporaneamente. Gli *indirizzi* globali usati vengono prelevati da una certa *pool* (che deve essere preconfigurata). Utile per la traduzione di tutti gli host che devono accedere alla rete esterna.

### Network Address Port Translation
Abbiamo introdotto il **NAPT** (*Network Address Port Translation*). Questo permette traduzione anche a livello dei numeri di porta TCP, per cui è ampiamente usato nelle reti di accesso.

### Application Level Gateways
Notiamo che una problematica del NAT è che alcune applicazioni smettono di funzionare quando gli indirizzi IP vengono trasportati nel payload del pacchetto (come ad esempio in FTP o in DNS). Per questo motivo si ha bisogno di **ALG** (*Application Level Gateways*).