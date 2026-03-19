I **decoratori** in [[Python]] sono particolari [[Funzioni]] che prendono in argomento altre funzioni, aggiungono qualche tipo di funzionalità a monte e a valle di queste (*wrapping*), e restituiscono la risultante funzione modificata. 

```python
def uppercase_decorator(func): # decoratore
	def wrapper():             # funzione wrapper
		original_result = func()
		modified_result = original_result.upper()
		return modified_result
	return wrapper

def greet():
	return "Ciao Mondo!"

greet = uppercase_decorator(greet) # applicazione manuale del decoratore
print(greet()) # Output: CIAO MONDO!
```

L'utilità dei decoratori è data dal fatto che il linguaggio stesso ne mette a supporto una sintassi specifica:

```python
def uppercase_decorator(func): # decoratore
	def wrapper():             # funzione wrapper
		original_result = func()
		modified_result = original_result.upper()
		return modified_result
	return wrapper

@uppercase_decorator # applicazione automatica del decoratore
def greet():
	return "Ciao Mondo!"

print(greet()) # Output: CIAO MONDO!
```

La sintassi dei decoratori "svolge" le funzioni indicate dalla sintassi a chiocciola `@` fornendo come argomento la funzione immediatamente seguente finché non si ottiene una nuova funzione, appunto, decorata. Si possono applicare i decoratori anche alle classi.
Si possono inoltre accodare più decoratori uno dopo l'altro, combinandone gli effetti (il secondo decoratore prende la funzione decorata dal primo, e così via).

### Decoratori con argomenti
I decoratori possono supportare argomenti (notiamo, gli argomenti della funzione decorata) attraverso il `*args, **kwargs` della classica [[Sintassi ad asterisco]], che prende tutti gli argomenti in formato lista e in formato dizionario (i cosiddetti *keyword arguments*).

```python
def uppercase_decorator(func):
	def wrapper(*args, **kwargs):
		original_result = func(*args, **kwargs)
		return original_result.upper()
	return wrapper
	
@uppercase_decorator
def greet(name):
	return f"Ciao {name}!"
	
print(greet("Imane")) # Output: CIAO IMANE!
```

I decoratori possono quindi accettare i loro stessi parametri (non quelli della funzione decorata) utilizzando un ulteriore livello di annidamento, secondo la sintassi (un po' convoluta):

```python
def repeat(n=1):                      # wrapper del decoratore
	def decorator(func):              # decoratore
		@functools.wraps(func)        
		def wrapper(*args, **kwargs): # funzione wrapper
			result = None
			for _ in range(n):
				result = func(*args, **kwargs)
			return result
		return wrapper
	return decorator

@repeat(n=3) # chiama repeat(n=3)
             # -> restituisce decorator(say_hello) con n=3 nella closure
def say_hello():
	print("Ciao")
	return "Done"
	
say_hello() # Output: Ciao Ciao Ciao
```

### Preservazione dei metadati
Di default, la funzione *wrapper* di un decoratore (quella che effettivamente viene restituita) è una funzione a se stante che chiama la funzione originale (quella che viene decorata). In questo modo, i metadati (nome, documentazione, ecc...) della funzione originale vengono sovrascritti.
Visto che questo potrebbe essere non desiderabile, il linguaggio mette a disposizione nel modulo `functools` un'utilità per preservare i metadati originali, che è a sua volta un decoratore:

```python
import functools

def uppercase_decorator(func):
	@functools.wraps(func) # preserva i metadati
	def wrapper(*args, **kwargs):
		original_result = func(*args, **kwargs)
		return original_result.upper()
	return wrapper
```

### Decoratori di classe
Come abbiamo anticipato, si possono applicare i decoratori anche alle classi (vedere [[Oggetti]]). Questo permette di modificarne il comportamento introducendo nuovi metodi in maniera programmatica:

```python
def add_greeting(cls):
	cls.greet = lambda self: f"Ciao, sono {self.name}"
	return cls
	
@add_greeting
class Person:
	def __init__(self, name):
		self.name = name
		p = Person("Luca")
		
print(p.greet()) # Output: Ciao, sono Luca
```

Notiamo che anche classi di tipo *Callable*, cioè che implementano il metodo `call`, possono essere usate a mo' di decoratori (e in tal caso dovranno accettare la funzione da decorare come argomento del costruttore).

[[Python]] include diversi decoratori di default per quanto riguarda i membri di classe, che vanno a sostituire quelle che negli altri linguaggi sono i membri statici sono funzionalità come le proprietà con *getter*/*setter*, i membri *statici*, ecc...
- `@property`: converte un metodo in una proprietà, e permette di specificare getter e setter come `@func.getter` e `@func.setter`;
- `@classmethod`: passa come primo argomento ad una funzione la definizione di classe stessa anziché l'istanza di classe su cui viene chiamata. Effettivamente rappresenta la cosa più vicina in Python che abbiamo ai metodi statici;
- `@staticmethod`: contrariamente al nome, non rappresenta un metodo statico vero e proprio, ma solo una funzione che non accetta niente di relativo alla classe (né l'istanza specifica né la definizione) come primo argomento. Ha senso solo per raggruppare il codice;
- `@abstractmethod`: segnala un metodo di classe come astratto (da specializzare in una sottoclasse). La chiamata del metodo astratto, cioè nella classe base non specializzato, comporta che automaticamente venga sollevata un'eccezione. 