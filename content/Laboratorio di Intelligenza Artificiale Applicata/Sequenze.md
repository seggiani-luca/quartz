Le **sequenze** in Python sono [[Collezioni]] *ordinate* e *posizionali*. Può essere una sequenza qualsiasi collezione che supporta:
- **Iterazione**: scorrimento in una o due direzioni della sequenza.
- **Indicizzazione**: accesso *posizionale* ad un elemento ad un certo indice.
Sono quindi sequenze le **stringhe**. Lo sono anche le [[Liste]] e le [[Tuple]], ma non altre collezioni come i [[Dizionari]] e gli [[Insiemi]] (che permettono solo l'indicizzazione con chiavi non necessariamente numeriche, caratteristica comune a tutte le [[Collezioni]]). Notiamo in particolare che tuple e stringhe sono sequenze *immutabili*, mentre le liste sono sequenze *mutabili* (per dettagli vedere [[Variabili in Python]], e ancora [[Collezioni]]).

### Operazioni aggregate
Sulle sequenze sono disponibili alcune operazioni. In particolare notiamo le operazioni **aggregate**: sono disponibili funzioni come `len()`, `min()` e `max()` che operano su tutti i dati della sequenza (restituiscono rispettivamente lunghezza della sequenza, minimo e massimo secondo un dato ordinamento).

### Indicizzazione
Si possono indicizzare le sequenze attraverso la solita sintassi a parentesi quadre:
```python
seq = ["gatto", "cane", "lupo"]
print(seq[0]) # "gatto"
print(seq[4]) # errore di indicizzazione!
```
L'operatore di indicizzazione permette di fornire indici negativi. In questo caso questi verranno sottratti dalla lunghezza della sequenza. Ad esempio:
```python
seq = ["alfa", "beta", "gamma"]
print(seq[-1]) # "gamma"
```
Ulteriori operazioni sulle sequenze possono essere fatte sfruttando le proprietà di [[Slicing]].