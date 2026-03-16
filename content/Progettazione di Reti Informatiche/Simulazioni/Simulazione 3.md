Vediamo una simulazione della sottorete riportata in figura.

![[tftp_serverless.png|800]]

I punti chiave che discuteremo in questa pagina saranno:
- La cablatura della rete secondo la topologia data;
- La configurazione delle interfacce secondo la mappa di indirizzi data (riportata sotto);
- La verifica della connettività;
- Il backup della configurazione:
	- Prima su NVRAM;
	- Quindi su memoria flash;
	- Infine su un server **TFTP** (*Trivial File Transfer Protocol*) dedicato.
- Verifiche della consistenza della configurazione dopo riavvi, su entrambi i mezzi.

### Cablaggio della rete
La rete così com'è cablata comprende 3 sottoreti:
1. La sottorete 0 (con al centro lo switch 0). Questa è formata da 2 PC ed un server. Di questi, uno dei PC è collegato attraverso un cavo console al router di gateway (il router LabA). Vedremo che assegneremo a tale sottorete l'indirizzo `205.7.5.0/24`;
2. La sottorete 1 (con al centro lo switch 1). Questa è formata da 2 PC. Di questi, uno dei PC è collegato attraverso un cavo console al router di gateway (il router LabB). Vedremo che assegneremo a tale sottorete l'indirizzo `223.8.151.0/24`;
3. La sottorete 2. Questa è formata da un PC collegato direttamente al router LabC, sia per la connettività di rete che alla console. Notiamo che per collegare la porta Ethernet del PC direttamente alla porta Ethernet del router abbiamo bisogno di un cavo cross-over (vedere [[Cavi]]). Vedremo che assegneremo a tale sottorete l'indirizzo `219.17.100.0/24`.

Le 3 sottoreti sono quindi connesse da un (**AS**, *Autonomous System*) formato dai 3 router LabA, LabB e LabC. Gli indirizzi IP delle 3 reti nell'AS sono:
- Fra LabA e LabB sta la sottorete `204.204.7.0/24`;
- Fra LabB e LabC sta la sottorete `199.6.13.0/24`;
- Fra LabA e LabC sta la sottorete `201.100.11.0/24`.
Notiamo che questi router presentano interfacce di tipo seriale (legacy), e sono quindi connessi da cavi seriali con estremità **DTE** (*Data Terminal Equipment*) sottomesse a estremità **DCE** (*Data Communications Equipment*) che forniscono il segnale di clock.

### Configurazione delle interfacce
Per l'assegnamento dei numeri (*numerazione*) dei dispositivi viene predisposta la seguente tabella:

| Router | Porta            | Indirizzo         |
| ------ | ---------------- | ----------------- |
| LabA   | FastEthernet 0/0 | `205.7.5.1/24`    |
| LabA   | Serial 1/0       | `204.204.7.1/24`  |
| LabA   | Serial 2/0       | `201.100.11.1/24` |
| LabB   | FastEthernet 0/0 | `223.8.151.1/24`  |
| LabB   | Serial 1/0       | `204.204.7.2/24`  |
| LabB   | Serial 2/0       | `199.6.13.1/24`   |
| LabC   | FastEthernet 0/0 | `219.17.100.1/24` |
| LabC   | Serial 1/0       | `201.100.11.2/24` |
| LabC   | Serial 2/0       | `199.6.13.2/24`   |

All'interno delle sottoreti `205.7.5.1/24` (Switch0), `223.8.151.1/24` (Switch1) e `219.17.100.1/24` (Switch2) si adotta la convenzione:
```
subnet_addr.< 10 + indice PC >
```
dove l'indice 0 viene riservato al server sulla sottorete 0.

Configuriamo quindi i PC, il server e i router della rete secondo quanto discusso in [[Cisco IOS#Configurazione delle interfacce]], e come mostrato nella scorsa simulazione:

```
Router>enable
Router#config terminal
Enter configuration commands, one per line. End with CNTL/Z.
Router(config)#interface serial 1/0
Router(config-if)#ip address /* seguono tutti gli indirizzi */
```

Inoltre, sempre come mostrato negli stessi articoli, configuriamo una password (semplicemente `password`) per tutti i router:

```
Router(config)>enable
Router#config terminal
Enter configuration commands, one per line. End with CNTL/Z.
Router(config)#line console 0
Router(config-line)#login
Router(config-line)#password router
```

Questo abiliterà l'interfaccia `console` anche da porta seriale (attraverso i cavi console che abbiamo collegato ad ogni router da un PC sulla sottorete corrispondente), permettendo la configurazione con collegamento da terminale.

Una volta allocati i numeri e configurati i router, resterà solamente da configurare le route statiche (come visto in [[Tabella di routing]], in [[Cisco IOS]] o sempre nella scorsa simulazione). 
Possiamo fare questo col comando `ip route`:

```
Router>enable
Router#config terminal
Router(config)#ip route 223.8.151.1 255.255.255.0 204.204.7.2
```

A questo punto sarà possibile collegarsi da qualsiasi dispositivo in una sottorete a qualsiasi altro dispositivo nella stessa sottorete o in una delle altri sottorete (passando rispettivamente attraverso il solo switch, o attraverso switch e almeno 2 router di gateway).

### Backup della configurazione
La chiave di questo esercizio è allocare la configurazione dei router, che inizia a essere piuttosto consistente, su un qualche dispositivo di configurazione in maniera tale da renderla persistente ai riavvi della rete (di base dei singoli router). L'approccio più comune sarà quello della scrittura della configurazione su **NVRAM**. 
Vedremo quindi 2 approcci per fare il *backup* della configurazione, uno basato sul su memoria **flash**, e l'altro su un server **TFTP** dedicato.

#### Salvataggio su NVRAM
Per il salvataggio della configurazione, i router con [[Cisco IOS]] in esecuzione hanno il comando generale `copy`. Questo prende come argomento:
- Il supporto di archiviazione, che può essere la memoria flash, un server TFTP, o altri tipi di server o supporto (semplici server FTP, l'NVRAM, ecc...);
- Il file da copiare, che per noi potrà essere `startup-config`, cioè il file di configurazione caricato all'avvio, o `running-config`, cioè il file di configurazione attualmente caricato nel sistema.
Il salvataggio della `running-config` su NVRAM, cioè sulla `startup-config`, è il processo di copia più comune che facciamo su un router Cisco. All'avvio, questo caricherà di default la sua configurazione da NVRAM, rendendolo il posto più adeguato per una configurazione predefinita.

Il comando da eseguire sarà quindi:

```
Router#copy running-config startup-config
```

da shell privilegiata, o usare direttamente l'alias:

```
Router#write memory
```

#### Backup su flash
La memoria *flash* è consigliata nel caso si vogliano fare backup locali al router di configurazioni predefinite. Queste non saranno necessariamente configurazioni caricate di default all'avvio (come nel caso della NVRAM), ma vari "preset" che potremmo selezionare a piacimento al variare della configurazione della rete.

- Per copiare la configurazione corrente in un file su memoria flash useremo il comando (che mostrerà un'opportuno prompt per la selezione del file di destinazione):
```
Router#copy running-config flash:
Destination filename [running-config]? running-config.bak
Building configuration...
[OK]
```

- Per copiare una configurazione salvata alla configurazione di default corrente (in NVRAM), quindi, useremo il comando (che mostrerà un prompt simile al precedente per la selezione del file):
```
Router#copy flash: startup-config
Source filename []? startup-config.bak
Destination filename [startup-config]?
[OK]
551 bytes copied in 0.416 secs (1324 bytes/sec)
```

#### Backup su server TFTP
A volte può essere utile archiviare la configurazione di più router di un AS su un unico server centralizzato. Una buona soluzione per un server di questo tipo può essere un server TFTP, che presenta un interfaccia simile a quella di FTP.

In [[Cisco Packet Tracer]], abbiamo a disposizione diversi tipi di servizi fra quelli offerti dai server, fra cui TFTP. Creiamo quindi un server di questo tipo, e colleghiamolo ai router dell'esempio:

![[tftp_server.png|800]]

Notiamo alcuni dettagli riguardo a questa configurazione: server è collegato ai router attraverso uno switch condiviso (lo Switch TFTP). Questo porta tutti i router a formare effettivamente una rete locale, a cui assegniamo l'indirizzo riutilizzabile `192.168.0.0/24`. Chiaramente, per consentire tale configurazione dovremmo dedicare una porta Ethernet di ciascun router alla connessione allo switch (un altra porta era di per sé collegata alla sottorete che ciascun router serviva). 

A questo punto, quindi, possiamo usare il comando `copy` per copiare configurazioni su e dal server. Nello specifico:

- Per copiare la configurazione corrente in un file sul server TFTP useremo il comando (che mostrerà un'opportuno prompt per la selezione dell'indirizzo del server e del file di destinazione):
```
Router#copy running-config tftp:
Address or name of remote host []? server.labnet.com
Destination filename [RT-lab-confg]?
Writing running-config...Translating "server.labnet.com"...!!
[OK - 604 bytes]
604 bytes copied in 0 secs
```

- Per copiare una configurazione salvata su TFTP alla configurazione di default corrente (in NVRAM), quindi, useremo il comando (che mostrerà un prompt simile al precedente per la selezione del server e del file):
```
Router#copy tftp: startup-config
Address or name of remote host []? server.labnet.com
Source filename []? startup-config.bak
Destination filename [startup-config]?
[OK]
551 bytes copied in 0.416 secs (1324 bytes/sec)
```

