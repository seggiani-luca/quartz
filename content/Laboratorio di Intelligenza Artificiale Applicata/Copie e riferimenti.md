In [[Python]] un oggetto creato viene preso per riferimento ogni volta che lo si usa in seguito. Cioè, ad esempio, prendendo [[Liste]]:
```python
a = [1, 2, 3]
b = [4, a, 5]

a[1] = 6
print(b[1]) # 1, 6, 3
         # b vede il cambiamento di a!
```
Quello che osserviamo è che una lista viene presa per riferimento, e quindi una variazione della lista originale varia ogni successivo utilizzo della stessa. Ricordiamo che possiamo modificare una lista in primo luogo dipende dalla sua [[Mutabilità]].

### Funzione copy()
Per ovviare al problema dei riferimenti nel caso servisse una copia originale degli oggetti, si può usare la funzione `copy()`. Sempre in relazione all'esempio precedente:
```python
a = [1, 2, 3]
b = [4, a.copy(), 5]

a[1] = 6
print(a) # 1, 6, 3
         # a è cambiato

print(b[1]) # 1, 2, 3
            # b non vede il cambiamento di a!
```