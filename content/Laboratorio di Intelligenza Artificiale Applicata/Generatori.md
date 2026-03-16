I **generatori** sono tipi speciali di [[Funzioni]] che restituiscono [[Iteratori]] che producono valori *uno alla volta*, solo quando richiesti. Questo approccio è chiamato anche *lazy evaluation*, in quanto i valori sono calcolati solo quando richiesti (ma possono comunque essere scorsi come [[Liste]] o altre [[Collezioni]]).

Si definiscono usando la parola chiave `yield` invece di `return` per i valori di ritorno delle funzioni:

```python
def count(n):
    i = 0
    while i < n:
        yield i
        i += 1

g = count(3)

print(next(g))  # restituisce 0
print(next(g))  #             1
print(next(g))  #             2
```

La cosa interessante è chiaramente usare generatori per avere iteratori in un ciclo:

```python
for x in count(3):
    print(x) # stampa 0, 1, 2
```