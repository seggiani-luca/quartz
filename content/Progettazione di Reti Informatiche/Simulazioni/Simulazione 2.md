Vediamo un esempio più approfondito riguardante i [[Router]]. In particolare, ci interesserà interagire con i router da terminale (quindi interagendo con il sistema operativo [[Cisco IOS]]).

### Configurazione della rete
Vediamo brevemente la topologia della configurazione di rete che vogliamo configurare.

![[router_pc_telnet.png|400]]

Abbiamo un router modello Cisco serie 4000 fornito delle tre porte *Gigabit Ethernet* 0/0/0, 0/0/1 e 0/0/2. Queste saranno configurate come segue:
- La porta 0/0/0 sarà collegata ad uno switch, quindi collegato ad un calcolatore (via porta *Fast Ethernet*). Questa andrà a formare la nostra [[Local Area Network]];
- La porta 0/0/1 sarà collegata all'esterno della LAN, ad una [[Wide Area Network]], che per adesso trascuriamo.

Per configurare le due porte Gigabit Ethernet del router a questa maniera, usiamo quanto detto in [[Cisco IOS#Configurazione delle interfacce]]. In particolare accediamo all'ambiente `(configure-if)` per le 2 interfacce ed impostiamo `ip address` e `no shutdown`:
```
Router_A#config terminal
Enter configuration commands, one per line. End with CNTL/Z.
Router_A(config)#interface gigabitethernet 0/0/1
Router_A(config-if)#ip address 111.111.111.1 255.255.255.0
Router_A(config-if)#no shutdown
Router_A(config)#interface gigabitethernet 0/0/0
Router_A(config-if)#ip address 222.222.222.1 255.255.255.0
Router_A(config-if)#no shutdown
Router_A(config-if)#end
```

Al termine di tale configurazione, potremo controllare lo stato delle interfacce con `show ip interface brief`:
```
Router_A#show ip interface brief
Interface            IP-Address    OK? Method Status                Protocol
GigabitEthernet0/0/0 222.222.222.1 YES manual up                    up
GigabitEthernet0/0/1 111.111.111.1 YES manual up                    up
GigabitEthernet0/0/2 unassigned    YES unset  administratively down down
Vlan1                unassigned    YES unset  administratively down down
```

### Configurazione di Telnet
Vediamo come configurare il *terminale virtuale* del router per accedere da remoto (cioè da una macchina via switch a una delle interfacce del router) via **Telnet**. Sempre guardando a quanto scritto in [[Cisco IOS#Configurazione delle linee]], attiviamo tale funzionalità su tutte le linee `vty`:

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

### Configurazione di SSH
Telnet potrebbe risultare un protocollo porco sicuro (tutto, incluse le password, viaggia in chiaro). Un miglioramento potrebbe quindi essere dato dall'utilizzo di **SSH** (*Secure SHell*).

Impostare *SSH* è leggermente più complesso rispetto a Telnet. In particolare, dobbiamo anche impostare un nome di dominio (non significativo al protocollo in sé per sé), generare una *chiave*, e creare un *utente*. Queste operazioni si svolgono come segue nel terminale del router:

```
Router_A#config terminal
Enter configuration commands, one per line. End with CNTL/Z.
Router_A(config)#ip domain-name example.com # imposta dominio
Router_A(config)#crypto key generate rsa # genera chiave
The name for the keys will be: Router_A.example.com
Choose the size of the key modulus in the range of 360 to 4096 for your
General Purpose Keys. Choosing a key modulus greater than 512 may take
a few minutes.

How many bits in the modulus [512]:
% Generating 512 bit RSA keys, keys will be non-exportable...[OK]
Router_A(config)#username admin password admin # crea utente
Router_A(config)#end
```

Notiamo come tutte queste operazioni si svolgono nella modalità *Global Configuration*: sono infatti operazioni globali al router. Quando si procederà a configurare l'interfaccia `vty` per attivare SSH con `transport input ssh`, ci verrà subito segnalata la disponibilità di SSH:

```
Router_A(config)#line vty 0 4
*Mar 1 2:30:35.323: RSA key size needs to be at least 768 bits for ssh version 2
*Mar 1 2:30:35.323: %SSH-5-ENABLED: SSH 1.5 has been enabled
Router_A(config-line)#transport input ssh
Router_A(config-line)#end
```

A questo punto SSH sarà attivo e potremo usarlo per accedere al router da terminale remoto. Vediamo il comando specifico:

```
C:\>ssh -l admin 222.222.222.1
Password:
Router_A>
```
dove notiamo occorre specificare il nome dell'utente creato prima.

### Configurazione di `route` statiche
Vediamo di estendere la nostra rete con un altro [[Router]] e un altra [[Local Area Network]], in maniera simile a come abbiamo mostrato nella prima sezione di questa nota.

![[ip_route.png|800]]

Come vediamo, quindi, abbiamo formato due sottoreti:
- La sottorete A, con indirizzi `222.222.222.0/24`, a cui è collegato il PC0;
- La sottorete B, con indirizzi `223.223.223.0/24`, a cui è collegato il PC1.
I due router (A e B) sono collegati via Gigabit Ethernet, e si trovano sulla sottorete `111.111.111.0/24`. 

Al momento, se si prova a collegarsi al terminale PC0 a partire dal PC1 (ad esempio con un comando `ping`) si ha fallimento, in quanto il gateway (cioè il router B) non è capace di trovare un percorso alla sottorete A.

```
C:\>ping 222.222.222.10
Pinging 222.222.222.10 with 32 bytes of data:
Reply from 223.223.223.1: Destination host unreachable.
```

Anche se cerchiamo di accedere ad un indirizzo accessibile dal gateway (come ad esempio il router A, indirizzo `111.111.111.1`) non abbiamo una riposta: questo perché il router A stesso non è capace di trovare un percorso verso di noi per spedirci la risposta.

Configuriamo quindi delle `route` *statiche* fra i due router che puntino alle sottoreti che questi gestiscono. Per fare ciò accediamo alla modalità di configurazione globale e aggiungiamo il percorso specificando:
- La sottorete di destinazione, e quindi anche la sua maschera, che per il router A sarà `223.223.223.0/24` (la sottorete B), e che per il router B sarà `222.222.222.0/24` (la sottorete A);
- Il *next hop* per l'accesso a tale sottorete, che per il router A sarà `111.111.111.2` (il router B) e per il router B sarà `111.111.111.1` (il router A).
Questo si può quindi fare usando `ip route`:

```
# router A
Router_A(config)#ip route 223.223.223.0 255.255.255.0 111.111.111.2

# router B
Router_B(config)#ip route 222.222.222.0 255.255.255.0 111.111.111.1
```

A questo punto potremmo far parlare i due calcolatori attraverso la sottorete formata dai router.

```
# PC1
C:\>ping 222.222.222.10 # IP del PC0
Pinging 222.222.222.10 with 32 bytes of data:
Reply from 222.222.222.10: bytes=32 time<1ms TTL=126
Reply from 222.222.222.10: bytes=32 time<1ms TTL=126
Ping statistics for 222.222.222.10:
	Packets: Sent = 2, Received = 2, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
	Minimum = 0ms, Maximum = 0ms, Average = 0ms
```