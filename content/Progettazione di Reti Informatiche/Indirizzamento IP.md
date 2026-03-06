Il protocollo IPv4 è il protocollo di livello *network* storicamente associato ad Internet (anche se oggi si sta cercando di muovere verso IPv6). Un indirizzo IP è formato da un numero naturale su 32 bit, solitamente notato come una stringa dove ogni byte viene riportato come naturale e separato da punti. Ad esempio l'indirizzo `0x00000000` viene riportato come `0.0.0.0`, ecc... Per ottenere gli indirizzi IP si fa uso di configurazione manuale, o nelle [[Local Area Network]], molto più spesso, di protocolli come il **DHCP** (*Dynamic Host Resolution Protocol)*.

In questo lo spazio di indirizzamento IP è molto ridotto ($2^{32}$ indirizzi possibili, tolti gli spazi riservati alle reti locali e l'indirizzo di broadcast). Per questo motivo è stato effettivamente esaurito molto presto. Le soluzioni a questo problema sono state diverse:
- L'uso di protocolli che prevedono un maggiore spazio di indirizzamento come IPv6 (indirizzi su 128 bit, $2^{128}$ possibilità);
- Uso di meccanismi come il **NAT** (*Network Address Translation*), che permettono di "mascherare" più dispositivi dietro un unico indirizzo IP all'interno di una [[Local Area Network]].

### Classless InterDomain Routing
IPv4 supporta oggi il **CIDR** (*Classless InterDomain Routing), mentre una volta la partizione dello spazio IPv4 era classful* (basata sulla divisione naturale in blocchi da 8 bit `a.b.c.d`). Nel CIDR, i primi $n$ bit dell'indirizzo vengono destinati all'identificazione della rete, e i successivi $32 - n$ all'identificazione del dispositivo nella rete. Questo numero viene annesso all'indirizzo IP.

Risulta quindi utile essere capaci di calcolare "al volo" le maschere di bit corrispondenti ai numeri CIDR. Per questo si procede comunque a multipli di 8, cioè si considerano le maschere triviali:

| CIDR | Classe | Maschera      |
| ---- | ------ | ------------- |
| /8   | a      | 255.0.0.0     |
| /16  | a.b    | 255.255.0.0   |
| /24  | a.b.c  | 255.255.255.0 |

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
		eth_send(pckt, gateway_eth_addr)             # invia su Ethernet (gatway)
	
```
Come vediamo, nel caso in cui il dispositivo destinatario si va a trovare sulla nostra sottorete, inviamo direttamente il pacchetto a lui (aspettandoci che questo transiti attraverso [[Switch]] per arrivargli direttamente). Altrimenti, dobbiamo inoltrare il pacchetto al *default gateway* (vedere anche [[Local Area Network]].
Notiamo come in entrambe le situazioni è necessario sfruttare il protocollo **ARP** (*Address Resolution Protocol*), per tradurre gli indirizzi IP (nel primo caso del destinatario, nel secondo del gateway) in indirizzi Ethernet fisici.