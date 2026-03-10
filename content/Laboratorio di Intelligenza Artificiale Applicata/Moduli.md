I moduli sono il meccanismo per l'organizzazione del codice del [[Python]]. In particolare, ogni file Python è un modulo, che definisce classi, variabili e funzioni (*pubbliche* di default). 

Per importare un modulo si può usare la parola chiave `import`:
```python
import HalalDetector
```

Si possono impostare alias per i moduli importati, con la parola chiave `as`:
```python
import HalalDetector as hd
```

### Pacchetti
Un **pacchetto** in Python non è altro che una directory contenente moduli. Si possono importare moduli dai pacchetti attraverso la parola chiave `from`:
```python
from quran import HalalDetector as hd
from quran import * # importa tutti i moduli del pacchetto
```

Per creare un pacchetto basta mettere tutti i moduli in una directory. Di default, tutti questi possono essere importati dal pacchetto. Esiste un file speciale, cioè il file `__init__.py`, che server a marchiare la directory come pacchetto Python, e dove si possono specificare quali file possono essere importati come moduli.

La struttura di un `__init__.py` è la seguente:
```python
print("Initializing my_package)
# configura il pacchetto, eseguito a tempo di importazione

__all__ = ["module1"] # esibisci il pacchetto modul1
```

Come abbiamo detto, `__init__.py` può anche essere vuoto, e in tal caso marchia solo una directory come pacchetto. Grazie a questo meccanismo, si possono definire i nostri algoritmi privati come file Python all'interno di una directory, e quindi esibire solo i moduli pubblici in `__all__`. Solitamente si prefiggono gli oggetti e le funzioni private col carattere `_`.

### Pacchetti utili
Vediamo una lista di pacchetti [[Python]] che ci torneranno utili.
- `os`: contiene hook per le funzioni del sistema operativo come `chdir`, `getcwd`, ecc...
- `shutil`: supporto di alto livello per la copia e lo spostamento di file;
- `glob`: cerca file usando un meccanismo simile a quello della shell Unix (con le wildcard);
- `math`: matematica di base, simile al `math.h` del C;
- `random`: gestisce la casualità, permette di generare numeri casuali, e attraverso `choice` selezionare elementi casuali da liste;
- `statistics`: elementi base di statistica, che opera su [[Liste]]. Permette di calcolare valori come media, mediana, ecc...
- `time`: permette di prelevare il tempo attuale, ecc...