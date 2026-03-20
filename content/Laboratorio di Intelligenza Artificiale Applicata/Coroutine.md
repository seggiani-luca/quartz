I [[Generatori]] in [[Python]] rappresentano un metodo per implementare le **coroutine**, sostanzialmente un modo per avere "falso" *multithreading*.
Le coroutine con generatori sono particolarmente utili quando è necessario gestire
multitasking cooperativo, elaborazione asincrona o flussi di dati:
1. Iterazione lazy su grandi dataset;
2. Pipeline di elaborazione dei dati;
3. Programmazione asincrona e guidata da eventi;
4. Gestione dello stato tra chiamate di funzione;
5. Simulazione della concorrenza senza thread.

Il meccanismo alla base delle coroutine è la funzione `send` che è possibile chiamare sui generatori per inviare nuovi valori. Ad esempio:

```python
def grep(pattern):
	print(f"Looking for {pattern}")
	while True:
		line = yield
			if pattern in line:
				print(line)

# prepara la coroutine
g = grep("python")
next(g)

g.send("python is great")         # "python is great" 
g.send("javascript is also cool") # ...
g.send("python is better")        # "python is better"
```

Esistono altri metodi di coroutine oltre alla `next`, fra cui:
- `send(value)`: invia un valore alla coroutine;
- `throw(exception)`: lancia un eccezione nel flusso di esecuzione del generatore;
- `close()`: chiude il generatore.