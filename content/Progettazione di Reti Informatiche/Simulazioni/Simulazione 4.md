Usiamo questa simulazione per studiare un "*bug*" che possiamo incontrare nel caso di router configurati in maniera erronea in un'insieme di sottoreti. 
Vediamo innanzitutto la rete:

![[badspray.png|800]]

### Configurazione della rete
Vediamo che la rete è formata da 3 sottoreti:
- La sottorete 0 (gateway Router0), con indirizzo `111.111.111.0/24`;
- La sottorete 1 (gateway Router1), con indirizzo `112.112.112.0/24`;
- La sottorete 2 (gateway Router2), con indirizzo `113.113.113.0/24`;
Ogni sottorete è formata da un singolo terminal (PC0, PC1 e PC2 rispettivamente) collegato direttamente al gateway attraverso un cavo di crossover. 
Le sottoreti fra i router sono quindi così disposte:
- Fra Router0 e Router1 sta la sottorete `221.221.221.0/24`;
- Fra Router1 e Router2 sta la sottorete `222.222.222.0/24`;
- Fra Router2 e Router0 sta la sottorete `223.223.223.0/24`;

Notiamo che, come nella scorsa simulazione, non usiamo collegamenti *Gigabit Ethernet* fra i router, ma porte seriali legacy.
Non configuriamo nemmeno nessuna linea o nessuna password dei router, in quanto facciamo tutta la configurazione direttamente dai loro terminali (offerti da [[Cisco Packet Tracer]]).

### Il "bug"
Il vivo della simulazione si incontra in fase di configurazione delle [[Tabella di routing]]. Abbiamo visto ampiamente il meccanismo della configurazione di tali tabelle in [[Cisco IOS]] (con il comando `ip route` nel contesto `config`), quindi passiamo ad una trattazione di livello logico. 
Per il nostro esempio, quindi, configuriamo i router come segue:

1. Configuriamo il Router0 perchè possa accedere alle sottoreti `113.113.113.0/24` e `112.112.112.0/24` nella maniera più naturale (cioè attraverso Router1 e Router2):
```
# configurazione route Router0

111.0.0.0/24 is subnetted, 1 subnets
C 111.111.111.0 is directly connected, FastEthernet2/0

112.0.0.0/24 is subnetted, 1 subnets
S 112.112.112.0 [1/0] via 221.221.221.2

113.0.0.0/24 is subnetted, 1 subnets
S 113.113.113.0 [1/0] via 223.223.223.1

C 221.221.221.0/24 is directly connected, Serial0/0
C 223.223.223.0/24 is directly connected, Serial1/0
```

2. Configuriamo il Router2 in maniera "stupida", cioè impediamogli di accedere ad alcuna delle altri sottoreti, semplicemente non fornendogli le route statiche di cui ha bisogno per rintracciarle (fare il next hop dei pacchetti diretti ad esse). Seguirà che le sue route sono solo quelle direttamente connesse:
```
# configurazione route Router1

113.0.0.0/24 is subnetted, 1 subnets
C 113.113.113.0 is directly connected, FastEthernet2/0

C 222.222.222.0/24 is directly connected, Serial1/0
C 223.223.223.0/24 is directly connected, Serial0/0
```

3. Infine, configuriamo il Router3 per fornire in maniera intenzionale 2 possibili route per la sottorete `111.111.111.0/24` (quella servita dal Router0). Le route saranno chiaramente attraverso il Router0 stesso, che è il modo più naturale (sulla sottorete `221.221.221.0/24`), e il percorso "lungo" attraverso il Router2 (sulla sottorete `222.222.222.0/24`). La tabella di routing avrà quindi il seguente aspetto, da dove si nota la doppia via per `111.111.111.0/24`:
```
111.0.0.0/24 is subnetted, 1 subnets
S 111.111.111.0 [1/0] via 221.221.221.1
                [1/0] via 222.222.222.2

112.0.0.0/24 is subnetted, 1 subnets
C 112.112.112.0 is directly connected, FastEthernet2/0

113.0.0.0/24 is subnetted, 1 subnets
S 113.113.113.0 [1/0] via 222.222.222.2

C 221.221.221.0/24 is directly connected, Serial1/0
C 222.222.222.0/24 is directly connected, Serial0/0
```

Quello che accade in questo caso è che di default i router sono configurati per supportare ed abilitare l'**ECMP** (*Equal-Cost Multi-Path*). Questa è una funzionalità che porta ad avere *spraying* dei pacchetti nel caso di più route equivalenti alla stessa destinazione, in una sorta di load balancing integrato nel router.

Di default, questo approccio è pensato per non riordinare i pacchetti, cioè mantenere le route costanti per i flussi che individua (per individuare i flussi ci si basa su una funzione hash calcolata a partire dai campi IP e porta sorgente e destinatario del pacchetto). 

Possiamo "abusare" di questa funzionalità inviando pacchetti **ICMP** (*Internet Control Message Protocol*), come quelli di ping. Questo perché in [[Cisco Packet Tracer]], e probabilmente in qualche applicazione reale, ogni pacchetto ICMP viene considerato come appartenente ad un flusso separato. Il risultato è che facendo, ad esempio, un ping dal PC0 al PC1, si ha la seguente situazione:
1. Il PC0 invia un pacchetto ICMP di ping al PC1: questo passa attraverso al suo gateway, cioè il Router0 (ben configurato), sulla sottorete `221.221.221.0/24`, e arriva al Router1, che lo inoltra al PC1;
2. Il PC1 riceve il pacchetto ICMP di ping, e risponde con un ping echo che viene inoltrato al suo gateway, cioè il Router1. Questo dovrà decidere quale route usare per tornare al PC0: avrà a disposizione, come abbiamo detto, sia il percorso per il Router0 (su `221.221.221.0/24`) che per il Router2 (su `222.222.222.0/24`). Diciamo che in prima istanza sceglie il percorso sul Router0: questo è ben configurato e quindi inoltra correttamente la risposta al PC0;
3. Un altro pacchetto ICMP di ping viene spedito dal PC0 al PC1, seguendo ancora lo stesso percorso (unico configurato in questo senso): Router0, sottorete `221.221.221.0/24`, Router1;
4. Nuovamente il PC1 riceve il pacchetto ICMP di ping, e risponde con un ping echo che viene inoltrato al Router1. In questo caso, visto che alla scorsa iterazione ha scelto il percorso per il Router0, il Router1  sceglierà il percorso per il Router2 per tornare al PC0;
5. Qui avviene l'inghippo: il Router2 non ha veramente un modo per arrivare al PC0, quindi il pacchetto di risposta viene perso nella rete. Tra l'altro, nessuno ha veramente modo di segnalare questo al PC0, o almeno al PC1, in quanto il Router1 ha inviato nella buona fede di una route statica, e il Router2 non ha modo di rispondere (la sua [[Tabella di routing]] non è configurata per raggiungere il PC1, al massimo potrebbe farlo attraverso il Router1).
Quello che accade, nel complesso, è quindi che un ping ha successo e l'altro no, in un ambiente simulato come [[Cisco Packet Tracer]] in maniera completamente alternativa. Possiamo verificare che questo è il caso analizzando l'output di ping eseguito dal PC0 come appena detto:

```
C:\>ping 112.112.112.2

Pinging 112.112.112.2 with 32 bytes of data:
Reply from 112.112.112.2: bytes=32 time=55ms TTL=126
Request timed out.
Reply from 112.112.112.2: bytes=32 time=40ms TTL=126
Request timed out.

Ping statistics for 112.112.112.2:
	Packets: Sent = 4, Received = 2, Lost = 2 (50% loss),
Approximate round trip times in milli-seconds:
	Minimum = 40ms, Maximum = 55ms, Average = 47ms
```

Abbiamo quindi visto una circostanza in cui una configurazione sbagliata di un router sulla rete causa il comportamento scorretto dell'intera rete. In particolare, vediamo come anche se il nostro router di gateway è ben configurato, e lo è anche quello della nostra destinazione, potremmo comunque avere problemi di comunicazione nel caso di route invalide.