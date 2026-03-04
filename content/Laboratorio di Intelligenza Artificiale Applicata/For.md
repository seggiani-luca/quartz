Il costrutto `for` in [[Python]] è leggermente più interessante degli altri: di base si itera non su una variabile di iterazione intera, ma su [[Sequenze]].
La sintassi è quindi:
```python
for a in sequenza:
	pass # a è ogni elemento di sequenza
```

Ad esempio, è abbastanza idiomatico (si dice *"pythonico"*) iterare su una stringa attraverso un `for`:
```python
for c in "prova":
	pass # vede 'p', 'r', 'o', 'v', 'a'
```

### Iteratori
Di base, la funzionalità dei `for()` si basa su quella degli [[Iteratori]]. Nel dettaglio, si chiama la funzione `next()` per chiamare ogni elemento successivo della sequenza ad ogni iterazione.
### Funzione range()
Per avere la classica forma dei `for` con variabile di iterazione, si può usare la funzione `range()`. Questa, in maniera analoga all'operatore di [[Slicing]], prende come argomento due bound e uno stride:
```python
for i in range(1, 5, 2):
	pass # vedrà 1, 3
```