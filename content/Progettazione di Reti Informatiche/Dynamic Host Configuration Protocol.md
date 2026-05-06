**DHCP** (*Dynamic Host Configuration Protocol*) è un protocollo per la configurazione dinamica degli indirizzi IP degli host (assieme ad un po' di altra informazione) basato su UDP alla porta 67, e pacchetti IP in *broadcast*.

Esistono alcune alternative a DHCP che non vedremo, fra cui:
- Reverse ARP;
- **BOOTP** (*Bootstrap Protocol*), un protocollo ormai legacy, con cui DHCP è compatibile nel formato dei messaggi.

### Allocazione degli indirizzi
DHCP consiste sostanzialmente in:
- Un *protocollo* per la trasmissione di parametri di configurazione agli host;
- Un *meccanismo* di allocazione di un blocco di indirizzi.
Esistono 3 modalità di allocazione degli indirizzi:
1. **Manuale**: l'amministratore assegna un indirizzo ad un host (nota qualche informazione come il MAC), e il server DHCP fornisce l'informazione preconfigurata all'host;
2. **Automatico**: il server assegna un indirizzo in maniera *permanente* ma *automatica* (prelevando da un certo pool di indirizzi) agli host che si collegano alla rete. Gli host quindi mantengono gli indirizzi in maniera, appunto, permanente;
3. **Dinamico**: il server assegna un indirizzo ad un host per un lasso di tempo limitato, cioè in qualche modo lo dà in noleggio (*leasing*). Scaduto il tempo (*lease time*) l'host deve rinnovare il *lease* dell'indirizzo che ha, o fare il lease di un nuovo indirizzo.

### Funzionamento di DHCP
DHCP può trovarsi, nella comunicazione con un host, in uno di 4 stati principali:
- **Initializing**, dove il server è in *idle*, e si aspetta che il client invii un messaggio DHCPDISCOVER per richiedere i servizi di un server DHCP sulla rete;
- **Selecting**, dove il server riceve il DHCPDISCOVER, ed inizia ad offrire indirizzi IP liberi al client attraverso messaggi DHCPOFFER;
- **Requesting**, in cui si entra quando il client richiede effettivamente di usare uno degli indirizzi offerti dal server DHCP attraverso un messaggio DHCPREQUEST;
  **Bound**, in cui il server conferma il lease dell'indirizzo attraverso un messaggio DHCPACK.
Tutti questi messaggi sono in *broadcast* (inclusi gli ACK), in quanto inizialmente l'host non ha un indirizzo IP proprio, né l'indirizzo IP del server DHCP sulla rete.

Successivamente alla fase bound, prima della scadenza del lease, ci possono essere diverse situazioni:
- Prima della scadenza del 50% del lease, il client tenta un nuovo DHCPREQUEST (stavolta in unicast al server) sull'indirizzo che ha, in modo da rinnovarlo (**renewing**);
- Se il renewing fallisce, viene rilasciato il lease (con DHCPRELEASE, a cui il server risponde con DHCPNACK), o comunque si supera l'87.5% del lease, si inoltra un nuovo DHCPREQUEST in broadcast al server per ottenere un nuovo indirizzo (**rebinding**).

Il diagramma di stato è quindi il seguente:

![[dhcp_state.png]]

### Pacchetto DHCP
Il pacchetto DHCP si presenta come segue:
![[dhcp_pkt.png]]

Dove quindi abbiamo:
- Alcune informazioni che non ci interessano, come l'*operation code*, l'*hardware type* e il numero di *hop*;
- L'identificatore di *transazione*, scelto dal client usa per distinguere la sua richiesta;
- *Indirizzi IP* già esistenti di client e server (`0.0.0.0` al client se questo ancora non ha un indirizzo IP configurato);
- Il *gateway* con cui il client accede a DHCP;
- L'indirizzo *hardware* del client (cioè il MAC);
- Il *nome del server* che risponde alla richiesta DHCP;
- Il nome del file di boot (per compatibilità con BOOTP).
Seguono diverse opzioni, che vengono usate per informare il client riguardo ad altre caratteristiche della rete, fra cui ad esempio l'indirizzo del server DNS installato:

![[dhcp_opt.png]]

### Configurazione su router
I router con [[Cisco IOS]] in esecuzione possono comportarsi di per sé da server DHCP, permettendo quindi di definire un server DHCP per porta collegata ad una sottorete. Questo si può fare come segue:
```
R1(config)# ip dhcp excluded-address 192.168.10.1 192.168.10.9
R1(config)# ip dhcp excluded-addresss 192.168.10.254
R1(config)# ip dhcp pool LAN-POOL-1 # definisce la pool di indirizzi
R1(dhcp-config)# network 192.168.10.0 255.255.255.0
R1(dhcp-config)# default-router 192.168.10.1
R1(dhcp-config)# domain-name span.com
R1(dhcp-config)# end
```

### Relay DHCP
Non è sempre utile avere un server DHCP per sottorete, o sfruttare il DHCP fornito dai router. Per questo motivo DHCP supporta l'uso di router come **relay**, o *inoltro*. L'inoltro DHCP è una funzionalità utilizzata da uno switch (noto anche come **relay agent**, o *agente di inoltro*), per consentire la comunicazione DHCP tra gli host e i server DHCP remoti che non si trovano sulla stessa rete.

Quando un client invia una trasmissione DHCP per un indirizzo IP, l'agente di inoltro inoltra la richiesta alla sottorete in cui risiede il server DHCP remoto, e quindi riporta la risposta al client che ha iniziato la transazione. 

La configurazione dei relay DHCP si fa come visto in [[Simulazione 5]], cioè usando il comando di configurazione `ip helper-address`.