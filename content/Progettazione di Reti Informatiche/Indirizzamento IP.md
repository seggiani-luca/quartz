Il protocollo IPv4 è il protocollo di livello *network* storicamente associato ad Internet (anche se oggi si sta cercando di muovere verso IPv6). Un indirizzo IP è formato da un numero naturale su 32 bit, solitamente notato come una stringa dove ogni byte viene riportato come naturale e separato da punti. Ad esempio l'indirizzo `0x00000000` viene riportato come `0.0.0.0`, ecc... Per ottenere gli indirizzi IP si fa uso di configurazione manuale, o nelle [[Local Area Network]], molto più spesso, di protocolli come il **DHCP** (*Dynamic Host Resolution Protocol)*.

In questo lo spazio di indirizzamento IP è molto ridotto ($2^{32}$ indirizzi possibili, tolti gli spazi riservati alle reti locali e l'indirizzo di broadcast). Per questo motivo è stato effettivamente esaurito molto presto. Le soluzioni a questo problema sono state diverse:
- L'uso di protocolli che prevedono un maggiore spazio di indirizzamento come IPv6 (indirizzi su 128 bit, $2^{128}$ possibilità);
- Uso di meccanismi come il **NAT** (*Network Address Translation*), che permettono di "mascherare" più dispositivi dietro un unico indirizzo IP all'interno di una [[Local Area Network]].

Una particolarità di IP è che il suo spazio di indirizzamento è *gerarchico*: diverse porzioni dell'indirizzo vengono allocate a descrivere diverse reti. Questa è una funzionalità che non solo organizza l'allocazione degli indirizzi, ma favorisce anche il processo di [[Routing dinamico]].

### Classful IPv4
Il metodo tradizionale per l'allocazione degli indirizzi è quello *classful*. In questo caso definiamo un indirizzo come composto dale 4 classi `a.b.c.d`, e consideriamo le seguenti **classi**:

| Classe | Maschera      | Primo ottetto (bit iniziali) | Range primo ottetto |
| ------ | ------------- | ---------------------------- | ------------------- |
| a      | 255.0.0.0     | `0xxxxxxx`                   | 1 – 126             |
| a.b    | 255.255.0.0   | `10xxxxxx`                   | 128 – 191           |
| a.b.c  | 255.255.255.0 | `110xxxxx`                   | 192 – 223           |

Notiamo che il primo ottetto contiene un breve codice che specifica la classe usata ( e quindi limita il numero di reti possibili per ogni classe.
La parte della maschera a `255` (un byte a `1`) definisce quindi gli indirizzi delle sottoreti, mentre la parte a `0` definisce gli indirizzi dei dispositivi su tali sottoreti.
- Per la classe `a` otteniamo $128$ reti con $16.777.214$ host per rete;
- Per la classe `b` otteniamo $16.384$ reti con $65.534$ host per rete;
- Per la classe `c` otteniamo $2.097.150$ reti con $254$ host per rete;
- C'erano quindi un blocco `d` per il *multicast*, ed un blocco `e` sperimentale.

Quello che si faceva era quindi assegnare *blocchi* di indirizzi di una certa classe (`a`, `b` o `c`) alle organizzazioni. L'ente che si occupava dell'assegnamento è (ad oggi) la **IANA** (*Internet Assigned Numbers Authority*).
Le problematiche di questo metodo è che i blocchi allocati hanno dimensione fissa, e ci sono poche scelte riguardo alla loro dimensione. Questo ha significato nel tempo un grande spreco di spazio di indirizzamento, dato ad esempio da blocchi di classe `b` che venivano allocati ma mai usati pienamente (in quanto prevedevano più dispositivi di quanto fosse realistico avere).

### Classless InterDomain Routing
IPv4 supporta oggi il **CIDR** (*Classless InterDomain Routing*), che supera la partizione dello spazio IPv4 *classful* (basata sulla divisione naturale in blocchi da 8 bit `a.b.c.d`). Nel CIDR, i primi $n$ bit dell'indirizzo vengono destinati all'identificazione della rete, e i successivi $32 - n$ all'identificazione del dispositivo nella rete. Questo numero viene annesso all'indirizzo IP.

Risulta quindi utile essere capaci di calcolare "al volo" le maschere di bit corrispondenti ai numeri CIDR. Per questo si procede comunque a multipli di 8, cioè si considerano le maschere triviali (uguali alle classi `a.b.c.d` del classful addressing):

| CIDR | Maschera      |
| ---- | ------------- |
| /8   | 255.0.0.0     |
| /16  | 255.255.0.0   |
| /24  | 255.255.255.0 |

A questo punto, per riempire i bit rimanenti conviene memorizzare la seguente tabella:

| Decimale | Binario    | Decimale inverso | Binario inverso |
| -------- | ---------- | ---------------- | --------------- |
| 0        | `00000000` | 255              | `11111111`      |
| 128      | `10000000` | 127              | `01111111`      |
| 192      | `11000000` | 63               | `00111111`      |
| 224      | `11100000` | 31               | `00011111`      |
| 240      | `11110000` | 15               | `00001111`      |
| 248      | `11111000` | 7                | `00000111`      |
| 252      | `11111100` | 3                | `00000011`      |
| 254      | `11111110` | 1                | `00000001`      |
| 255      | `11111111` | 0                | `00000000`      |

Notiamo la particolarità del CIDR /31, che può essere usato per usare due indirizzi IP in un link point-to-point.

L'uso di IPv4 CIDR permette un uso più efficiente dello spazio di indirizzamento IPv4, in quanto:
- Si può avere un *sub-netting* più granulare dei blocchi assegnati;
- All'altro estremo, si può avere *super-netting* e *route summarization* (cioè unificare route ad indirizzi con gli stessi prefissi).

### Indirizzamento dentro e fuori la sottorete
Riassumiamo quindi in breve come avviene l'indirizzamento di un dispositivo, noto il suo indirizzo IP, quando gli si vuole inviare un pacchetto. Innanzitutto si dovrà confrontare l'indirizzo del dispositivo con il nostro, e verificare se gli indirizzi di rete corrispondono, cioè:

```python
// my_addr, subnet_mask, gateway_addr noti
def send(pckt, dest_addr):
	my_subnet = my_addr & subnet_mask
	if my_subnet == addr & subnet_mask:
		# destinatario sulla nostra sottorete
		eth_addr = arp_resolve(dest_addr) # protocollo ARP (destinatario)
		eth_send(pckt, eth_addr)          # invia su Ethernet
	else:
		# destinatario su un altra sottorete
		gateway_eth_addr = arp_resolve(gateway_addr) # protocollo ARP (gateway)
		eth_send(pckt, gateway_eth_addr)             # invia su Ethernet
	
```

Come vediamo, nel caso in cui il dispositivo destinatario si va a trovare sulla nostra sottorete, inviamo direttamente il pacchetto a lui (aspettandoci che questo transiti attraverso [[Switch]] per arrivargli direttamente). Altrimenti, dobbiamo inoltrare il pacchetto al *default gateway* (vedere anche [[Local Area Network]].
Notiamo come in entrambe le situazioni è necessario sfruttare il protocollo **ARP** (*Address Resolution Protocol*), per tradurre gli indirizzi IP (nel primo caso del destinatario, nel secondo del gateway) in indirizzi [[Ethernet]] fisici.

### Indirizzi speciali
La *IANA* ha delegato alcuni range specifici di indirizzi ad uso particolare (RFC 1918). Innanzitutto, notiamo i range di indirizzi *interni*, usati per l'indirizzamento all'interno delle [[Local Area Network]], e che non ci aspettiamo possano essere usati per indirizzare host in rete.

| Classe | Range                             | CIDR             |
| ------ | --------------------------------- | ---------------- |
| A      | `10.0.0.0` - `10.255.255.255`     | `10.0.0.0/8`     |
| B      | `172.16.0.0` - `172.31.255.255`   | `172.0.0.0/12`   |
| C      | `192.168.0.0` - `192.168.255.255` | `192.168.0.0/16` |

Notiamo che in questo caso le classi non combaciano con quelle dello spazio IPv4 *classful*, in quanto il blocco B ha dimensione 12 anziché 16. 
Abbiamo quindi che di questi indirizzi:
- L’uso è libero nelle reti private:
- Non possono essere instradati su Internet pubblico (i router degli ISP sono configurati di conseguenza);
-  L’unicità globale non è garantita.
I vantaggi e svantaggi dell’uso dello spazio di indirizzi privati sono i seguenti:
- Flessibilità nella progettazione della rete grazie a un maggiore spazio di indirizzi disponibile;
- Scelta sicura quando è necessaria connettività verso l’esterno (anche se in tal caso è necessario il *Network Address Translation* (**NAT**);
- Può richiedere la rinumerazione in caso di fusione di più reti.

Altri indirizzi speciali, secondo la RFC 3330, sono:
**Indirizzi di rete e di broadcast**
  - Parte network tutta a 0;
  - Parte host tutta a 1.
**“Questa” rete**
  - 0.0.0.0/8, si riferisce agli host sorgente su "questa" rete.
**Loopback**
  - 127.0.0.1, usato dagli host per inviare traffico a sé stessi (bypassando i livelli inferiori dello stack);
  - 127.0.0.0/8 è in realtà riservato, nessun indirizzo in questo blocco dovrebbe mai apparire su una rete.
**Link-local (RFC 3297)
  - 169.254.0.0/16, può essere assegnato automaticamente da un host locale a sé stesso quando non sono disponibili altri metodi di configurazione IP;
  - Non deve essere usato come indirizzo di destinazione in pacchetti inoltrati a un router, e il TTL deve essere impostato a 1.
**Indirizzi TEST-NET**
  - 192.0.2.0/24, riservato per l’uso in documentazione e codice di esempio;
  - Non dovrebbe apparire su Internet.