Vediamo il dettaglio di come è formato un pacchetto [[Open Shortest Path First]]. Abbiamo che innanzitutto questo è organizzato come segue:

![[ospf_packet.png]]

Si incapsula quindi il pacchetto OSPF vero e proprio in un pacchetto IP. Notiamo che non si sfrutta alcun protocollo di trasporto, ma si incapsula direttamente il pacchetto OSPF con numero di protocollo *#89* (questo lo differenzia da altri protocolli di scambio fra router, come ad esempio RIP che usa UDP, e BGP che usa TCP). L'header specifico al pacchetto OSPF segue quello IP, e ha il seguente aspetto:

![[ospf_header.png]]

Questo header contiene i seguenti valori:
- La *versione* di OSPF usata;
- Il *tipo* di pacchetto, che approfondiremo a breve;
- La *lunghezza* del pacchetto;
- Informazioni sugli *ID* di router e area a cui appartiene, per maggiori dettagli vedere [[Open Shortest Path First#AS]];
- Infine, il *checksum* e informazioni di *autenticazione* per questioni di sicurezza.

### Tipi di pacchetto
Vediamo quali sono i tipi di pacchetto che possiamo incontrare in OSPF. Si ha innanzitutto il pacchetto di *Hello*, che viene scambiato fra router vicini (non necessariamente adiacenti nella rete overlay OSPF), solo per notificare i router di una sottorete dell'esistenza l'uno dell'altro:
- **Pacchetto Hello (tipo 1)**: fornisce un meccanismo per la scoperta dinamica dei vicini, e supporta l’elezione del Router Designato (DR) e del Backup Designato (BDR) su un segmento LAN. 
  
  ![[ospf_hello.png]]
  
  Un pacchetto di Hello contiene quindi tutte le informazioni necessarie a stabilire un *vicinanza* OSPF. Nel caso i parametri dei pacchetti Hello corrispondano, dopo uno scambio a 3 vie, la vicinanza può essere costruita. L'intervallo *Hello Interval* rappresenta la frequenza con cui si invia il pacchetto di Hello ai vicini (solitamente ogni 10 secondi, continuamente anche dopo la fase di avvio), mentre il *Router Dead Interval* rappresenta il tempo massimo che si aspetta un router che non risponde agli Hello prima di dichiararlo come down. Notiamo inoltre che in un pacchetto di Hello si notano il router designato come centrale di quell'area, il suo backup, e la lista delle altre vicinanze scoperte;
Come abbiamo detto in [[Open Shortest Path First#Operazione di OSPF]], dopo il pacchetto di Hello, la fase di scambio bidirezionale, e la sincronizzazione dei database, due router che rispettano determinati requisiti possono diventare *adiacenti*. Questa adiacenza viene registrata in un apposito *database delle adiacenze*. Inoltre, ogni router (compresi DR e BDR) ha un database di livello [[Link State]] che contiene l'informazione di routing. Per aggiornare tale database ci sono i pacchetti di **LSA** (*Link State Advertisement*), scambiati fra router effettivamente adiacenti a livello OSPF (o da questi agli altri router), che servono a rappresentare l'informazione di routing vera e propria:
- **Pacchetto di Descrizione del Database (tipo 2)**: tutti i router nella stessa area condividono lo stesso database di stato dei link, per cui questo pacchetto è quello che consente una sincronizzazione rapida tra router adiacenti senza attendere il flooding dei **LSA** (*Link State Advertisement*);
- **Pacchetto di Richiesta dello Stato dei Link (tipo 3)**: viene inviato per richiedere uno specifico insieme di LSA a un router adiacente;
- **Pacchetto di Aggiornamento dello Stato dei Link (tipo 4)**: viene inviato in risposta a una richiesta oppure per implementare il flooding delle LSA. Ogni pacchetto di aggiornamento di livello [[Link State]] contiene più LSA:
  
  ![[ospf_update.png]]
  
  Un pacchetto di aggiornamento di questo tipo può essere generato da un router casuale che ne è l'origine, ad esempio per notificare un cambio di topologia, rispondere ad una richiesta, o semplicemente ogni 30 minuti per confermare la stessa informazione che è già nella rete. Può anche essere trasmesso da un router che non sarà la sorgente, e in questo caso sarà un router DR o BDR, per effettuare il flooding delle LSA.

  Ogni LSA è preceduta da un rispettivo header, che contiene informazioni di *identificazione* della LSA e dell'originatore, un *numero di sequenza* che permetta il *selective flooding* (vedere [[Link State]]), e informazioni di *aging* per rimuovere le vecchie LSA dalla circolazione.
  
  ![[ospf_lsa_header.png]]
  
  La *link state age* implementa quindi il meccanismo di aging che permette aggiornamenti rapidi della topologia (rimuovendo vecchia informazione). Un LSA è identificata univocamente da *LS type*, *LS ID* e *advertising router* (il router originatore). L'istanza più recente di una LSA, invece (per il selective flooding) si individua guardando al *sequence number* e alla *LS age*. Le tipologie di LSA sono indicate dal LS type e sono variegate:
  1. **Router-LSA**: generata da ogni router nell'area, resta all'interno di tale area e descrive connessioni point-to-point con altri router, connessioni a transit network, a stub network, o link virtuali;
  2. **Network-LSA**: generata dai DR, resta all'interno dell area da cui origina e contiene informazioni riguardo ai router connessi al DR che rappresenta la rete;
  3. **Summary-LSA**: generata dall'**ABR** (*Area Boundary Router*), cioè il router di confine dell'area (per noi AS) OSPF, descrive le route verso altre aree alle reti. Queste route possono anche essere soggette a [[Route summarization]];
  4. **ASBR-LSA**: generata dall'ABR, indica ai router nelle aree come raggiungere l'**ASBR** (*Autonomous System Boundary Router*). Non trasporta reti, ma la raggiungibilità del router che redistribuisce rotte esterne;
  5. **AS-external-LSA**: generata dall'**ASBR** (*Autonomous System Boundary Router*), descrive route pubblicizzare dall'ASBR stesso e ottenute attraverso altri protocolli (ad esempio BGP) che vanno inoltrati in OSPF. Viene diffusa per flooding in tutto l'AS oltre le aree;
  6. **MOSPF-group-LSA**: oggi obsoleta, usata in passato per **MOSPF** (*Multicast Open Shortest Path First*);
  7. **NSSA-external-LSA**: generata dall'ASBR, porta le route di tipo 5 all'interno degli **NSSA** (*Not So Stubby Area*);
  8. **Link-LSA**:  generata da ogni router coinvolto in un link, fornisce l'indirizzo locale al link del router ad ogni altro router sulla rete;
  9. **Intra-Area-Prefix-LSA**: rimpiazza alcuna della funzionalità delle LS di tipo 1 (Router-LSA).

- **Pacchetto di Acknowledgement dello Stato dei Link (tipo 5)**: utilizzato per rendere affidabile il flooding delle LSA. Ogni LSA ricevuta da un router da un vicino deve essere esplicitamente confermata attraverso un pacchetto di ACK di questo tipo.
