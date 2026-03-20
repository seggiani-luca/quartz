In una rete il **routing** viene effettuato dai [[Router]] in 3 modi principali:
- Routing tradizionale (destination based routing), per solo indirizzo di *destinazione*. Sarebbe l'approccio usato di default da IP;
- Routing attraverso etichette (label swapping, ad esempio usato nel protocollo **MPLS** (*Multi Protocol Label Switching*)), che vengono cambiate fra un hop e un altro. Questo ci permette di usare un meccanismo simile alla commutazione di circuito, anche nelle reti a pacchetto;
- Routing da *sorgente*, dove l'intera sequenza degli hop che un pacchetto deve fare è già scritta nel pacchetto, così com'è stato inviato da sorgente. Questo sarebbe supportato anche da IP, ma sostanzialmente oggi si usano protocolli sofisticati e proprietari (sopratutto in contesti aziendali).

Abbiamo già detto che il compito di base di un router è quello di:
- Prendere un pacchetto da una *porta di ingresso*;
- Ricavarne l'indirizzo di destinazione;
- Consultare un'apposita tabella di *routing* (o tabella di *forwarding*, che non necessariamente è la stessa cosa) in modo da ricavare la *porta di uscita* del pacchetto;
- Inoltrare il pacchetto su tale porta.
Abbiamo quindi che l'associazione dell'indirizzo destinazione è fatta solamente sulla porta di uscita, cioè al next hop adiacente al router che elabora il pacchetto. Inoltre notiamo che i router usano un approccio *longest prefix* alla selezione della porta di uscita, cioè selezionano quella più specifica per l'indirizzo di destinazione.

### Router Cisco
Nei router Cisco (quindi con sistema operativo [[Cisco IOS]]) la tabella di routing può essere visualizzata com il comando `show ip route`. Un risultato di esempio di questo comando è il seguente:

```
RE#show ip route
Codes: C - connected, S - static, I - IGRP, R - RIP, M - mobile, B - BGP
D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
E1 - OSPF external type 1, E2 - OSPF external type 2, E - EGP
i - IS-IS, L1 - IS-IS level-1, L2 - IS-IS level-2, ia - IS-IS inter area
* - candidate default, U - per-user static route, o - ODR
P - periodic downloaded static route
Gateway of last resort is not set
R 192.168.0.0/24 [120/2] via 192.168.66.1, 00:00:03, Serial0/0/1
R 192.168.3.0/24 [120/1] via 192.168.68.1, 00:00:02, Serial0/1/0
C 192.168.4.0/24 is directly connected, FastEthernet0/0
R 192.168.5.0/24 [120/1] via 192.168.70.2, 00:00:03, Serial0/0/0
R 192.168.64.0/24 [120/1] via 192.168.66.1, 00:00:03, Serial0/0/1
R 192.168.65.0/24 [120/2] via 192.168.68.1, 00:00:02, Serial0/1/0
[120/2] via 192.168.66.1, 00:00:03, Serial0/0/1
C 192.168.66.0/24 is directly connected, Serial0/0/1
R 192.168.67.0/24 [120/1] via 192.168.68.1, 00:00:02, Serial0/1/0
C 192.168.68.0/24 is directly connected, Serial0/1/0
R 192.168.69.0/24 [120/1] via 192.168.70.2, 00:00:03, Serial0/0/0
[120/1] via 192.168.68.1, 00:00:02, Serial0/1/0
C 192.168.70.0/24 is directly connected, Serial0/0/0
```

Notiamo quindi che abbiamo diverse entrate, di tipi diversi indicate dalle lettere (di cui la legenda che viene stampata per prima):
- C - connesso;
- S - statico;
- I - IGRP;
- R - RIP;
- M - mobile;
- B - BGP;
- D - EIGRP;
- EX - EIGRP esterno;
- O - OSPF;
- IA - OSPF inter-area;
- N1 - OSPF NSSA esterno tipo 1;
- N2 - OSPF NSSA esterno tipo 2;
- E1 - OSPF esterno tipo 1;
- E2 - OSPF esterno tipo 2;
- E - EGP;
- i - IS-IS;
- L1 - IS-IS livello 1;
- L2 - IS-IS livello 2;
- ia - IS-IS inter-area;
- * - candidata per default;
- U - percorso statico per utente;
- o - ODR;
- P - percorso statico scaricato periodicamente.
In questo semplice esempio è tutto **R** (collegato attraverso protocollo RIP), o **C** (collegato direttamente). Per ogni entrata della tabella seguono quindi:
- L'indirizzo della sottorete di destinazione su cui fare matching;
- Le [[Metriche di routing]] associate al percorso. In particolare, prendendo ad esempio il percorso:
  `R 192.168.0.0/24 [120/2] via 192.168.66.1, 00:00:03, Serial0/0/1`
  si ha che `120` è la *distanza amministrativa* del percorso, cioè la preferenza specificata di default dal router a quel tipo di percorso, mentre `2` è la metrica RIP (il numero di hop). 
- L'indirizzo del router di *next hop*, cioè il prossimo a cui instradare il pacchetto;
- La porta attraverso la quale si può raggiungere tale router. Questa sarà quella effettivamente utile al forwarding.
Notiamo inoltre che le entrate della tabella di routing hanno solitamente un **TTL** (*Time To Live*) dopo il quale vengono invalidate.