La sintassi ad **asterisco** `*` in [[Python]] è stata incontrata ad esempio per l'unpacking delle [[Tuple]], e per la definizione di [[Funzioni]] ad argomenti variabili. In verità, esistono due modi principali di usare la sintassi ad asterisco:

### Come valore destro
Questo è il modo più comune, ed effettua l'unpacking in place di una tupla (vedere [[Tuple]]). Ad esempio, vale l'esempio:
```python
t = (1, 2, 3)  
print(*t) # equivale a print(1, 2, 3)
```

Questa è la stessa sintassi che usiamo nelle dichiarazioni di funzione ad argomenti variabili (vedere [[Funzioni]]). Ad esempio:
```python
def var_fun(*tup):
	# tutti i valori di tup (tupla) sono disponibili qui 
```

### Come valore sinistro
Si può anche usare la sintassi ad asterisco quando si fa l'unpacking *in* qualche insieme di variabili. Nello specifico, se si dice:
```python
a, b, *c = my_tuple
```
si ha che `a` otterrà il primo elemento di `my_tuple`, `b` il secondo, e `c` i rimanenti (qualsiasi siano questi in numero). Questa sintassi ricorda in qualche modo quella di funzione ad argomenti variabili, ma notiamo che si va a popolare una nuova tupla con gli ultimi $n$ elementi di una tupla già esistente (non ad effettuare l'unpacking in place di una tupla preesistente, ciò che accadeva nel primo caso).

### Dizionari
Si può usare la sintassi ad asterisco anche per definire [[Dizionari]]. Di base si ha che:
- La sintassi con 1 asterisco (`*`) definisce una tupla;
- La sintassi con 2 asterischi (`**`) definisce un insieme di chiavi-valore, e quindi un dizionario. Questo significa che con questa sintassi, ad esempio, si può definire un argomento dizionario di lunghezza variabile. La differenza dal passare semplicemente un `dict` è che, in una funzione, la sintassi a 2 asterischi raccoglie anche tutti gli argomenti non posizionali nel dizionario creato (vedere [[Funzioni#Argomenti]]).