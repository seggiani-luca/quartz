Come abbiamo visto in [[File#Blocco with as]], in [[Python]] abbiamo a disposizione dei meccanismi che ci permettono di allocare e rilasciare risorse contestualmente al loro utilizzo. Chiamiamo questo meccanismo quello dei **context manager**.
L'uso tipico dei context manager è con lo statement `with ... as ...`, che assicura che una risorsa aperta dopo il `with` venga gestita correttamente qualsiasi siano gli avvenimenti all'interno del blocco.

```python
with open("mio_file.txt", "w") as f:
	# qui possiamo usare il file 
# qui il file viene liberato (implicitamente)
```

Senza context manager, avremmo dovuto usare una sintassi del tipo:

```python
file = open("mio_file.txt", "r")
try:
	# qui possiamo usare il file 
finally: 
	# qui il file viene liberato (esplicitamente)
	file.close()
```

### Context manager multipli
Notiamo che si possono usare più context manager in un unico statement `with ... as ...`. Ad esempio, vediamo come possiamo aprire sia un file di ingresso che uno di uscita, contemporaneamente:

```python
with open("input.txt", "r") as input_file, open("output.txt", "w") as output_file:
	# maiuscolizza
	data = input_file.read()
	output_file.write(data.upper())
```

### Implementazione di un context manager
Di base, i context manager sono [[Oggetti]] che implementano le seguenti funzioni (chiamate *di nascosto* dal blocco `with ... as ...`), come già detto in [[File#Blocco with as]]:
- `__enter__()`: acquisisce la risorsa file e la restituisce, chiamata quando si entra nel contesto del blocco `with ... as ...`;
- `__exit__()`: libera la risorsa file, chiamata quando si esce dal contesto.

Vediamo un implementazione di esempio di un context manager:

```python
class FileManager:
	def __init__(self, filename, mode):
		self.filename = filename
		self.mode = mode
		self.file = None
		
	def __enter__(self):
		self.file = open(self.filename, self.mode)
		return self.file
		
	def __exit__(self, exc_type, exc_val, exc_tb):
		if self.file:
			self.file.close()
			return False # propaga le eccezioni
```

Notiamo la funzione `__exit__` in particolare:
- Questa prende in argomento le eccezioni che provocano l'eventuale chiusura della risorsa. In particolare, la firma è `def __exit__(self, exc_type, exc_val, exc_tb):` dove `exc_type` è il tipo di eccezione, `exc_val` è il suo valore, ed `exc_tb` è il *traceback*;
- Questa può quindi restituire un valore booleano che segnala se propagare o meno le eccezioni ricevute. In particolare, se si restituisce `False`, l'eccezione viene propagata, mentre se si restituisce `True` l'eccezione viene soppressa a questo livello.
In ogni caso, la `__exit__` prende in argomento un'unica sulla risorsa aperta (la prima che viene sollevata).

### Context manager da generatori
Si può usare una utility fornita nel modulo `contexlib` per generare context manager a partire da [[Generatori]]. Questa in particolare è il decoratore `@contextmanager`:

```python
from contextlib import contextmanager
	@contextmanager
	def open_file(filename, mode):
		file = open(filename, mode)
		try:
			yield file # restituisce la risorsa (un file)
		finally:
			file.close()
```