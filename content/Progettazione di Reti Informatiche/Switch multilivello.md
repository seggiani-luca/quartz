Uno **switch** è solitamente un componente di livello *datalink*, a configurazione *plug and play*, che si occupa dell'instradamento di frame di livello *datalink* (solitamente [[Ethernet]]).
In alcuni tipi di rete, fra cui solitamente nell'aggancio all'ISP delle reti di casa (vedere [[Classificazione delle reti informatiche]]), si fa uso di particolari [[Switch]] che forniscono anche funzionalità di [[Router]] (i cosiddetti **switch multilivello**).

In questo caso dobbiamo notare che le porte offerte da uno switch multilivello (solitamente tutte porte Ethernet) hanno la stessa forma fisica ma diverse funzionalità. In particolare, solitamente si hanno $N+1$ porte, dove le $N$ fanno parte di uno switch (sono al livello *datalink*), e l'ultima fa parte di un router (è al livello *network*).

### VLAN
Gli switch multilivello sono utili anche nella gestione delle [[Virtual Local Area Network]] (come ampiamente discusso nell'articolo collegato). Per riassumere, è utile avere switch che si comportano anche da router (sono così praticamente tutti gli switch moderni), per effettuare il cosiddetto inter-VLAN routing.

Abbiamo in generale che le porte di uno switch possono essere configurate come *routed*, cioè come porte gestite in routing anziché in switching:
```
Switch(config-if)#no switchport # questa non viene trattata come porta switch
```

Questo sarà ad esempio il caso della porta $+1$ a cui ci riferivamo prima, o di una porta diretta verso un router nel caso di switch multilivello che gestiscono VLAN.