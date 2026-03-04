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