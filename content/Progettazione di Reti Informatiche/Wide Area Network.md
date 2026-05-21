Reti come Internet vengono dette **WAN** (*Wide Area Network*) per la grande copertura che hanno. In particolare in questo tipo di rete abbiamo caratteristiche diverse:
- Tecnologie che possono essere a commutazione di *circuito* (**POTS**, *Plain Old Telephone Service*) o a commutazione di *pacchetto* (la comune rete Internet). Anche su Internet si cerca oggi di richiamare in qualche modo la filosofia della commutazione di circuito attraverso tecnologie come l'**MPLS** (*Multiprotocol Label Switching*) che intervengono sulla struttura di IP.
- Servizi digitali dedicati;
- Reti private **virtuali**, cioè che permettono la formazione di [[Local Area Network]] virtuali distribuite su un'area di copertura più grande. In questo si fanno uso di tecnologie come il tunneling **GRE** (*Generic Routing Encapsulation*) sviluppato da Cisco.

In genere le WAN sono reti che coprono aree geografiche anche vaste, gestite da un qualche *provider* di telecomunicazioni.

### Topologie di WAN
Possiamo distinguere le reti WAN sulla base della *topologia* adottata:

![[wan_topologies.png]]

Di queste notiamo:
- Topologia **point-to-point**, la più semplice, dove il provider fornisce connettività da un sito A ad un sito B;
- Topologia **hub-and-spoke**, dove il provider fornisce connettività fra più siti attraverso un *hub* centrale;
- Topologia a **full mesh**, dove il provider fornisce connettività fra tutti i suoi siti. Chiaramente questo è il caso più ridondante (e quindi a massima affidabilità);
- Topologia a **partial mesh**, una variante della full mesh dove non abbiamo tutti i link (cosa che la rende meno ridondante).

Sostanzialmente le reti locali ([[Local Area Network]]) che abbiamo studiate fanno parte della cosiddetta *Enterprise Edge*, composta dal **CPE** (*Customer Premises Equipment*). Questo è l'equipaggiamento dell'azienda, su cui l'azienda ha il controllo. Dall'altro lato c'è la *Service Provider Edge*, che comprende il *local loop* della rete dalla nostra LAN all'ufficio centrale (**CO**) del service provider, e quindi alla loro rete WAN. Il punto che distingue la *Enterprise Edge* dal *Service Provider Edge* (solitamente la scatola di giunzione fisica dei cavi) viene detto *punto di demarcazione*.

L'equipaggiamento che si occupa dell'interfaccia con la rete del service provider viene detto **DCE** (*Data Communications Equipment*), mentre l'equipaggiamento interno alla LAN viene detto **DTE** (*Data Terminal Equipment*).

### Servizi WAN
I servizi WAN moderni ricadono nelle seguenti categorie:
- Banda larga **dedicata**: oggi principalmente in fibra, può essere installata indipendentemente da un’organizzazione per collegare direttamente tra loro sedi remote. La _dark fiber_ (cioè fibra installata ma non ancora in utilizzo) può essere noleggiata o acquistata da un fornitore.
- **Commutazione di pacchetto**: le soluzioni offerte qui sono **Metro Ethernet**, che ta sostituendo molte soluzioni WAN tradizionali, e **MPLS**, che Permette ai siti di connettersi al provider indipendentemente dalle tecnologie di accesso utilizzate.
- Banda larga basata su **Internet**: le organizzazioni oggi usano comunemente l’infrastruttura globale di Internet per la connettività WAN. Questo tipo di servizio viene solitamente implementato tramite [[Virtual Private Network]].