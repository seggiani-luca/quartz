I **dizionari** in [[Python]] sono [[Collezioni]] rappresentate da tabelle hash, che formano *associazioni* fra **chiavi** e **valori**. Sono *indicizzabili* attraverso le chiavi, *mutabili* (vedere [[Mutabilità]]) e *non permettono* duplicati (almeno alle chiavi, nessuno ci vieta di duplicare valori). Come gli [[Insiemi]], non sono **ordinati**.

Un dizionario in Python si definisce specificando chiavi e valori attraverso la sintassi a 2 punti:
```python
d = {"one": 1, "two", 2, "three", 3}
```
In questo caso la chiave è di tipo stringa, mentre il valore è di tipo intero.

### Operazioni sui dizionari
Abbiamo visto che l'indicizzazione dei dizionari si fa per chiave, e non per indici:
```python
specie = {"paperino": "papero", "topolino": "topo"}
spec = specie["topolino"] # spec = "topo"
```
In ogni caso, nulla vieta che le chiavi di un dizionario siano comunque indici numerici.

I dizionari sono mutabili, per cui si possono modificare gli elementi usando l'operatore di indicizzamento (le parentesi quadre).

Sono poi disponibili diverse funzioni per accedere a chiavi e valori di un dizionario:
- `get()`, che prende in argomento la chiave e restituisce il corrispettivo valore. Notiamo che nel caso l'oggetto non venga trovato, `get()` restituisce `None`. Si può fornire un secondo argomento che indica il valore da mettere alla chiave specificato nel caso questa sia vuota;
- `pop()`, che rimuove un valore specificato da una certa chiave, restituendolo;
- `keys()`, che restituisce la lista delle chiavi; 
- `values()`, che restituisce la lista dei valori;
- `items()`, che restituisce una lista di [[Tuple]] che accoppiano chiave a valore.

### Dictionary comprehension
Come per le [[Liste]] e gli [[Insiemi]], i dizionari hanno una forma di comprehension basata sulla sintassi:
```python
insieme = [<espressione> for <elemento> in <sequenza> if <condizione>]
```