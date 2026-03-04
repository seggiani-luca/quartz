Le liste in [[Python]] sono oggetti definiti di default dal linguaggio. Come abbiamo detto in [[Variabili in Python]], sono rappresentate da vettori dinamici e non da linked list.

Di default le liste Python possono essere variegate:
```python
mia_lista = [12, "Mela", "Bana", 34]
```

Come abbiamo visto, le liste sono [[Sequenze]], per cui supportano l'operatore di indicizzazione e lo [[Slicing]].

### Mutabilità
Una particolarità delle liste è che sono *mutabili*, cioè gli elementi, oltre ad essere variegati, possono essere variati dopo che la lista è stata creata. Come vediamo in [[Mutabilità]], questo non è il caso per tutte le [[Collezioni]] Python.

### Copie e riferimenti
Alle liste Python si applica il concetto delle [[Copie e riferimenti]]. Di default quando si usa una lista dopo averla creata, quello che si ottiene è un riferimento alla lista. Si possono effettuare copie con la funzione `copy()`.

### Operazioni su liste
Sulle liste sono definite diverse operazioni. 
Di base, si possono concatenare liste usando l'operatore `+`:
```python
a = ["mele", "pere"]
b = ["banane", "lampone"]

c = a + b # "mele", "pere", "banane", "lampone"
```

Esistono quindi funzioni come `append()`, `pop()`, ecc... In generale, le liste Python possono essere usate, a discrezione del programmatore, come stack, code, array, e tutte le strutture dati basate su queste.

### List comprehension
Un modo interessante e molto idiomatico in Python di creare liste è quello della [[List comprehension]], una cui versione è disponibile anche per [[Dizionari]] e [[Insiemi]].