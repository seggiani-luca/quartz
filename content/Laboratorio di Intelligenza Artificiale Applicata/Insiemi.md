In [[Python]], gli **insiemi** sono [[Collezioni]] rappresentate da tabelle hash (sono effettivamente [[Dizionari]] verso booleani, e come questi non sono **ordinati**), che rappresentano oggetti sulla base della loro appartenenza o meno all'insieme stesso. Per questo motivo, come i dizionari, sono *mutabili* (vedere [[Mutabilità]]]]) e *non permettono* duplicati.

Come abbiamo visto, a differenza dei dizionari, non possono essere indicizzati (si usa l'operatore `in` per valutare l'appartenenza):
```python
a = {1, 5, 12}
for i in range(1, 20):
	if i in a: # i è nell'insieme
```

Gli insiemi sono iterabili (e quindi si possono costruire loop [[For]] su di essi). Di contro, non sono indicizzabili, quindi non possono rappresentare [[Sequenze]], e non supportano lo [[Slicing]].

### Casting in liste
Insiemi e [[Liste]] possono essere convertiti l'uno nell'altra e viceversa, usando la solita sintassi per il *casting* (la avevamo vista in [[Formattazione di stringhe]]):
```python
insieme = {"Luca", "Giovanni", "Marco"}
lista = list(insieme)
nuovo_insieme = set(lista)
```

### Operazioni sugli insiemi
Gli insiemi in Python supportano, oltre alle chiare operazioni di inserzione e rimozione elementi (`add()` e `remove()`), tutta una serie di operazioni insiemistiche:  
- **Unione**: `A | B` oppure `A.union(B)`;
- **Intersezione**: `A & B` oppure `A.intersection(B)`;
- **Differenza**: `A - B` oppure `A.difference(B)`;
- **Differenza simmetrica**: `A ^ B` oppure `A.symmetric_difference(B)`. La differenza simmetrica è data dagli elementi che sono solo in `A` o `B`, e non entrambi gli insiemi;
- **Sottoinsieme**: `A <= B` oppure `A.issubset(B)`;
- **Sottoinsieme proprio**: `A < B`;
- **Sovrainsieme**: `A >= B` oppure `A.issuperset(B)`;
- **Sovrainsieme proprio**: `A > B`;
- **Disgiunzione**: `A.isdisjoint(B)`.

### Set comprehension
Sugli insiemi è disponibile una funzionalità simile alla [[List comprehension]] delle [[Liste]] e la corrispettiva funzionalità dei [[Dizionari]]. Si può infatti usare la stessa sintassi:
```python
insieme = [<espressione> for <elemento> in <sequenza> if <condizione>]
```
per formare insiemi a partire da sequenze arbitrarie.