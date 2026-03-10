In [[Python]] tutto è un **oggetto**.

Per eliminare un riferimento a un oggetto si usa:

```python
del x
```

`del` elimina il riferimento, non necessariamente l’oggetto immediatamente: l’oggetto viene liberato quando non esistono più riferimenti (*reference counting* + *garbage collection*).

Python usa il paradigma delle **classi** per i suoi oggetti, quindi si ha:
- **Class** → definizione di un tipo
- **Object** → istanza di una classe
- **Method** → funzione definita nella classe
- **Attribute** → variabile appartenente all’oggetto.

Una classe si definisce con:
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
Per l'*introspezione* (*riflessione*) delle classi in Python si può usare il metodo `dir`. Questo:
- restituisce i metodi con `__` (quelli privati);
- i metodi definiti nella classe
- gli attributi dell'oggetto.

Se si usa `dir()` direttamente sul **tipo**:
```python
dir(Cat)
```
si trovano ulteriori metodi definiti col `__` definiti dal tipo.