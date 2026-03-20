Tutti gli oggetti che possono essere usati in un loop [[For]] del [[Python]] vengono detti **iterabili**. Non è detto che un iterabile sia *indicizzabile* o abbia una *lunghezza* definita, ma ciò che è importante è che fornisca una funzione `next()` per l'accesso al prossimo elemento.

I loop [[For]] ottengono automaticamente un iteratore dagli oggetti iterabili forniti. Si può anche usare la funzione `iter()` sugli oggetti iterabili per ottenerne esplicitamente un iteratore.

### Enumerazione di iteratori
Abbiamo detto che gli iteratori non sono necessariamente indicizzabili. Se si desidera avere un indice, si può usare la funzione `enumerate()`. Questa prende come argomento un iteratore e fornisce un altro iteratore, che a sua volta restituisce [[Tuple]] `(<indice>, <valore>)` col valore restituito dall'iteratore originale.
```python
def gen():
	a = 42
	while(True):
		a = a + 1
		yield a # questo riprende il flusso di controllo da qui 
		        # alla prossima chiamata

for (idx, val) in enumerate(gen()):
	# vede (0, 42), (1, 43), ...
	if val > 50: break
```

### Oggetti iteratore
Vediamo il concetto di [[Oggetti]] iteratore nel dettaglio. In generale, possiamo dire che un *iterabile* è *qualsiasi* oggetto su cui si può ciclare ottenendo elementi ([[Liste]], [[Dizionari]], ecc...), mentre un *iteratore* è un oggetto che rappresenta uno stream di dati, permettendone l'accesso uno alla volta. 

L'oggetto iteratore (o un oggetto iterabile che quindi fornisce un iteratore) dovrà implementare il cosiddetto *protocollo iteratore*, che di base consiste definire due metodi:
- `__iter__`: restituisce l'iteratore stesso (non necessariamente un istanza di questo oggetto, ad esempio ha senso avere una classe che restituisce un iteratore di tipo diverso);
- `__step__`: il metodo che restituisce il prossimo elemento dell'iteratore. Questo deve venire effettivamente implementato dall'oggetto iteratore stesso. Ha il compito di segnalare la fine dell'iteratore lanciando l'eccezione `StopIteration`.
A scopo di esempio, vediamo una classe con annessa classe iteratore:

```python
class EvenNumbers:
	def __init__(self, max_num):
		self.max_num = max_num
		
	def __iter__(self):
		return EvenNumbersIterator(self.max_num)

class EvenNumbersIterator:
	def __init__(self, max_num):
		self.current = 0
		self.max_num = max_num

	def __iter__(self):
		return self

	def __next__(self):
		if self.current > self.max_num:
			raise StopIteration # interrompe l'iteratore
		else:
			self.current += 2
			return self.current - 2
```
