Un [[Router]] o uno [[Switch]] con [[Cisco IOS]] può comportarsi come un **firewall** (in particolare, come un *packet filter*) attraverso il meccanismo delle **ACL** (*Access Control List*).
Un’ACL (Access Control List) è definita da un elenco ordinato di regole, che vengono controllate sequenzialmente alla ricerca di un pattern corrispondente.
- Una sola ACL può essere configurata per protocollo, per direzione e per interfaccia;
- Viene configurata su router firewall, router di confine o router intermedi tra due aree separate della rete per limitare e controllare il traffico, e offrire sicurezza.

La scansione delle ACL viene fatta per l'interfaccia di ingresso, e per quella di uscita, per ogni pacchetto. Per il pacchetto si controlla ogni regola della ACL sequenzialmente. Le regole sono di tipo *deny* (blocca il pacchetto) o *permit* (lascia passare). I pacchetti che non soddisfano nessuna regola vengono implicitamente bloccati.
 
![[acl.png]]

### Tipologie di ACL
Esistono 2 tipologie di ACL:
- ACL **standard**: esistono solo al livello 3, e fanno filtraggio di pacchetti sulla base dell'indirizzo IP sorgente;
  ACL **estese**: permettono di fare packet filtering su altri parametri, come ad esempio il protocollo usato (TCP/UDP) e i numeri di porta livello 4.

### Configurazione delle ACL
Visto che il pattern matching delle regole viene fatto in maniera sequenziale, anche la configurazione va fatta in maniera sequenziale. La sintassi di base per l'introduzione di una regola è:
```
Router(config)#access-list 130 {permit | deny} <options>
```
dove le opzioni specificano i parametri (standard o estesi) della regola.

Quindi, per applicare l'ACL ad un interfaccia, si può usare la seguente sintassi, nel'ambiente di configurazione di un'interfaccia:
```
Router(config-if)#ip access-group {access-list-number | access-list-name} {in |
out}
```
Le ACL possono anche essere applicate alle linee, con la sintassi:
```
Router(config-line)#access-class {access-list-number | access-list-name} {in |
out}
```

Notiamo che ci si può riferire ad una ACL per numero, o per nome, usando la sintassi:
```
ip access-list standard <name>
# configurazione della ACL
```
dove notiamo si specifica anche il tipo della ACL (`standard` o `extended`). Se si specifica un'ACL per numero, bisogna inserire le regole sequenzialmente e rimuovere l'intera lista in caso di errori. Se si usa un'ACL con nome, si ha invece accesso ad una modalità di configurazione specifica per le ACL, dove si può anteporre un  *numero di sequenza* alle regole.