[[Python]] è di per se un linguaggio a tipizzazione debole, dove i tipi non vengono controllati a tempo di esecuzione. Si può "riportare" in Python un po' della funzionalità dei linguaggi a tipizzazione forte usando i cosiddetti **type hints**.

Questi di specificare i tipi attesi delle variabili, dei parametri delle funzioni e dei valori di ritorno.
I type hints non influenzano il comportamento a runtime, ma consentono:
- Migliore documentazione del codice;
- Supporto migliorato dagli IDE (auto-completamento, rilevamento degli errori);
- Controllo statico dei tipi con strumenti come **mypy**;
- Migliore manutenibilità del codice.

### Tipi base
Per i tipi **base** (vedere [[Variabili in Python]]), possiamo usare direttamente i nomi dei tipi:
- `int`: tipi interi;
- `float`: tipi a virgola mobile;
- `bool`: tipi booleani;
- `str`: tipi stringa;
- `bytes`: sequenze di byte;
- `None`: il tipo nullo.

### Tipi derivati
Per i tipi **derivati** (come le [[Collezioni]]), a partire da Python 3.10, si può usare la seguente sintassi:

```python
numbers: list[int] # numbers è una lista di tipi interi
coordinates: tuple[float, float] # coordinates è una tupla (float, float)
# ...
```

Prima di Python 3.10, si doveva usare il modulo `typing`:

```python
from typing import List, Dict, Tuple, Set

numbers: List[int] = [1, 2, 3, 4, 5]
coordinates: Tuple[float, float] = (10.5, 20.3)
```

dove i tipi derivati venivano ridefiniti come classi (quindi stavolta con la lettera maiuscola, per distinguere). Per questi tipi *ridefiniti* valevano i type hint coi tipi base.

### Funzioni con type hint
I type hint, base o derivati, possono usarsi anche nelle **funzioni**:

```python
def divide(a: int, b: int) -> float:
	return a / b
```

dove la sintassi *a freccia* `->` indica il tipo di ritorno.

### Tipi `callable`
Esiste un tipo particolare di tipo derivato definito in `typing`, che è il tipo `callable`, usato per funzioni (o funzioni lambda, sostanzialmente oggetti che possono essere chiamati come funzioni):

```python
OperationFunc = Callable[[int, int], float]

def apply_operation(x: int, y: int, operation: OperationFunc) -> float:
	return operation(x, y)

def divide(a: int, b: int) -> float:
	return a / b# Usage

result = apply_operation(10, 5, divide) # restituisce 2.0
```

### Tipi unione
I tipi **unione** sono type hint su più possibili tipi. Questi, ad oggi, stanno nel modulo `typing`. Si specificano con la sintassi a `|` (da Python 3.12) o come `Union`:

```python
from typing import Union

value: Union[int, str] = 42
value: int | str = 42
```

### Alias di tipo
Python permette di definire **alias** di tipo (sostanzialmente definizioni di tipo), secondo 2 modalità (una moderna, a partire da Python 3.12, e una legacy basata su `typing`, che sfrutta il tipo `TypeAlias`
```python
# da 3.12
Url = str
def retry(url: Url, retry_count: int) -> None

# prima
from typing import TypeAlias
Url: TypeAlias = str
def retry(url: Url, retry_count: int) -> None:
```

### Generic
Infine, notiamo che il Python moderno supporta i **generic** come molti altri linguaggi:

```python
from typing import TypeVar, Generic, List

T = TypeVar('T')

class Stack(Generic[T]):
	def __init__(self) -> None:
		self.items: List[T] = []

	def push(self, item: T) -> None:
		self.items.append(item)

	def pop(self) -> T:
		return self.items.pop()


int_stack = Stack[int]() # stack di interi
str_stack = Stack[str]() # stack di stringhe
```