Vediamo una prima simulazione di prova in [[Cisco Packet Tracer]] (reperibile [qui](test_0.pkt)). L'obiettivo sarà di creare una piccola [[Local Area Network]], far funzionare un server Web con annesso server DNS, duplicare la rete e collegare le 2 reti ottenute attraverso un [[Router]].

### [[Local Area Network]]
Iniziamo col vedere la prima LAN, costituita da 3 calcolatori (*Terminal 0, 1, e 2*), uno Web server e un server DNS.

![[sottorete_a.png|500]]

Così è come si presenta la rete all'avvio. I pallini arancioni indicano che le porte dello switch sono bloccate in attesa della scoperta di porte attive dal protocollo **STP** (*Spanning Tree Protocol*) in esecuzione sullo [[Switch]]. Dopo alcuni secondi, gli indicatori si trasformano in triangoli verdi, che rappresentano che quel link è in stato *up* (attivo). Di qui in poi lo switch continuerà a mandare pacchetti <span style="display:inline-block;width:24px;height:16px;background:#ff8ee0;border-radius:2px;margin-left: 2px; margin-right:4px"></span> (quindi sempre STP) per mappare la rete, che non arriveranno a nessun altro switch e quindi verranno scartati.

Denominiamo questa sottorete *Sottorete A*, e assegniamogli l'indirizzo IP `111.111.111.0/24`. Questo significa che i primi 24 bit a 1 rappresentano la sottorete, e le 256 combinazioni degli ultimi 8 bit rappresentano i dispositivi della rete (vedere [[Indirizzamento IP]]).
Scegliamo i seguenti indirizzi per i dispositivi sulla Sottorete A:
- **Terminal 0, 1 e 2**: indirizzi a partire da `111.111.111.100` e fino a `111.111.111.102`;
- **Web Server A**: indirizzo `111.111.111.200`;
- **DNS Server A**: indirizzo `111.111.111.2`. Inoltre configuriamo in questo un record di tipo **A** (*Authoritative*): `(servera.com, A record, 111.111.111.200` (che quindi punta al Web server).
Inoltre, configuriamo tutti i dispositivi per puntare al server DNS a `111.111.111.2`.

Possiamo provare alcune funzionalità di rete. Partiamo ad esempio dal *Terminal 1 A*, e cerchiamo di ottenere la pagina `index.html` dal Web server, usando il nome di dominio `servera.com`.
<ol>  
<li>
Innanzitutto avremo bisogno di trasformare il nome di dominio <code>servera.com</code> nell'indirizzo IP del Web server (che noi sappiamo essere <code>111.111.111.200</code>, ma il terminal no). Proviamo quindi a farlo manualmente utilizzando l'utility <code>nslookup</code>:
<pre style="background:black;margin:10px;padding:10px;"><code style="padding:0;"><p style="color:white;margin:0;">Cisco Packet Tracer PC Command Line 1.0
C:\> nslookup servera.com
Server: [111.111.111.2]
Address: 111.111.111.2
Non-authoritative answer:
Name: servera.com
Address: 111.111.111.200</p></code></pre>
Che sembra essere l'indirizzo IP giusto. 
Vediamo cosa succede effettivamente nella simulazione quando lanciamo questo comando:
<ol>
<li>
All'inizio, il Terminal 1 A prepara 2 pacchetti: uno è il pacchetto con la richiesta DNS per l'indirizzo di <code>servera.com</code>, su UDP. L'altro è la richiesta ARP per l'indirizzo MAC del server DNS a <code>111.111.111.2</code>. Questa va fatta in quanto abbiamo fornito solo l'indirizzo IP (dalla configurazione IP), ma non abbiamo ancora a disposizione l'indirizzo di rete a cui inviare il frame con la richiesta DNS (per dettagli, vedere <a href="Indirizzamento IP.md" class="internal-link">Indirizzamento IP</a>). Questo pacchetto viene quindi inviato per primo, all'indirizzo di broadcast Ethernet;
</li>
<li>
Giunto allo switch, il pacchetto viene inoltrato a tutti gli altri nodi della rete. Chiaramente, tutti tranne il destinatario del pacchetto ARP (cioè il server DNS) ignoreranno il pacchetto, mentre quest'ultimo preparerà una risposta ARP e la inoltrerà allo switch;
</li>
<li>
Lo switch potrà quindi riportare la risposta ARP al Terminal 1 A. Notiamo che a questo punto non ha bisogno di inoltrare a tutti i nodi, in quanto la trasmissione da Terminal 1 A a Server DNS è stata registrata, e per le proprietà di <i>self-learning</i> dei router la tabella di forwarding è stata compilata con l'associazione fra la porta del Terminal 1 A (<code>111.111.111.101</code>) e il suo indirizzo Ethernet. Ci riferiamo a questo meccanismo con <i>unicast</i> e <i>multicast</i>. In particolare, possiamo vedere la tabella di forwarding con:
<pre style="background:black;margin:10px;padding:10px;"><code style="padding:0;"><p style="color:white;margin:0;">Switch> show mac address-table
Mac Address Table
-------------------------------------------
Mac  Address         Type     Ports
---- --------------- -------- -------
1    0001.42c2.6106  DYNAMIC  Eth4/1
1    00e0.f9aa.43e2  DYNAMIC  Fa1/1</p></code></pre>
dove <code>Eth4/1</code> è la porta del server DNS e <code>Fa1/1</code> è la porta del Terminal 1 A;
</li>
<li>
Segue lo scambio della richiesta DNS vera e propria, incapsulata su UDP. Come abbiamo detto, la tabella di forwarding è stata ormai compilata per i due nodi interessati, per cui il pacchetto viene inoltrato direttamente al destinatario;
</li>
<li>
Il server DNS riceve la richiesta, consulta la sua tabella di record, ed estrae il record di tipo A che avevamo inserito: <code>(servera.com, A record, 111.111.111.200</code>. Questo viene nuovamente inoltrato allo switch, che lo inoltra direttamente al Terminal 1 A.
</li>
</ol>
Al termine di questa operazione, quindi, abbiamo a disposizione l'indirizzo IP del Web server;
</li>
<li>
Una volta noto l'IP, procediamo a comunicare con il Web server. Prendiamo per adesso di inviare solo un comando <code>ping</code>. Sempre attraverso l'interfaccia a riga di comando del Terminal 1 A, possiamo dire:
<pre style="background:black;margin:10px;padding:10px;"><code style="padding:0;"><p style="color:white;margin:0;">C:\> ping 111.111.111.200
Pinging 111.111.111.200 with 32 bytes of data:
Reply from 111.111.111.200: bytes=32 time=76ms TTL=128
Reply from 111.111.111.200: bytes=32 time=31ms TTL=128
Reply from 111.111.111.200: bytes=32 time=1ms TTL=128
Reply from 111.111.111.200: bytes=32 time<1ms TTL=128
Ping statistics for 111.111.111.200:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 76ms, Average = 27ms

</p></code></pre>
da cui vediamo che siamo riusciti a comunicare. Questa comunicazione si svolge 3 volte per le specifiche di <code>ping</code>, e secondo le stesse modalità dello scambio dei messaggi DNS. Senza perdersi nei dettagli, abbiamo che stavolta alla prima trasmissione lo switch dovrà inoltrare a tutti i nodi, in quanto l'indirizzo Ethernet del Web server non sarà ancora nella tabella di forwarding. Già alla prima risposta del Web server, però, la forwarding table sarà popolata e potremo procedere per instradamenti diretti. 
</li>
<li>
Quello che farà un Web server sarà quindi esattamente il procedimento visto: prima si ottiene l'indirizzo IP attraverso il DNS, cosa che comprende l'uso del protocollo ARP per ottenere l'indirizzo fisico del DNS. Quindi si invierà una richiesta HTTP all'indirizzo IP del server ricevuto, sempre usando ARP per individuarne l'indirizzo fisico. In questo modo, potremo scaricare i dati della pagina <code>index.html</code> e visualizzarla sullo schermo della macchina Terminal 1 A.
</li>
</ol>

### [[Router]]
Introduciamo un router nella simulazione. Prima di tutto, non avrebbe senso avere per una sola sottorete, quindi introduciamo una nuova sottorete:

![[sottorete_b.png|400]]

chiamiamo questa *Sottorete B*. I suoi componenti saranno:
- Un calcolatore, detto **Terminal 1 B**, con indirizzo `222.222.222.100`;
- Uno **Web server**, con indirizzo `222.222.222.200`;
- Un **server DNS**, con indirizzo `222.222.222.2`. Questo sarà caricato con un record di tipo A: `(serverb.com, A record, 222.222.222.200` (che quindi punta al Web server), e con il record già presente nel server DNS della sottorete A. Notiamo che anche il server DNS in quella rete verrà popolato con il record che punta al Web server di questa (Packet Tracer non supporta DNS iterativo o ricorsivo).

All'interno della sottorete B tutto si svolgerà come prima (instradamento *unicast* e *multicast* attraverso lo switch, protocollo ARP, ecc...). Non ripetiamo quindi questi dettagli.
Colleghiamo quindi le due reti attraverso un router:

![[router_ab.png|1000]]

Notiamo che la configurazione di questo non è *plug and play* come lo era stato per gli switch: le 2 porte collegate ad ogni sottorete vanno infatti configurate:
- Innanzitutto bisogna accendere le porte, configurare la maschera di rete e l'indirizzo IP su ogni porta (scegliamo `111.111.111.1` sulla sottorete A e `222.222.222.1` sulla sottorete B). Notiamo la particolarità del router, che ha più di un indirizzo IP, cioè uno per ogni porta;
- Nei dispositivi di ogni rete, bisogna configurare l'indirizzo del rispettivo gateway, cioè della porta del router che si collega alla loro sottorete.
A questo punto il router è pronto ad eseguire i suoi algoritmi di routing (qui banali, si può inoltrare solo da una porta all'altra), senza bisogno di configurare tabelle di routing statiche.

Proviamo quindi un esempio leggermente più complicato del precedente: quello di accedere ad una pagina sul Web server della sottorete B a partire dal Terminal 1 A (situato nella sottorete A).
<ol>
<li>
Come sempre, abbiamo bisogno dell'indirizzo IP del Web server indicato da `serverb.com`. Questo, come abbiamo detto, è già nel DNS della sottorete A, per cui tutta la procedura si svolge esattamente come nello scorso esempio. L'unica differenza è che le tabelle di forwarding dello switch sono già configurate, e quindi tutto si svolge in unicast. Otteniamo quindi il risultato:
<pre style="background:black;margin:10px;padding:10px;"><code style="padding:0;"><p style="color:white;margin:0;">C:\> nslookup serverb.com
Server: [111.111.111.2]
Address: 111.111.111.2
Non-authoritative answer:
Name: serverb.com
Address: 222.222.222.200</p></code></pre>
</li>
<li>
La prima differenza sta nel fatto che l'indirizzo ricevuto (<code>222.222.222.1</code>)  non è nella sottorete locale. Per il Terminal 1 A occorre quindi prendere l'indirizzo del default gateway ed inoltrare i pacchetti a tale indirizzo. Viene da sé che l'indirizzo fisico del gateway (cioè della porta del router rivolta verso la sottorete A) dovrà essere ricavato con ARP. In questo caso sarà il router stesso che eseguirà un lato del protocollo ARP! 
Vediamo quindi di fare un <code>ping</code> dal Terminal 1 A al Web server della sottorete B:
<pre style="background:black;margin:10px;padding:10px;"><code style="padding:0;"><p style="color:white;margin:0;">C:\> ping 222.222.222.200
Pinging 222.222.222.200 with 32 bytes of data:
Reply from 222.222.222.200: bytes=32 time=55ms TTL=127
Reply from 222.222.222.200: bytes=32 time=24ms TTL=127
Reply from 222.222.222.200: bytes=32 time=1ms TTL=127
Reply from 222.222.222.200: bytes=32 time<1ms TTL=127
Ping statistics for 222.222.222.200:
	Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
	Minimum = 0ms, Maximum = 55ms, Average = 20ms</p></code></pre>
Notiamo che questi <code>ping</code> percorrono l'intera rete costruita: partono dal Terminal 1 A, vengono inoltrati attraverso lo switch della sottorete A alla prima porta del router, quindi dal router vengono inoltrati allo switch della sottorete B. Ci si aspetta che al primo pacchetto questa invierà in multicast il pacchetto a tutti i nodi della rete. Quindi imparerà via <i>self-learning</i> l'indirizzo Ethernet del Web server della sottorete B, e potrà instradare pacchetti direttamente ad esso. Per il percorso inverso, tutta la procedura si ripete al contrario;
</li>
<li>
Quello che farà un Web server sarà quindi esattamente il procedimento visto: prima, come nel primo esempio, si ottiene l'indirizzo IP attraverso il DNS. Dell'indirizzo ricevuto si riconosce che appartiene ad una sottorete che non è la nostra. Quindi si invia una richiesta HTTP all'indirizzo IP del gateway, sempre usando ARP per individuarne l'indirizzo fisico. Il gateway, che altro non è che una porta del router, instraderà questa richiesta alla sottorete B, dove quindi verrà ricevuta dal Web server destinatario. In questo modo, potremo scaricare i dati della pagina <code>index.html</code> allocata su una macchina in un altra sottorete e visualizzarla sullo schermo della macchina Terminal 1 A. Tralasciando gli (importantissimi) dettagli del routing e altri protocolli avanzati come DHCP, questo è grossomodo quello che accade costantemente in Internet.
</li>
</ol>
