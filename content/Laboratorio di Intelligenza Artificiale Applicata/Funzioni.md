In [[Python]] le funzioni si definiscono attraverso la parola chiave `def`:
```python
def fun():
	return 420
```

### Visibilità
Nelle funzioni Python valgono le solite regole di **visibilità**, cioè all'interno di un blocco funzione sono visibili le variabili dichiarate nei blocchi esterni, e ridefinendo variabili all'interno del blocco si oscura la visibilità.

### Argomenti
Tutti i tipi in Python, nelle chiamate di funzione, vengono passati per **riferimento** (tranne chiaramente i tipi primitivi come gli interi). Questo significa che se e.g. si passa una lista, una variazione della lista all'interno del corpo funzione comporta la stessa variazione della lista anche nel chiamante.

Esistono due modi di indicizzare gli argomenti di funzione:
- **Posizionale**, che è il modo a cui siamo abituati da linguaggi di programmazione classici. La lista degli argomenti viene specificata nella dichiarazione di funzione, e ci si aspetta che la funzione venga chiamata con gli stessi argomenti in tale ordine;
- A **parola chiave**, che è specifico del Python, permette di usare una sintassi `key=value` per specificare il *valore* di un qualsiasi argomento identificandolo col suo nome (cioè la sua *chiave*) nella dichiarazione della funzione. Questo avviene quindi in maniera *non posizionale*. La regola è che gli argomenti non posizionali possono trovarsi solo *dopo* gli argomenti posizionali.
Vediamo ad esempio:
```python
def foo(a, b, c):
	pass

foo(1, 2, 3)     # totalmente posizionale
foo(1, c=2, b=3) # non posizionale e posizionale misto
foo(c=2, 1, 2)   # errore!
```

Si possono avere argomenti **variabili** attraverso la [[Sintassi ad asterisco]] `*`. Avevamo visto questa sintassi per l'*unpacking* in [[Tuple#Packing e unpacking]]. Ad esempio:
```python
def var_fun(*tup):
	# tutti i valori di tup (tupla) sono disponibili qui 
```
Come abbiamo visto in [[Sintassi ad asterisco]], poi, si può usare la sintassi a 2 asterischi per avere come argomenti dizionari a lunghezza variabile (composti eventualmente anche dagli argomenti non posizionali raccolti).

### Funzioni lambda
Il Python supporta le funzioni lambda attraverso la parola chiave (fantasiosa) `lambda`. La sintassi è la seguente:
```python
my_lambda = lambda x: x 2
```
dove si specifica l'argomento (o argomenti, può essere una tupla), i 2 punti per indicare che inizia il corpo della lambda, e quindi il corpo della lambda stesso. 
Come in tutti i linguaggi imperativi che le supportano, le lambda possono essere usate come argomenti di funzioni (ad esempio la `sort`) che implementano funzioni di confronto, o di esecuzione su singoli argomenti, ecc... 
#### `sort`
Ad esempio, vediamo l'uso in una `sort`:
```python
# sort (n, l) combinations by aufbau
nls.sort(key=lambda x: (x[0] + x[1], x[0]))
```
Nell'esempio vediamo come si usa anche la notazione non posizionale per l'argomento `key`, che indica la funzione usata da `sort` come comparatore fra gli elementi. Specifichiamo quindi questa funzione come una lambda.

#### `map`
Per fare un altro esempio, vediamo che esiste la funzione `map` che può essere applicata ad iteratori per far passare ogni elemento attraverso una certa funzione (che spesso definiamo come una lambda). Ad esempio:
```python
my_list = # ...
new_list = list(map(lambda x: x * 2, my_list)) # raddoppio my_list
```

#### `filter`
Vediamo un esempio simile al precedente, che è quello della `filter`. Questa è analoga alla `map`, ma sfrutta un valore booleano che usa per rimuovere alcuni elementi (rimuove gli elementi che restituiscono `False`, e mantiene quelli che restituiscono `True`). Ad esempio:
```python
my_list = # ...
new_list = list(filter(lambda x: x % 2 == 0, my_list)) # mantiene i pari
```

### `any`
`any` è un'altra funzione eseguibile su iterabili, che valuta se almeno uno degli elementi forniti ha un valore `True`. Se si fornisce il vettore vuoto, restituisce `False`. Si può usare la `any` in congiunzione a `map` per valutare il risultato di una funzione booleana su un vettore, ad esempio:
```python
any(num > 10 for num in numbers) # controlla se c'è almeno un numero > 10
```
Quello che accade in questo caso è che la sintassi `num > 10 for num in numbers`, analoga alla [[List comprehension]] (vediamo che in verità vengono creati [[Generatori]]), mappa da numeri a booleani, che quindi vengono gestiti da `any`. La stessa cosa fatta con `map` sarebbe:
```python
any(map(lambda x: x > 10, numbers))
```