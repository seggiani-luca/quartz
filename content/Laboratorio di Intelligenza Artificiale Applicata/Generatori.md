I **generatori** sono tipi speciali di [[Funzioni]] che restituiscono [[Iteratori]] che producono valori *uno alla volta*, solo quando richiesti. Questo approccio è chiamato anche *lazy evaluation*, in quanto i valori sono calcolati solo quando richiesti (ma possono comunque essere scorsi come [[Liste]] o altre [[Collezioni]]). In questo, ci permettono di creare iteratori senza implementare l'intero *protocollo* associato agli iteratori (vedere [[Iteratori#Oggetti iteratore]]).

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

Riassumendo, i generatori hanno quindi le seguenti caratteristiche:
- Restituiscono un *oggetto generatore*, anziché una lista di oggetti;  
- Usano `yield` invece di `return`. In questo, mantengono lo stato tra le chiamate, in quanto un singolo flusso di esecuzione viene sospeso ad ogni `yield`;  
- Possono restituire potenzialmente infiniti elementi, senza occupare memoria infinita;
- Sono efficienti in termini di memoria per dataset di grandi dimensioni: chiariamo questo aspetto. Abbiamo che una lista restituita da una funzione regolare ha dimensione $O(n)$ dove $n$ è il numero di elementi. Per il principio della lazy evaluation, invece, un generatore è un oggetto a dimensione fissa, da cui otteniamo un elemento (sempre di dimensione fissa o comunque contenuta) per volta. Questo rende utili i generatori per gestire dataset di grandi dimensioni, che non potremmo caricare interamente in memoria in una singola lista.

### Generator comprehension
Anche i generatori sono disposti di una funzionalità di comprehension simile alla [[List comprehension]]. In particolare, la **generator comprehension** restituisce oggetti generatori anziché liste. Vediamo un esempio che chiarisce anche il punto precedente di *dimensione* diversa fra liste e oggetti generatore:

```python
# list comprehension 
squares_list = [x * x for x in range(10)]

# generator comprehension
squares_gen = (x * x for x in range(10))

import sys
list_comp = [x for x in range(10000)]
gen_exp = (x for x in range(10000))

print(f"List size: {sys.getsizeof(list_comp)} bytes")    # 85176 byte
print(f"Generator size: {sys.getsizeof(gen_exp)} bytes") # 192 byte
```

### Concatenazione di iteratori
Più generatori possono essere composti (*concatenati*) per creare pipeline di elaborazione dati. Ad esempio:

```python
def generate_numbers(n):
	for i in range(n):
		yield i

def square(numbers):
	for number in numbers:
		yield number * number

def filter_even(numbers):
	for number in numbers:
		if number % 2 == 0:
			yield number
			
			
numbers = generate_numbers(10)      # 0, 1, 2, ..., 9
squared = square(numbers)           # 0, 1, 4, ..., 81
even_squares = filter_even(squared) # 0, 4, 16, 36, 64
```

Notiamo che nel caso di generatori concatenati, da Python 3.3 in poi abbiamo a disposizione lo statement `yield from`, che delega la generazione ad un altro generatore:

```python
def gen1():
	yield 1
	yield 2
	yield 3
	
def gen2():
	yield 4
	yield 5
	yield 6
	
def combined():
	yield from gen1() # 1, 2, 3
	yield from gen2() # 4, 5, 6
```

### Generatori ricorsivi
Lo `yield from` permette di creare generatori *ricorsivi*, cioè che generano da se stessi:

```python 
def flatten(nested_list):
	"""Flatten a nested list structure."""
	for item in nested_list:
		if isinstance(item, list):
			yield from flatten(item) # qui si crea un nuovo generatore 
			                         # che viene quindi chiamato da next
		else:
			yield item

nested = [1, [2, [3, 4], 5], 6]
for num in flatten(nested):
	print(num) # 1, 2, 3, 4, 5, 6
```