Le **list comprehension** (o *comprensioni di lista* in italiano) sono una funzionalità offerta dal linguaggio [[Python]] per costruire nuove [[Liste]] a partire da un espressione eseguita su ogni elemento di [[Sequenze]].
La list comprehension è in genere un modo molto idiomatico (pythonico) di fare le cose in Python.

Generalmente la list comprehension è formata dalla sintassi:
```python
lista = [<espressione> for <elemento> in <sequenza> if <condizione>]
```
dove:
- La `lista` è chiaramente la lista che otteniamo dalla list comprehension;
- L'`elemento` è la variabile che contiene il generico elemento della sequenza `sequenza`;
- La `sequenza` è appunto una sequenza da cui estraiamo elementi per popolare la lista;
- La `condizione` viene valutata su ogni elemento della sequenza e determina se quell'elemento appartiene o meno alla lista generata (`lista`). Notiamo quindi che è possibile usare la variabile `elemento` all'interno della condizione.

A scopo di esempio, vediamo come si può dividere una stringa individuando i caratteri in posizioni pari:
```python
str = "Questa è una stringa..."
chars = [c for (i, c) in enumerate(str) if i % 2 == 0]
# 'Q', 'e', 't', ' ', ' ', 'n', ' ', 't', 'i', 'g', '.', '.'
```
Ricordiamo che potevamo fare qualcosa di simile, ma ottenendo un'altra stringa anziché una lista, usando lo [[Slicing]]:
```python
str = "Questa è un'altra stringa..."
str_even = str[0::2] # "Qet  n tig.."
```

### Set comprehension
Notiamo che una forma di *comprehension* è disponibile anche per gli [[Insiemi]], con una sintassi del tutto simile a quella vista per le liste:
```python
insieme = [<espressione> for <elemento> in <sequenza> if <condizione>]
```

Dopotutto, avevamo visto come gli [[Insiemi]] supportano in maniera naturale il casting a [[Liste]], e viceversa.
### Dictionary comprehension
Anche per i [[Dizionari]] abbiamo una forma di comprehension basata sempre sulla solita sintassi:
```python
insieme = [<espressione> for <elemento> in <sequenza> if <condizione>]
```