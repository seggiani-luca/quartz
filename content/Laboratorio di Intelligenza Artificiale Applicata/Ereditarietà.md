Gli [[Oggetti]] [[Python]] supportano l'**ereditarietà** attraverso la sintassi:

```python
class Animal:
	def __init__(self, name, color):
		self.name = name
		self.color = color
		
class Cat(Animal):
	def sound(self):
		print("Miao!")

class Dog(Animal):
	def sound(self):
		print("Bau!")
```

Se vogliamo raggiungere attributi della superclasse all'intero di una sottoclasse dobbiamo accedere al costruttore della superclasse nel costruttore della sottoclasse, attraverso la `super()`:

```python
class Person:
	def __init__(self, name):
		self.name = name

class Student:
	def __init__(self, name, id):
		super().__init__(self, name)
		self.id = id
		
	def __repr__(self):
		return f"Lo studente {self.name}, matricola {self.id}"
```

### Verifiche di istanze
Per verificare se un oggetto appartiene a qualche classe, o a un ereditaria di tale classe, esiste il metodo `isinstance`. Per fare verifiche nello specifico riguardo alle sottoclassi, esiste anche `issubclass`.

### Ereditarietà multipla
Python supporta l'ereditarietà **multipla**, secondo la stessa sintassi di prima.

```python
class UomoTigre(Cat, Person):
	# ...
```

In particolare, quando ogni attributo o funzione viene usato, viene eseguita una *ricerca* dalla classe derivata a tutte le classi base per il simbolo cercato (in maniera ricorsiva).

### Polimorfismo
In Python il **polimorfismo** è implementato col *duck typing*: se due oggetti implementano gli stessi metodi e gli stessi attributi, si possono usare in maniera polimorfa. Il linguaggio (di base) non effettua nessun tipo di aiuto nei nostri confronti, e dobbiamo assicurarci in qualche modo di usare gli oggetti che definiamo nella maniera corretta.