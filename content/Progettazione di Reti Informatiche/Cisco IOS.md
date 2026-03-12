**Cisco IOS** è un sistema operativo sviluppato per [[Apparati di rete]], in esecuzione sui [[Router]] e [[Switch]] a marchio Cisco.

Giusto per riassumere, notiamo quanto avevamo già detto riguardo a questi dispositivi:

> [!quote] [[Router]]
> Nello specifico, i router sono i dispositivi che si trovano al confine delle [[Local Area Network]], e che si occupano quindi di connettere più [[Local Area Network]] fra di loro attraverso il cosiddetto processo di *routing*.

I sistemi operativi per router più diffusi sono *Juniper Network Operating System* (**Junos**) della Junyper, e appunto, *Cisco Internetwork Operating System* (**IOS**).

Un sistema operativo per router dovrà assicurare le seguenti funzionalità:
- **Sicurezza** dei pacchetti instradati;
- [[Indirizzamento IP]] delle interfacce;
- Gestione delle **interfacce** su cui i pacchetti effettivamente viaggiano;
- **Routing** vero e proprio dei pacchetti (quindi l'esecuzione degli algoritmi di routing);
- **Quality of Service**: dobbiamo pensare queste macchine come dispositivi ad altissima frequenza che devono gestire migliaia di pacchetti al secondo.
Come tutti i sistemi operativi, poi, un sistema per router dovrà prevedere un livello base di gestione delle **risorse**.

### Accesso all'interfaccia
IOS offre un interfaccia a riga di comando, a cui si può accedere via Telnet, SSH (oggi più diffuso) sulla rete locale, attraverso una porta *console* dedicata, e attraverso alcune modalità legacy (come da *modem*).

![[router_cons.png|500]]

Solitamente le interfacce legacy e sopratutto la porta dedicata alla console vengono usate in caso di *disaster recovery*, cioè situazioni dove il sistema ha fallito, non si può più accedere alla rete, e si deve provvedere al riavvio dell'apparato (o eventuale troubleshooting) interagendo direttamente con la riga di comando attraverso la porta dedicata.

### Riga di comando
L'interfaccia a riga di comando di **IOS** è *modale*: esiste una gerarchia dei comandi disponibili che si articola attraverso categorie di comandi. Questo permette di avere distinzione semantica fra le categorie di comandi, e di spostarsi fra di esse come ci si sposterebbe in un *filesystem* di un sistema operativo *general purpose*, o in un menù modale di qualsiasi altro dispositivo:

![[cmds.png|800]]

Ad esempio, vediamo di avere due categorie top-level:
- *User EXEC*: i comandi che si possono eseguire senza autenticarsi. Questi sono ad esempio `ping`, `show` per l'informazione sulle interfacce, `enable` per accedere alla modalità privilegiata, ecc...
- *Privileged EXEC*: i comandi che si possono eseguire autenticandosi. Qui ad esempio abbiamo le impostazioni per *configurare* il router, le interfacce, ecc...
Il *prompt* della riga di comando riflette in ogni momento la categoria di comandi all'interno di cui ci troviamo. Ad esempio:
```
Router (config-if)#
```
significa che siamo in modalità *privilegiata* (simbolo `#` contro simbolo `>`), di configurazione (`config`) delle interfacce (`if`).

### Aiuto integrato
Cisco IOS fornisce un sistema di *aiuto* integrato accessibile digitando `?`.
- Digitandolo dopo che si è digitato qualche carattere, mostra i comandi che iniziano con i caratteri inseriti . Notiamo che in IOS un comando è preso per buono appena si digitano i caratteri prefissi minimi che non diano ambiguità con altri comandi;
- Digitandolo dopo che si è digitato un comando, e quindi uno spazio, mostra tutte le opzioni disponibili per tale comando;
- Digitandolo dopo che si è digitato un comando e un opzione, mostra il formato dell'opzione selezionata;
- Digitandolo da un terminale vuoto, lista i comandi disponibili nella modalità corrente. Ad esempio, dopo aver fatto `enable` per accedere alla modalità privilegiata, abbiamo il seguente listato:

| Comando    | Descrizione                                                 | Prefisso min. |
| ---------- | ----------------------------------------------------------- | ------------- |
| Exec       | Session number to resume                                    | `ex`          |
| auto       | Exec level Automation                                       | `au`          |
| clear      | Reset functions                                             | `cl`          |
| clock      | Manage the system clock                                     | `clo`         |
| configure  | Enter configuration mode                                    | `conf`        |
| connect    | Open a terminal connection                                  | `conn`        |
| copy       | Copy from one file to another                               | `cop`         |
| debug      | Debugging functions (see also 'undebug')                    | `deb`         |
| delete     | Delete a file                                               | `del`         |
| dir        | List files on a filesystem                                  | `di`          |
| disable    | Turn off privileged commands                                | `disa`        |
| disconnect | Disconnect an existing network connection                   | `disco`       |
| enable     | Turn on privileged commands                                 | `en`          |
| erase      | Erase a filesystem                                          | `er`          |
| exit       | Exit from the EXEC                                          | `exi`         |
| logout     | Exit from the EXEC                                          | `lo`          |
| mkdir      | Create new directory                                        | `mk`          |
| more       | Display the contents of a file                              | `mo`          |
| no         | Disable debugging informations                              | `n`           |
| ping       | Send echo messages                                          | `pi`          |
| reload     | Halt and perform a cold restart                             | `rel`         |
| resume     | Resume an active network connection                         | `resu`        |
| rmdir      | Remove existing directory                                   | `rm`          |
| send       | Send a message to other tty lines                           | `se`          |
| setup      | Run the SETUP command facility                              | `setu`        |
| show       | Show running system information                             | `sh`          |
| ssh        | Open a secure shell client connection                       | `ss`          |
| telnet     | Open a telnet connection                                    | `te`          |
| terminal   | Set terminal line parameters                                | `ter`         |
| traceroute | Trace route to destination                                  | `tr`          |
| undebug    | Disable debugging functions (see also 'debug')              | `und`         |
| vlan       | Configure VLAN parameters                                   | `vl`          |
| write      | Write running configuration to memory, network, or terminal | `wr`          |

Vediamo quindi quali sono i comandi e le funzioni più importanti di IOS.
### Comando `show`
Questo comando permette di ottenere informazioni riguardo a tutta una serie di caratteristiche e parametri del router. In particolare si ha:
- `show interfaces` - Mostra le statistiche di *livello 1* e *livello 2* per tutte le interfacce del dispositivo. Possiamo quindi usarlo per ottenere informazioni riguardo agli indirizzi MAC (`show interfaces | include address`) e altre caratteristiche di livello fisico o link delle interfacce;
- `show version` - Mostra informazioni sulla versione del software attualmente caricata, insieme alle informazioni hardware e del dispositivo;
- `show arp` - Mostra la tabella ARP del dispositivo;
- `show startup-config` - Mostra la configurazione salvata presente nella NVRAM;
- `show running-config` - Mostra il contenuto del file di configurazione attualmente in esecuzione oppure la configurazione di una specifica interfaccia o le informazioni della map class;
- `show ip interface` - Mostra le statistiche IPv4 per tutte le interfacce di un router: quindi informazioni sullo stato `up` o `down` dell'interfaccia e del protocollo, nonché l'indirizzo configurato, ecc... Per visualizzare le statistiche di una specifica interfaccia, usare il comando `show ip interface` seguito dal numero di slot/porta dell’interfaccia specifica. `show ip interface brief` è una variante del comando utile per ottenere rapidamente un riepilogo delle interfacce e del loro stato operativo:
```
Router_A#show ip interface brief
Interface            IP-Address    OK? Method Status                Protocol
GigabitEthernet0/0/0 222.222.222.1 YES manual up                    up 
GigabitEthernet0/0/1 111.111.111.1 YES manual up                    up
GigabitEthernet0/0/2 unassigned    YES unset  administratively down down
Vlan1                unassigned    YES unset  administratively down down
```

### Configurazione delle interfacce
Vediamo come si accede all'ambiente di configurazione e si configurano le interfacce montate su un router. Nella scorsa sezione abbiamo visto come `show ip interface brief` ci dà una vista panoramica di tutte le interfacce montate e il loro stato. Ad un primo avvio, si avrà che queste sono tutte `down` e senza un indirizzo IP impostato (*administratively down*). Vorremo quindi procedere con la configurazione.

Prima di tutto, notiamo che per entrare alla modalità di configurazione globale si usa `config terminal`, e quindi si sceglie un interfaccia con `interface <tipo> <numero>`. Ad esempio, per accedere all'interfaccia *GigabitEthernet* 0/0/1 di un router serie 4000:
```
Router_A#config terminal
Enter configuration commands, one per line. End with CNTL/Z.
Router_A(config)#interface gigabitethernet 0/0/1
# qui possiamo configurare
```

Vediamo quindi i comandi di base disponibili:
- `ip address` - Permette di configurare indirizzo IP e maschera dell'indirizzo (come stringa, e.g. `ip address 192.168.0.1 255.255.0.0` prende `192.168.0.1/16`, vedere [[Indirizzamento IP]]);
- `no shutdown` - Pone l'interfaccia in stato `up` se un indirizzo è valido è stato configurato. Si può quindi procedere ad usare il router.

### Configurazione delle linee
Vediamo come configurare il *terminale virtuale* del router per accedere da remoto (ad esempio da una macchina collegata direttamente o via switch a una delle interfacce del router). Faremo un breve esempio della configurazione di *Telnet*, approfondito in [[Simulazione 2]].

Per configurare i terminali virtuali, accediamo alla modalità di configurazione (come prima, con `config terminal`), e si seleziona un terminale virtuale come:
```
Router_A#config terminal
Enter configuration commands, one per line. End with CNTL/Z.
Router_A(config)#line vty 0 4
```

Qui abbiamo che `vty` seleziona i terminali virtuali. Gli altri dispositivi di linea disponibili sono:
- `tty` - I terminali *asincroni* vecchio stile accessibili via modem o linee specializzate. Oggi spesso non sono nemmeno inclusi;
- `console` - Il terminale accessibile attraverso la porta *console* presente nella maggior parte dei router.;
  `vty` - I terminali virtuali, accessibili da remoto, come quello che vogliamo configurare in questo esempio.
Gli argomenti `0` e `4`, invece, indicano che vogliamo configurare i `vty` (terminali virtuali) dal primo al quinto (solitamente ne troviamo 5 su un router, 16 nei modelli più recenti).

Le impostazioni di configurazione disponibili sono quindi:
- `login` - Attiva l'autenticazione della linea, rendendola disponibile all'accesso tramite password;
- `password` - Permette di specificare la password da usare per effettuare l'accesso, attivato tramite il comando precedente (`login`);
- `secret` - Permette di specificare una password sicura, che viene criptata prima di essere memorizzata;
- `transport input` - Permette di specificare la modalità di accesso al terminale se si parla di `vty`. In particolare, si può configurare l'accesso via *Telnet* o via *SSH* (*Secure SHell*). 

Per tornare all'esempio, vediamo come configurare un router per esporre la shell Telnet su tutte le linee `vty`:
```
# terminale router
Router_A(config)#line vty 0 4
Router_A(config-line)#login
% Login disabled on line 2, until 'password' is set
% Login disabled on line 3, until 'password' is set
% Login disabled on line 4, until 'password' is set
% Login disabled on line 5, until 'password' is set
% Login disabled on line 6, until 'password' is set
Router_A(config-line)#password router
Router_A(config-line)#login
Router_A(config-line)#transport input telnet
```

Come vediamo, prima di impostare una password, ci viene impedito di dare la configurazione `login` (in quanto non c'è una password da chiedere durante l'autenticazione). Dopo averla impostata, possiamo invece attivare il login e offrire il servizio `telnet`.

A questo punto, da una macchina esterna collegata al router, potremmo effettuare l'operazione di collegamento al router via `telnet`:
```
# terminale calcolatore (sulla sottorete del router)
C:\>telnet 222.222.222.1
Trying 222.222.222.1 ...Open
User Access Verification
Password:
Router_A>ping 222.222.222.10
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 222.222.222.10, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 0/6/17 ms
```

Qui ci siamo collegati al router all'indirizzo `222.222.222.1/24`, quindi sulla sottorete `222.222.222.0/24`, dalla macchina `222.222.222.10` (collegata al router attraverso uno switch). A scopo di test della connettività, abbiamo quindi inviato un comando `ping` dal router alla macchina stessa, che come vediamo ha avuto successo.