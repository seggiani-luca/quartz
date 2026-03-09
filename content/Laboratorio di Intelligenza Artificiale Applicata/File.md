La gestione dei **file** in [[Python]] è analoga a quella dei linguaggi della famiglia C/C++, ma di molto semplificata. Quindi abbiamo le solite funzioni `open()`, `read()`, `write()`, e `close()`.

### `open`
La `open()` prende come argomento il percorso del file e un a lettera che indica la modalità. Questa può essere:
- `r`: lettura;
- `w`: scrittura;
- `rw`: lettura + scrittura;
- `a`: lettura in append;
- ecc...

### `read`
La `read()` ci permette di leggere i file in maniera molto veloce. L'intero contenuto del file viene infatti restituito come stringa:
```python
f = open("mio_file.txt", "r")
content = f.read() # il file è in content
```
Nel caso questo non fosse molto agibile, esiste la `readlines()`, che restituisce una riga per volta:
```python
f = open("mio_file.txt", "r")
lines = f.readlines();
for line in lines:
    # vediamo linea per linea del file
```

### `write`
Si può scrivere sui file semplicemente con la `write()`:
```python
f = open("mio_file.txt", "w")
f.write("qualcosa") // scrive qualcosa nel file
```
La modalità di scrittura della `write` dipende da come si è aperto il file (`r` sovrascrive, `a` concatena).

### Blocco with as
Per la gestione degli errori di IO nella gestione dei file è fornito il blocco `with ... as ...`. 
```python
with open("mio_file.txt", "w") as f:
	# qui possiamo usare il file 
# qui il file viene liberato
```
Questo permette di ottenere la chiamata automatica della `close()` alla fine del blocco che gestisce il file, nonché la gestione delle eccezioni durante la gestione dello stesso. In particolare, esistono due funzioni *nascoste* di `open()`:
- `__enter__()`: acquisisce la risorsa file e la restituisce;
- `__exit__()`: libera la risorsa file.
Quello che fa il blocco `with ... as ...` è chiamare automaticamente tali funzioni.