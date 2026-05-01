Per la configurazione del protocollo e l'algoritmo [[Open Shortest Path First]] nei router Cisco con [[Cisco IOS]] in esecuzione, si hanno a disposizione una serie di utility `ospf`. 

Inizialmente, per avviare il processo `ospf` si usa il comando, da ambiente di configurazione:
```
Router(config)#router ospf <process-id>
```
dove il `<process-id>` è l'indice che assegniamo al processo che stiamo per mandare in esecuzione.

Dopo aver aperto il processo `ospf` dovremmo assegnare un router ID al nostro router (che notiamo non è a priori legato all'indirizzo IP). Di base l'ordine in cui vengono controllate le sorgenti per il router ID è:
- L'indirizzo configurato col comando `router-id`;
- Il più alto fra gli indirizzi delle sue interfacce di loopback. Qui conviene fare un approfondimento su cosa è di preciso l'interfaccia di loopback.
  Nel protocollo IP un blocco di indirizzi viene allocato alle cosiddette *interfacce di loopback*, che sono interfacce virtuali gestite interamente all'interno di un singolo dispositivo. I pacchetti inviati dal dispositivo all'interfaccia di loopback vengono gestiti dallo stack di rete fino al dispatch, quindi immaginati come ricevuti dal dispositivo, e quindi gestiti nuovamente dallo stack di rete fino a tornare al livello application.
  Talvolta nei router conviene creare interfacce virtuali con indirizzi non di loopback. Condividere gli indirizzi di tali interfacce attraverso protocolli come OSPF permette ai router di pubblicizzare un indirizzo costante, non dipendente dalle interfacce (ricordiamo che un [[Router]] ha un indirizzo per interfaccia).
- Il più alto fra gli indirizzi delle sue interfacce fisiche in stato `up`.

L'uso di OSPF viene fatto dal router selettivamente sulle interfacce, sulla base della configurazione data. Per questo è predisposto il comando `network`:
```
Router(config-router)#network <network-address> <wildcard-mask> area <area-id>
```
Questo comando determina quali interfacce, per area, partecipano al processo di routing OSPF. Ogni interfaccia che ha un indirizzo corrispondente a `network-address` contribuirà al protocollo OSPF inviando e ricevendo pacchetti OSPF, e la rete specificata parteciperà agli aggiornamenti di routing OSPF.

La maschera `wildcard-mask` è il complemento a 1 della maschera di rete dell'indirizzo fornito. Si usa la `wildcard-mask` anziché la comune `subnet-mask` in quanto i primi bit della maschera potrebbero essere alternativamente a 1.

Esistono effettivamente più modalità di questo comando:
- **Interfaccia singola**: usando una wildcard mask tutta a 0 (`0.0.0.0`) si può configurare una singola interfaccia come appartenente all'area. Questo è il modo più specifico e permette in ogni caso di configurare tutte le interfacce del router, al costo di essere più dispendioso in tempo e comandi da battere a tastiera;
- **Interfaccia multipla**: specificando una wildcard vera e propria (che è la modalità d'uso prevista effettivamente) si può assegnare un *insieme* di interfacce, anziché una singola interfaccia, ad un area. Questo è utile nel caso in cui si allochino gli indirizzi delle interfacce in maniera tale da riflettere le aree OSPF che si vogliono creare (cosa che non è sempre vera), in quanto in tal caso diminuisce il tempo di configurazione (si riesce a fare tutto con meno comandi);
- **Tutte le interfacce**: il caso estremo (e pericoloso) dell'ultimo esempio è quello di assegnare la wildcard mask `255.255.255.255`, e quindi indicare tutte le interfacce connesse al router come parte di un'area OSPF. Questo è però generalmente sconsigliato.

### Interfacce passive
C'è un primo problema di *sicurezza* che possiamo avere se configuriamo i nostri router per usare OSPF. Visto che un router con OSPF in esecuzione condivide periodicamente sulle interfacce appartenenti ad una certa area le LSA (vedere [[Pacchetto OSPF]]), un malintenzionato potrebbe collegarsi da una LAN ad un router di bordo fingendosi un router (magari il router della LAN stesso) e ottenere il database delle LSA (che contiene informazioni rilevanti su tutta la topologia di rete).

Per risolvere questo problema si può configurare un interfaccia come appartenente ad OSPF ma non destinata a ricevere le LSA, attraverso il comando di configurazione OSPF `passive-interface <interface>`. Questo prende in argomento un interfaccia vera e propria (non l'indirizzo) e la mantiene parte dell'area in cui è stata configurata, senza però condividere con essa le LSA.

Abbiamo quindi uno workflow di configurazione delle interfacce forse poco intuitivo:
1. Prima si configurano tutte le interfacce appartenenti ad un'area, assumendole inizialmente tutte come attive (ricevono LSA);
2. Solo in un secondo momento si configurano le interfacce passive, cioè quelle appartenenti ai router di bordo che escono dalla rete, e dalla quale non dobbiamo propagare le LSA.

### Configurazione dei costi
Cisco IOS utilizza la larghezza di banda dell’interfaccia per calcolare il costo OSPF, come
$$
\text{costo} = \frac{\text{banda di riferimento}}{\text{banda di interfaccia}}
$$
dove la *banda di riferimento* `reference-bandwidth` può essere configurata con un comando di configurazione (di default è 100 Mbps):
```
auto-cost reference-bandwidth <reference-bandwidth>
```

Per ogni interfaccia dobbiamo quindi configurare la larghezza di banda per interfaccia. Ci sono dei valori di default che danno la seguente configurazione:

| Tipo Interfaccia    | Formula (100 / bandwidth Mbps) | Costo |
| ------------------- | ------------------------------ | ----- |
| 10 Gigabit Ethernet | 100 / 10000                    | 1     |
| Gigabit Ethernet    | 100 / 1000                     | 1     |
| Fast Ethernet       | 100 / 100                      | 1     |
| Ethernet            | 100 / 10                       | 10    |
| E1                  | 100 / 2.048                    | 48    |
| T1                  | 100 / 1.544                    | 64    |
| 128 kbps            | 100 / 0.128                    | 781   |
| 64 kbps             | 100 / 0.064                    | 1562  |
Per link dove la larghezza di banda non corrisponde a quella di default, si può accedere alla modalità di configurazione interfaccia e usare il comando di configurazione `bandiwidth`:
```
R1#conf t
Enter configuration commands, one per line. End with CNTL/Z.
R1(config)#int se0/0/0
R1(config-if)#bandwidth 2000 # imposta la larghezza di banda a 2000 Kbit
```

Se ci si volesse risparmiare questa configurazione manuale delle interfacce (per poi variare il rapporto fra bandwidth di riferimento e di interfaccia) si possono configurare direttamente i costi OSPF per interfaccia (*configurazione amministrativa*):
```
R2(config)#int se0/0/0
R2(config-if)#ip ospf cost 50
```

### Configurazione degli ABR
Vogliamo che gli **ABR** (*Area Boundary Router*) pubblicizzino la route di default (e.g. verso internet) agli altri router OSPF. Questo combacia con la classica configurazione aziendale dove c'è un singolo punto di collegamento al router dell'ISP.

Per attivare questa funzionalità esiste il comando `default-route originate`, che può essere forzato con `default-route originate always`, che porta il router a pubblicizzare agli altri router OSPF la sua route di default.

### Elezione di DR e BDR
DR e BDR vengono secondo un elezione dove il criterio di spareggio è:
- Il **DR** è il router con la *più alta* priorità OSPF di router;
- Il **BDR** è il router con la *seconda più alta* priorità OSPF di router.
La priorità OSPF di router può essere modificata da ambiente di configurazione:
```
Router(config-if)#ip ospf priority {0 - 255}
```

Se le priorità OSPF sono uguali, il secondo criterio di spareggio considerato è il router ID: il router con il router ID più alto ottiene il posto.

Notiamo che l'elezione comincia potenzialmente prima che la configurazione di rete sia terminata: questo significa che possiamo avere una situazione dove un router con router ID (o priorità OSPF) più bassa viene configurato prima e diventa DR. In tal caso, il DR corrente rimane finché non fallisce.