Una **VPN** (*Virtual Private Network*) è un tunnel implementato sulla rete Internet globale per simulare un link punto punto fra 2 router. Questo tunnel deve avere determinate specifiche di sicurezza, che vengono implementate attraverso protocolli come **IPSec**, nonché informazioni relative alla VPN stessa, implementate ad esempio tramite il **GRE** (*Generic Routing Encapsulation*).

### IPSec
**IPSec** (da *Internet Protocol Security*) è una suite di protocolli di sicurezza che lavorano al
livello IP, permettendo crittografia, autenticazione ed integrità a livello datagramma. In questo, IP Sec riguarda sia il traffico utente che quello di controllo (DNS, ecc...)
### GRE
**GRE** (*Generic Routing Encapsulation*) viene usato in *congiunzione* ad IPSec, e non da solo, in quanto non offre da sé alcuna caratteristica di sicurezza. Un pacchetto GRE è sostanzialmente un pacchetto IP incapsulato all'interno di un altro pacchetto IP, che presenta l'header GRE. Questo contiene 2 campi:
- *Flags*, che contiene alcuni campi opzionali dell'header;
- *Protocol Type*, che specifica il tipo di pacchetto incapsulato (`0x800` per IPv4).

### Configurazione di un tunnel VPN
Un tunnel VPN su un router con [[Cisco IOS]] può essere configurato come un'interfaccia a sé, di tipo `tunnel`:
```
R1(config)#interface Tunnel0
R1(config-if)#tunnel mode gre ip
R1(config-if)#ip address 192.168.2.1 255.255.255.252 # tunnel local
R1(config-if)#tunnel source Serial0/0/0 # da chi provengono i pacchetti tunnel?
R1(config-if)#tunnel destination 198.133.219.86 # a chi inviare i pacchetti tunnel?
```

Chiaramente la stessa configurazione va fatta dall'altra parte del tunnel, sul router che riceverà i pacchetti provenienti da questo router (attraverso Internet). Entrambi i router otterranno i pacchetti dal tunnel attraverso Internet (a cui sono collegati tramite l'ISP, via porta seriale), e per rispondere dovranno nuovamente inviare pacchetti in Internet (con le `tunnel destination` configurate con gli indirizzi di rete specifici).

Solitamente le configurazioni dei tunnel sono corredate da un'istanza in esecuzione di OSPF, che provvede a portare al di là del tunnel informazioni riguardo alla topologia di rete locale.