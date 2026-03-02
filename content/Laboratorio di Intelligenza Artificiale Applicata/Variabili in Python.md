Le *variabili* in [[Python]] sono analoghe alle variabili di tutti gli altri linguaggi di programmazione: contenitori per valori (nello specifico riferimenti agli spazi di memoria che contengono determinate informazioni).

### Tipizzazione
In particolare, vogliamo fare alcuni cenni al **sistema di tipi** che si usa in Python:
- Python è **strongly typed**: le regole di *casting* fra tipo non possono cambiare in maniera inaspettata;
- Python è **dynamically typed**: gli oggetti a tempo di esecuzione hanno un tipo, non le variabili, perciò i tipi non vengono assegnati prima del tempo di esecuzione;
- Python è **implicitly typed**: i tipi degli oggetti vengono ricavati dai valori che gli vengono assegnati;
- Python è **case sensitive**;
- Python è **object oriented**: tutto è un oggetto.

I tipi predefiniti del Python sono i classici:
- Numeri interi;
- Stringhe;
- Booleani.
Per quanto riguarda le *collezioni*, si hanno i 4 tipi fondamentali:
- **Liste**: rappresentate da array dinamiche (non linked list);
- **Dizionari**: rappresentati da tabelle hash;
- **Tuple**: sono liste con elementi variegati e immutabili. A differenza delle liste, possono essere usate come record di dizionari;
- **Insiemi**: rappresentati ancora da tabelle hash (sono effettivamente dizionari verso booleani).
I *file* sono considerati tipi a sé stanti, e infine si ha supporto per le **classi**.

### Riflessione
Per ottenere il tipo di un oggetto a tempo di esecuzione (che ricordiamo è l'unico contesto in cui il concetto di tipo è effettivamente valido), si può usare `type()`:
```python
type(1)       # <class 'int'>
type("fuffa") # <class 'str'>
```

### Cast esplicito
Per effettuare conversioni esplicite di tipo, si può usare la sintassi `<tipo>()`:
```python
i = 10       # type(i) = <class 'int'>
f = float(i) # type(f) = <class 'float'>
```
