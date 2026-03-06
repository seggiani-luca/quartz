L'organizzazione delle [[Reti informatiche]] viene classificata dal modello **OSI**, che mira ad un organizzazione gerarchica basata sul modello dei *servizi* offerti da ogni livello al livello superiore. Il modello OSI prevede **7 livelli**:  
- **Application**  
Livello a cui operano le applicazioni vere e proprie utilizzate dagli utenti.  
- **Presentation**  
Livello introdotto per trasformare i dati in ingresso in un formato comprensibile alle macchine degli utenti (gestione di particolarità come *byte ordering*, encoding, ecc.).  
- **Session**  
Livello introdotto per gestire le sessioni degli utenti.  
- **Transport**  
Garantisce l’affidabilità ad alto livello dell’informazione e la corretta trasmissione dei dati anche attraverso diversi *hop*.  
- **Network**  
Permette l’interconnessione di reti diverse attraverso un formato comune di indirizzamento e instradamento.  
- **Datalink**  
Costruito sopra il livello **Physical**. Si occupa del trasferimento dei dati tra nodi direttamente collegati e introduce, in alcuni casi, meccanismi di controllo degli errori.  
- **Physical**  
Riguarda il mezzo fisico vero e proprio e la trasmissione dei bit sul canale.

Solitamente i primi 3 livelli (*Application*, *Presentation* e *Session*) vengono omologati al livello *Application*, in quanto:
- La distinzione non è particolarmente significativa;
- La maggior parte dei sistemi reali implementa tali funzionalità allo stesso livello in ogni caso.