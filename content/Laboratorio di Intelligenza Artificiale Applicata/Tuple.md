Le **tuple** in [[Python]] sono liste con elementi variegati e *immutabili* (vedere [[Collezioni]] ed [[Mutabilità]]). *Permettono* di avere elementi duplicati. A differenza delle liste, possono essere usate come record di [[Dizionari]].

Una tupla può essere definita con la sintassi fra parentesi o senza:
```python
tupla0 = ('a', 2, "ciao")
tupla1 = 'b', 3, "salve" # vale lo stesso
```
Si possono avere tuple con un unico elemento ponendo una virgola dopo la variabile o il letterale che costituisce l'elemento:
```python
a = (1)
b = (1,)
c = 1,
# sono tutte tuple valide!
```
Per avere tuple vuote, si deve invece usare una virgola e per forza le parentesi:
```python
d = (,)
e = ()
f = , # errore
```

### Operazioni sulle tuple
Sulle tuple valgono tutte le operazioni che valevano sulle [[Liste]], quindi l'indicizzazione come [[Sequenze]], e lo [[Slicing]] (ricordando che, essendo queste *immutabili*, lo slicing restituisce una nuova tupla che non può essere assegnata alla tupla originale, non modificabile). Chiaramente, non è possibile usare altre operazioni che modificano la tupla.

Risulta importante ricordare che fa eccezione anche l'operazione di *assegnamento* a tupla: i singoli elementi risentono dell'immutabilità, per cui cercare di modificarli nella tupla restituisce un errore:
```python
tup = (2, "foo", 3)
tup[1] = "bar" # eccezione! 'tuple' object does not support item assignment
```

### Packing e unpacking
Quando si assegna un valore ad una tupla, effettivamente si vanno ad assegnare *più* valori alla stessa variabile, un processo detto *packing*:
```python
var_packed = (var0, var1, var2)
```
Questi valori possono essere ricavati attraverso la sintassi dell'*unpacking*:
```python
var0, var2, var2 = var_packed
```

Packing e unpacking sono molto utili in diverse situazioni. Di base, permettono di avere in maniera molto semplice il ritorno multiplo da funzioni:
```python
def fun_multi():
	return 69, 420
	
a, b = fun_multi() # a = 69, b = 420
```

### Scambio di variabili
Un'altro *party trick* interessante è quello di effettuare lo scambio di due variabili senza una variabile di appoggio, usando esclusivamente le funzioni di packing e unpacking. Di norma, in un linguaggio di programmazione che supporta le variabili, per scambiare i valori di 2 variabili si deve dire:
```python
t = a # t è una variabile di appoggio
a = b
b = t
```
Usando la funzionalità appena vista, in Python si può dire direttamente:
```python
a, b = b, a # packing e unpacking sulla stessa linea
```
dove si ha *packing* a destra dell'uguale e *unpacking* a sinistra, con il risultato di scambiare i valori delle variabili `a`e `b`.

### Funzione zip()
La funzione `zip()` permette di trasformare un certo numero di iterabili (vedere [[Iteratori]]) in un iteratore restituente tuple con lo stesso numero di elementi, prendendo ogni volta il prossimo elemento da ogni iterabile. Ad esempio:
```python
nums = [1, 2, 3, 4]
chars = ['a', 'b', 'c', 'd']

for n, c in zip(nums, chars):
	print(f"Num: {n}, char: {c}") # vede (1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')
```