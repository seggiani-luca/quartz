Le **eccezioni** sono un meccanismo offerto da diversi linguaggi di programmazione (fra cui il [[Python]]) che servono a segnalare condizioni inaspettate lungo l'esecuzione di un programma. 

Per lanciare un eccezione si può usare la solita sintassi `raise`:
```python
raise Exception
```

### Eccezioni di default
Python offre una serie di eccezioni di default:
![[except.png|600]]

Ad esempio, vediamo che tutte queste derivano dalla classe `BaseException`, di cui cui sono figlie anche la `SystemExit` (lanciata da `exit()` nel modulo `os`) e `KeyboardInterrupt` (lanciata dal segnale SIGINT all'interprete Python). Seguono quindi le `Exception` vere e proprie, che rappresentano diverse condizioni di errore:
- `ArithmeticError`: per gli errori aritmetici (divisione per zero, ecc...);
- `LookupError`: errori di indirizzamento e di indicizzazione;
- `TypeError`: funzioni applicate ad oggetti di tipo sbagliato;
- `ValueError`: funzioni applicate ad oggetti di tipo corretto ma valore inammissibile.

### `try ... catch`
Il Python supporta i classici blocchi `try ... catch` per la gestione delle eccezioni:
```python
try:
	# operazione rischiosa
except Eccezione1:
	# gestisci Eccezione 1
except Eccezione2:
	# gestisci Eccezione 2
# ...
```

In verità ogni eccezione rappresenta un errore, che può essere ottenuto come:
```python
except Exception as e
# si può usare e
```
e che restituisce i *dettagli* sulla situazione di errore che ha portato all'eccezione.

### Clausola `finally`
Come il Java, Python offre la clausola `finally` nei blocchi `try ... catch` che viene eseguita se un eccezione viene registrata o meno:
```python
try:
	file = open("path.txt", "r")
	content = file.read()
except FileNotFoundError:
	print("The file was not found!")
else:
	print("File was read!")
finally:
	file.close() # il file verrà sempre chiuso
```

Notiamo come nell'esempio di codice riportato si è usata la parola chiave `else` a seguito di un blocco `except` per proseguire nel caso l'eccezione non si sia verificata.
