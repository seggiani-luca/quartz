**Cisco IOS** è un sistema operativo sviluppato per [[Apparati di rete]], in esecuzione sui [[Router]] a marchio Cisco.

Giusto per riassumere, notiamo quanto avevamo già detto riguardo a questi dispositivi:

> [!quote] [[Router]]
> Nello specifico, i router sono i dispositivi che si trovano al confine delle [[Local Area Network]], e che si occupano quindi di connettere più [[Local Area Network]] fra di loro attraverso il cosiddetto processo di *routing*.

I sistemi operativi per router più diffusi sono *Juniper Network Operating System* (**Junos**) della Junyper, e appunto, *Cisco Internetwork Operating System* (**IOS**).

Un sistema operativo per router dovrà assicurare le seguenti funzionalità:
- **Sicurezza** dei pacchetti instradati;
- **Indirizzamento** IP delle interfacce (vedere [[Indirizzamento IP]]);
- Gestione delle **interfacce** su cui i pacchetti effettivamente viaggiano;
- **Routing** vero e proprio dei pacchetti (quindi l'esecuzione degli algoritmi di routing);
- **Quality of Service**: dobbiamo pensare queste macchine come dispositivi ad altissima frequenza che devono gestire migliaia di pacchetti al secondo.
Come tutti i sistemi operativi, poi, un sistema per router dovrà prevedere un livello base di gestione delle **risorse**.

### Accesso all'interfaccia
IOS offre un interfaccia a riga di comando, a cui si può accedere via Telnet, SSH (oggi più diffuso) sulla rete locale, attraverso una porta *console* dedicata, e attraverso alcune modalità legacy (come da *modem*).

![[router_cons.png|500]]

Solitamente le interfacce legacy e sopratutto la porta dedicata alla console vengono usate in caso di *disaster recovery*, cioè situazioni dove il sistema ha fallito, non si può più accedere alla rete, e si deve provvedere al riavvio dell'apparato (o eventuale troubleshooting) interagendo direttamente con la riga di comando attraverso la porta dedicata.

L'interfaccia a riga di comando di **IOS** è *modale*: esiste una gerarchia dei comandi disponibili che si articola attraverso categorie di comandi. Questo permette di avere distinzione semantica fra le categorie di comandi, e di spostarsi fra di esse come ci si sposterebbe in un *filesystem* di un sistema operativo *general purpose*, o in un menù modale di qualsiasi altro dispositivo:

![[cmds.png|800]]

Ad esempio, vediamo di avere due categorie top-level:
- *User EXEC*: i comandi che si possono eseguire senza autenticarsi. Questi sono ad esempio `ping`, `show` per l'informazione sulle interfacce, `enable` per accedere alla modalità privilegiata, ecc...
- *Privileged EXEC*: i comandi che si possono eseguire autenticandosi. Qui ad esempio abbiamo le impostazioni per *configurare* il router, le interfacce, ecc...
Il *prompt* della riga di comando riflette in ogni momento la categoria di comandi all'interno di cui ci troviamo. Ad esempio:
```
Router (config-if)#
```
significa che siamo in modalità *privilegiata* (simbolo `#` contro simbolo `>`), di configurazione (`config`) delle interfacce (`if`).

Vediamo quindi quali sono i comandi più importanti di IOS.
#### Comando `show`
Questo comando permette di ottenere informazioni riguardo a tutta una serie di caratteristiche e parametri del router. In particolare si ha:
- `show interfaces` – Mostra le statistiche per tutte le interfacce del dispositivo.
- `show version` – Mostra informazioni sulla versione del software attualmente caricata, insieme alle informazioni hardware e del dispositivo.
- `show arp` – Mostra la tabella ARP del dispositivo.
- `show startup-config` – Mostra la configurazione salvata presente nella NVRAM.
- `show running-config` – Mostra il contenuto del file di configurazione attualmente in esecuzione oppure la configurazione di una specifica interfaccia o le informazioni della map class.
- `show ip interface` – Mostra le statistiche IPv4 per tutte le interfacce di un router. Per visualizzare le statistiche di una specifica interfaccia, usare il comando `show ip interfaces` seguito dal numero di slot/porta dell’interfaccia specifica.
- `show ip interface brief` – Variante del comando precedente utile per ottenere rapidamente un riepilogo delle interfacce e del loro stato operativo.
