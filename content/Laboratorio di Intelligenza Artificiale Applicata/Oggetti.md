In [[Python]] tutto è un **oggetto**.

Per eliminare un riferimento a un oggetto si usa:

```python
del x
```

`del` elimina il riferimento, non necessariamente l’oggetto immediatamente: l’oggetto viene liberato quando non esistono più riferimenti (*reference counting* + *garbage collection*).

Python usa il paradigma delle **classi** per i suoi oggetti, quindi si ha:
- **Class** → definizione di un tipo (*class Class*);
- **Object** → istanza di una classe (*obj = Class()*);
- **Method** → funzione definita nella classe (*obj.method()*);
- **Attribute** → variabile appartenente all'oggetto (*object.attribute*). Gli attributi di default sono tutti *pubblici*, cioè vi si può accedere da qualsiasi altra parte nel codice. La convenzione per gli attributi privati è di prefiggerli con `__`. Notiamo che questo non rende effettivamente gli attributi privati, ma semplicemente cambia il loro nome in modo da non renderli accessibili col nome attraverso il quale vengono dichiarati (il Python non ha veri membri privati). Esiste anche la convezione con un singolo `_`, che rende un attributo "*semi-privato*": il codice funzionerà anche se lo si usa, ma è sconsigliabile farlo.

Una classe si definisce quindi con la seguente sintassi:

```python
class Cat:
    def __init__(self, name):
        self.name = name
```

dove `__init__` è un metodo speciale che funge sostanzialmente da *costruttore*. In questo contesto, `self` è il puntatore *this*.

### Oggetti built-in
Gli oggetti base (`int`, `list`, `dict`, ecc.) sono implementati in C dentro l’interprete (l'interprete più comune, scritto in C, del Python) e poi esposti al linguaggio Python.
A scopo di esempio, vediamo che in *CPython*  le liste sono implementate come segue:

```c
typedef struct {
    PyObject_VAR_HEAD
    PyObject **ob_item;
    Py_ssize_t allocated;
} PyListObject;
```

Dove:
- `PyObject_VAR_HEAD` → header comune a tutti gli oggetti Python  
- `ob_item` → array di puntatori agli oggetti  
- `allocated` → capacità allocata della lista  

Per via del fatto che gli oggetti vengono effettivamente allocati dentro oggetti C, si ha che questi sono più lenti della controparte che potremmo implementare in C.

### Classi come oggetti
Anche le istanze di classi, chiaramente, sono oggetti.  Internamente funzionano in modo simile a **dizionari** che contengono:
- Metodi;
- Attributi;
- Metadati della classe.

### Introspezione
Per l'**introspezione** (*riflessione*) delle classi in Python si può usare il metodo `dir`. Questo:
- restituisce i metodi con `__` (quelli privati);
- i metodi definiti nella classe
- gli attributi dell'oggetto.

Se si usa `dir()` direttamente sul **tipo**:

```python
dir(Cat)
```

si trovano ulteriori metodi definiti col `__` definiti dal tipo.

### Overriding dei metodi
Python supporta l'**overriding** dei metodi. Ad esempio, i metodi di default possono essere ridefiniti da una classe, per fornire funzionalità che sia specifica alla semantica di quella classe. Vediamo un esempio:

```python
class Cat:
	def __init__(self, name, color):
		self.name = name
		self.color = color
		
	def __repr__(self):
		return f"Un gatto {self.color} di nome {self.name}"
```

In questo caso la classe `Cat` ridefinisce la funzione `__repr__`, che è una funzione di conversione a stringa usata quando si fa la `print` di oggetti. 

L'*overriding* delle funzioni permette l'**overloading** degli operatori: esistono infatti funzioni particolari (ad esempio `__add__`) che equivalgono agli operatori aritmetici e relazionali di default del linguaggio. Ridefinire tali funzioni equivale a ridefinire il comportamento di tali operatori sugli oggetti su cui ridefiniamo. 