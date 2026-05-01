Questa simulazione riguarda la configurazione della seguente rete:

![[exerc_lan.png]]

Notiamo prima alcune caratteristiche della rete. Sono previste 4 sottoreti, di cui:
- 3 composte da host utente (A, B e C);
- 1 composta da un server che fornisce servizi di rete (DHCP per le reti locali, più DNS e server Web), detta S.
L'allaccio a Internet è previsto attraverso il di frontiera *ABSR* al router dell'ISP (si assume che il link all'ISP è competenza dell'ISP stesso. 

### Allocazione degli indirizzi
Viene fornita la seguente tabella per il numero indicativo di host per sottorete:

| Sottorete | H. indicativi | H. effettivi               | Blocco allocato | H. allocati   |
| --------- | ------------- | -------------------------- | --------------- | ------------- |
| LAN A     | 25            | 25 + RA + PCA = 27         | /25             | 32 - 2 = 30   |
| LAN B     | 120           | 120 + RB + PCB = 122       | /26             | 128 - 2 = 126 |
| LAN C     | 55            | 55 + RC + PCC = 57         | /27             | 64 - 2 = 62   |
| LAN S     | 6             | 6 + S1 + RA + RB + RC = 10 | /28             | 16 - 2 = 14   |

Abbiamo già riportato in tabella il numero di host effettivi (contante le interfacce dei router e i dispositivi già presenti) per sottorete, nonché la dimensione del blocco minimo allocato per contenerli. Da questo ricaviamo che dobbiamo allocare un blocco di dimensione /25, e blocchi di dimensione /26, /27 e /28, che insieme formano un blocco da /24 lasciando spazio libero per l'allocazione dei link fra i router. Acquistiamo quindi il blocco di indirizzi:
$$
\texttt{172.16.0.0/24}
$$
Suddividiamo gli indirizzi di questo blocco fra le sottoreti come segue, partendo dalla sottorete di dimensioni più grandi (la LAN B):

| Sottorete | Indirizzo                  | H. allocati | Ultimo ottetto       |
| --------- | -------------------------- | ----------- | -------------------- |
| LAN B     | $\texttt{172.16.0.0/25}$   | 126         | $\texttt{0000 0000}$ |
| LAN C     | $\texttt{172.16.0.128/26}$ | 62          | $\texttt{1000 000}$  |
| LAN A     | $\texttt{172.16.0.192/27}$ | 30          | $\texttt{1100 0000}$ |
| LAN S     | $\texttt{172.16.0.224/28}$ | 14          | $\texttt{1110 0000}$ |
| RA - RC   | $\texttt{172.16.0.240/30}$ | 4           | $\texttt{1111 0000}$ |
| RB - RC   | $\texttt{172.16.0.244/30}$ | 4           | $\texttt{1110 1000}$ |

### Configurazione delle interfacce
Procediamo quindi a configurare le interfacce dei router ABSR, RA, RB e RC (il router dell'ISP non lo configureremo noi, ma l'ISP) come già ampiamente visto in [[Cisco IOS]] e le simulazioni [[Simulazione 2]] e [[Simulazione 3]]. Inoltre, configuriamo gli indirizzi degli host sulla rete, cioè i PC da A a C, e il server S1. Per la scelta degli indirizzi, facciamo le seguenti considerazioni:
- Gli indirizzi IP delle interfacce dei router vengono scelti dando la precedenza a quello più in alto nel workspace di [[Cisco Packet Tracer]];
- Gli host prendono gli ultimi indirizzi della rete (dopo i router).

La configurazione che otteniamo è quindi la seguente, dove vengono evidenziate le sottoreti:

![[exerc_labeled.png]]

Per concludere la configurazione degli indirizzi, configuriamo l'interfaccia $\texttt{209.165.201.34/30}$ (router ISP lato ABSR) come la route statica dall'ABSR verso l'ISP.

### Configurazione di OSPF
Vediamo di mettere l'algoritmo [[Open Shortest Path First]] in esecuzione su questa rete. A tal riguardo, scegliamo la sottorete S come area di *backbone* della rete, e il resto della sottorete come area 1. Notiamo che prendiamo il collegamento fra ASBR e router di ISP come al di fuori del nostro dominio OSPF.

Scegliamo di fare la configurazione delle aree OSPF sfruttando il meccanismo delle *wildcard mask*, per cui prendiamo il complemento delle maschere di sottorete a cui appartengono le porte di ogni router, e lo usiamo come wildcard mask per i comandi *network* con cui dichiariamo le aree. Ad esempio, per la rete LAN S (che va in area 0, di backbone), diamo il comando:
```
network 172.16.0.224 0.0.0.15 area 0
```
su ogni router che ha un'interfaccia sulla LAN S. Questo risparmia tempo in quanto si usa lo stesso comando su tutti i router.

Ci sono anche altri dettagli che notiamo:
- Usiamo `default-information originate` per il router ABSR in quanto questo contiene la route di default verso l'ISP (che andrà pubblicizzata) alle altre aree;
- Usiamo `passive-interface FastEthernet0/0` su tutti i router collegati a reti composte solo da end devices (cioè i router da A a C): questo per evitare di propagare informazione OSPF a dispositivi che non ne hanno bisogno o non sanno cosa farsene.

### Test di connettività
Proviamo a collegarci al sito web `www.labnet.com` offerto dal server `labnet`, al di là dell'ISP (quindi, per quanto ci riguarda, sull'Internet globale). Innanzitutto, perché il server `labnet` sia capace di inoltrare pacchetti sulla nostra LAN, avremo bisogno di pubblicizzare un qualche tipo di route verso la nostra LAN. Questo può essere fatto in diversi modi:
1. Attraverso il protocollo **BGP** (*Border Gateway Protocol*) potremmo configurare il router ASBR per pubblicizzare una route verso la nostra rete attraverso sé stesso, all'ISP;
2. Una soluzione forse migliore nel caso di LAN aziendali è quella di configurare il router ASBR per effettuare il **NAT** (*Network Address Translation*) degli indirizzi dalla nostra LAN verso l'esterno (quindi mantenendo attive le connessioni verso l'Internet esterna);
3. Una soluzione molto semplice è quella di configurare una singola route statica verso la nostra rete dal router dell'ISP. Questo chiaramente richiede l'accesso al router dell'ISP stesso.
Scegliamo per adesso la terza opzione, ed inseriamo una route statica nel router dell'ISP verso il blocco di indirizzi che abbiamo allocato, attraverso l'interfaccia dell'ASBR verso l'ISP ($\texttt{209.165.201.33}$):
```
ISP(config)#ip route 172.16.0.0 255.255.255.0 209.165.201.33
```

Da qui in poi le route interne alla rete sono pubblicizzate via OSPF, l'ABSR ha una route di default verso l'ISP (diffusa sempre attraverso OSPF), e il server `labnet` al di là del router dell'ISP ha la possibilità di raggiungere la nostra rete. Sfruttando il browser integrato di [[Cisco Packet Tracer]], possiamo collegarci a `www.labnet.com`.

### Configurazione DHCP
Segue la configurazione del servizio DHCP sul server S1 (all'indirizzo $\texttt{172.16.0.228}$). Questo farà da server DHCP per le LAN A, B e C. Inseriamo quindi i seguenti record:

![[exerc_dhcp.png]]

Notiamo che abbiamo bisogno di configurare l'`helper-address` per l'inoltro dei messaggi DHCP su UDP alla porta 67 (in broadcast), attraverso i router A B e C. Questo si fa come segue:
```
RB>enable
RB#configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
RB(config)#interface fa 0/0
RB(config-if)#ip helper-address 172.16.0.228 # indirizzo server DHCP
```

Possiamo provare la funzionalità di DHCP inserendo un nuovo dispositivo nella rete, ad esempio un computer portatile nella sottorete LAN A. Notiamo che non abbiamo alcun router (o comunque dispositivo) abilitato alle reti wireless nella nostra rete, per cui dovremo comunque usare un link cablato. Collegando il laptop alla nostra rete come segue:
![[excerc_laptop.png]]
vediamo che dopo un po' di tempo questo ottiene l'indirizzo $\texttt{172.16.0.195}$ (correttamente all'interno della LAN A), il gateway $\texttt{172.16.0.193}$ (cioè il router RA) e il server DNS $\texttt{172.16.0.228}$. Il laptop sarà quindi completamente configurato per navigare in rete, e potrà ad esempio accedere come tutti gli altri dispositivi a `www.labnet.com`.

### Configurazione NAT
Vediamo quindi brevemente la seconda modalità di configurazione del NAT che avevamo nominato in [[Simulazione 5#Test di connettività]]. Questa prevedeva la configurazione del *NAT* sul router di frontiera ASBR, per tradurre gli indirizzi in uscita in un range ridotto. Prevediamo quindi la seguente configurazione:
- Gli indirizzi degli host nelle LAN A e B vanno tradotti dinamicamente, utilizzando il pool di indirizzi $\texttt{209.165.201.17}$ – $\texttt{209.165.201.30}$;
- Gli indirizzi degli host nella LAN S vanno tradotti staticamente. In particolare, all’host S1 è assegnato l’indirizzo $\texttt{209.165.201.1}$.

La maggior parte della configurazione che facciamo va fatta sul router ASBR. Innanzitutto vogliamo configurare le interfacce di NAT *inside* (verso la LAN S) e di NAT *outside* (verso l'ISP):
```
interface FastEthernet0/0 # verso LAN S
ip address 172.16.0.225 255.255.255.240
ip nat inside
duplex auto
speed auto

interface Serial0/0/0 # verso router ISP
ip address 209.165.201.33 255.255.255.252
ip nat outside
```

#### NAT statico
Quindi, vorremo configurare la route statica verso il server S1. Questo sarà semplice e dato dall'unico comando:
```
ASBR(config)#ip nat inside source static 172.16.0.228 209.165.201.1
```

Da qui in poi i pacchetti in uscita dal server verranno tradotti, e viceversa verranno tradotti i pacchetti in entrata verso il server.

#### NAT dinamico
Per il NAT dinamico abbiamo bisogno di un po' più di configurazione. Innanzitutto, dobbiamo dichiarare la pool di indirizzi che metteremo a disposizione del NAT, che chiameremo `NAT-POOL`:
```
ip nat pool NAT-POOL 209.165.201.17 209.165.201.30 netmask 255.255.255.240
```

Quindi dovremmo dichiarare una *access list* che isoli le sole LAN A e B. Questo può essere fatto cumulando più comandi `access-list permit` su una singola access list come segue:
```
access-list 10 permit 172.16.0.192 0.0.0.31
access-list 10 permit 172.16.0.0 0.0.0.127
```
dove notiamo che in questo caso si è presa la access list 10.

A questo punto siamo pronti a configurare il NAT dinamico sulla access list 10, con il pool appena dichiarato (`NAT-POOL`):
```
ASBR(config)#ip nat inside source list 10 pool NAT-POOL overload
```

Da qui in poi il NAT come lo abbiamo pianificato sarà impiegato sui pacchetti in uscita e in entrata sulla rete. Come ultima modifica perché tutto funzioni, però, dobbiamo fornire al router dell'ISP un modo per reinviare i pacchetti verso la nostra LAN. Facciamo ciò definendo la route statica, come visto nell'esempio di connettività precedente:
```
ISP(config)#ip route 209.165.201.0 255.255.255.224 209.165.201.33
```

