Abbiamo visto in [[Configurazione OSPF]] come configurare il protocollo [[OSPF]] sui router con [[Cisco IOS]]. Vediamo quindi come configurare esplicitamente più **aree** OSPF per un router.

Chiaramente, configurare più aree si farà col già visto comando `network`:
```
R2(config)#router ospf 1
R2(config-router)#network 192.168.10.2 0.0.0.0 area 0 # area 0
R2(config-router)#network 192.168.10.9 0.0.0.0 area 0
R2(config-router)#network 10.10.0.1 0.0.0.0 area 1    # area 1
R2(config-router)#network 10.10.1.1 0.0.0.0 area 1
```

### Summarization
La [[Route summarization]] non viene eseguita di default su OSPF dai router Cisco, ma va configurata sugli ABR in modo tale che il traffico rivolto all'area che gestiscono (o che comunque vogliono oscurare) sia riassunto verso la loro porta di ingresso. Per far ciò esiste il comando di configurazione `area`:
```
Router(config-router)#area <area-id> range <address> <mask>
```
dove `area-id` è chiaramente l'id dell'area verso cui vogliamo riassumere, e `address` e `mask` descrivono il range di indirizzi che vogliamo riassumere come riferiti a tale area.

### Backbone
Notiamo in particolare che l'area 0 è l'area di **backbone**: abbiamo bisogno di una backbone in quanto il protocollo di comunicazione fra più aree OSPF è effettivamente di tipo [[Distance Vector]] (anziché il routing inter area, che è [[Link State]]). Visto che i grafi che presentano cicli portano a problemi (come il *conteggio all'infinito*) nei sistemi DV, assicurando che esista una backbone centrale su cui viene indirizzato tutto il traffico inter-area portiamo il grafo ad essere uno *spanning tree* e risolviamo tali problemi.