L'algoritmo **OSPF** (*Open Shortest Path First*) è un algoritmo di routing di tipo [[Link State]] aperto, e ampiamente impiegato nelle reti di router.

### AS
Un singolo dominio di routing all'interno di OSPF viene detto **AS** (*Autonomous System*). 
- Su Internet, ogni AS viene identificato da un numero centralmente assegnato. 
- Ad ogni router dentro un AS, quindi, assegniamo una stringa di 32 bit univoca, detta *router id* (che notiamo *non* è l'indirizzo IP). 
- Per supportare la scalabilità dell'operazione, quindi, ogni AS può essere ulteriormente partizionato in *aree*. Un area include un sottoinsieme di router dell'AS e le annesse interfacce. Un router appartiene ad un area se ha almeno un interfaccia connessa a tale area. Ogni area è individuata da una sua stringa di 32 bit univoca, detta *area id*.
OSPF lavora in maniera gerarchica: in ogni area il routing è gestito in maniera autonoma, e vengono definiti meccanismi per l'interscambio di informazioni fra diverse aree. Per la nostra trattazione semplificata, assumiamo che ogni AS sia formato da unica area.

### Tipi di router
I router all'interno degli AS di BGP possono avere 2 ruoli sulla base delle loro interfacce:
- **Router interno**: tutte le interfacce nella stessa area;
- **Router di confine** dell’AS: almeno un’interfaccia collegata a un altro AS.