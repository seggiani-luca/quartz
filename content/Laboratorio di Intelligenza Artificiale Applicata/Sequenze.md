Le **sequenze** in Python sono collezioni *ordinate* e *posizionali*. Può essere una sequenza qualsiasi collezione che supporta:
- **Iterazione**: scorrimento in una o due direzioni della sequenza.
- **Indicizzazione**: accesso *posizionale* ad un elemento ad un certo indice.
Sono quindi sequenze le **stringhe**. Lo sono anche le **liste** e le **tuple**, ma non altre collezioni come i **dizionari**. Notiamo in particolare che tuple e stringhe sono sequenze *immutabili*, mentre le liste sono sequenze *mutabili* (per dettagli vedere [[Variabili in Python]]).

### Operazioni aggregate
Sulle sequenze sono disponibili alcune operazioni. In particolare notiamo le operazioni **aggregate**: sono disponibili funzioni come `len()`, `min()` e `max()` che operano su tutti i dati della sequenza (restituiscono rispettivamente lunghezza della sequenza, minimo e massimo secondo un dato ordinamento).

### Indicizzazione
Si possono indicizzare le sequenze attraverso la solita sintassi a parentesi quadre:
```python
seq = ["gatto", "cane", "lupo"]
print(seq[0]) # "gatto"
print(seq[4]) # errore di indicizzazione!
```