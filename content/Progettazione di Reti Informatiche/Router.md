Un **router** è un dispositivo di livello *network* (vedere [[Modello OSI]]) che si occupa dell'instradamento di pacchetti IP. In particolare è:
- Dispositivo di livello 3 (rete) del modello OSI;
- Collega reti diverse e instrada i pacchetti IP tra di esse;
- Usa tabelle di routing e protocolli (es. statico, dinamico);
- Può fare **NAT**, **DHCP**, e firewall di base (vedere [[Indirizzamento IP]]);
- Tipicamente collega le [[Local Area Network]] a Internet ([[Wide Area Network]]).

Nello specifico, i router sono i dispositivi che si trovano al confine delle [[Local Area Network]], e che si occupano quindi di connettere più [[Local Area Network]] fra di loro attraverso il cosiddetto processo di *routing*. I collegamenti che collegano i singoli router rispettano diversi protocolli, e sono di tipo *punto-punto*.

Abbiamo che i router sono a tutti gli effetti computer estremamente specializzati (specializzati ad inviare pacchetti sulla rete). Il loro compito, come anticipato dal corso di reti informatiche, è duplice:
- A livello **data plane**, quello di effettuare il *forwarding* dei pacchetti (ottenuti dalle porte di entrata) verso le loro destinazioni attraverso le porte di uscita;
- A livello **control plane**, eseguire un *algoritmo di routing* e quindi selezionare il percorso migliore per i pacchetti. Ricordiamo che il *control plane* può essere implementato in 2 modi: il metodo tradizionale è quello di implementare algoritmi di routing *distribuiti* (ad esempio **OSPF**, *Open Shortest Path First*, **RIP**, *Routing Information Protocol*, **BGP**, *Border Gateway Protocol*, ecc...); il secondo metodo è quello del cosiddetto **SDN** (*Software Defined Networking*), che si basa sull'esistenza di un sistema centralizzato di gestione delle tabelle di routing per tutti i router di un *autonomous system*.

Come tutti i computer, quindi, i router sono dotati di memoria (in particolare, RAM, NVRAM di configurazione, e memoria flash di configurazione), CPU, e loro particolarità, un sistema di I/O estremamente specializzato (ed estremamente veloce) composto dalle porte di ingresso e uscita (solitamente di tipo [[Ethernet]]) su cui viaggiano i pacchetti (a tal proposito, [[Interfacce e porte]]).  Vediamo ad esempio il *backplane* di un router Cisco serie 1800 per vedere il tipo di interfacce di cui ha bisogno:
![[router_backs.png|400]]

Su un router, per abilitare la sua operazione, è solitamente in esecuzione un *sistema operativo per router*, come ad esempio [[Cisco IOS]].

### Fase di boot
Vediamo come si svolge la sequenza di **boot** di un router, studiando il listato che si ottiene sulla console in fase di boot. Prima di tutto, abbiamo che la procedura a grandi linee sarà:
- Appena l'alimentazione è stabile e il router può avviarsi, l'hardware esegue il **POTS** (*Power On Self Test*). Segue l'inizio dell'esecuzione da parte del processore del caricatore di *bootstrap*;
- Questo cercherà nella memoria flash l'immagine del sistema operativo [[Cisco IOS]], e quindi la caricherà in memoria;
- Una volta caricata l'immagine del sistema operativo, questo entra in esecuzione. Si ha quindi un listato delle caratteristiche tecniche del router, e quindi viene caricata la configurazione precedentemente salvata nella NVRAM (la cosiddetta *startup-config*). Per maggiori informazioni riguardo alla configurazione della NVRAM si rimanda alle note sul sistema operativo IOS.

Vediamo quindi un listato tipo che si ottiene da un router in fase di boot sulla porta seriale (o comunque su un terminale, anche successivamente al boot, attraverso il comando `show version`).

``` 
1) Boilerplate, informazioni legali e di base

System Bootstrap, Version 15.2(2r)T1, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 2012 by cisco Systems, Inc.
Total memory size = 1024 MB
C819HGW-V-A-K9 platform with 1048576 Kbytes of main memory
Main memory is configured to 32 bit mode
Readonly ROMMON initialized

2) Caricamento e decompressione dell'immagine di IOS

IOS Image Load Test
___________________

Digitally Signed Production Software
program load complete, entry point: 0x4000000, size: 0x319275c
Self decompressing the image :
########################################################################## [OK]

3) Inizio dell'esecuzione di IOS, prima configurazione

Smart Init is enabled
smart init is sizing iomem
TYPE MEMORY_REQ
TOTAL: 0x00000000
Rounded IOMEM up to: 0Mb.
Using 6 percent iomem. [0Mb/512Mb]

Restricted Rights Legend
Use, duplication, or disclosure by the Government is
subject to restrictions as set forth in subparagraph
(c) of the Commercial Computer Software - Restricted
Rights clause at FAR sec. 52.227-19 and subparagraph
(c) (1) (ii) of the Rights in Technical Data and Computer
Software clause at DFARS sec. 252.227-7013.
cisco Systems, Inc.
170 West Tasman Drive
San Jose, California 95134-1706

Cisco IOS Software, C800 Software (C800-UNIVERSALK9_IOX-M), Version 15.5(1)T, RELEASE SOFTWARE (fc2)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2014 by Cisco Systems, Inc.
Compiled Wed 26-Nov-14 19:27 by mnguyen

This product contains cryptographic features and is subject to United
States and local country laws governing import, export, transfer and
use. Delivery of Cisco cryptographic products does not imply
third-party authority to import, export, distribute or use encryption.
Importers, exporters, distributors and users are responsible for
compliance with U.S. and local country laws. By using this product you
agree to comply with applicable laws and regulations. If you are unable
to comply with U.S. and local laws, return this product immediately.

A summary of U.S. laws governing Cisco cryptographic products may be found at:
http://www.cisco.com/wwl/export/crypto/tool/stqrg.html

If you require further assistance please contact us by sending email to
export@cisco.com.

4) Listato delle caratteristiche tecniche (interfacce, memoria disponibile)

Cisco C819G-4G-V-K9 (revision 6.0) with 490572K/33715K bytes of memory.
Processor board ID FTX1906822L
1 Ethernet interface(s)
4 FastEthernet interface(s)
1 Gigabit Ethernet interfaces
1 Low-speed serial(sync/async) network interface(s)
DRAM configuration is 32 bits wide
255K bytes of non-volatile configuration memory.
999936K bytes of ATA System CompactFlash (Read/Write)
```