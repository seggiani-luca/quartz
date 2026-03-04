Abbiamo accennato alle **collezioni** in [[Python]] quando stavamo parlando delle [[Variabili in Python]]. In generale, una collezione è un insieme di elementi variegati raggruppati secondo un qualche schema (indicizzati, attraverso hash, ecc...). Diverse collezioni sono adatte a scopi diversi.

In generale, le collezioni in Python appartengono a 4 tipi di default, distinti secondo le seguenti caratteristiche ortogonali:
- **Indicizzabilità**: la capacita di, appunto, *indicizzare* gli elementi, cioè individuarli attraverso indici numerici o meno (abbiamo visto che le [[Sequenze]] offrono un operatore di indicizzazione). Possiamo dire che l'indicizzabilità definisce la possibilità degli elementi di una collezione di essere **ordinati**. Vedremo che [[Dizionari]] ed [[Insiemi]] sono le collezioni *non ordinate* del Python. 
- **Mutabilità**: l'abbiamo vista nel dettaglio in [[Mutabilità]], in breve si riferisce alla possibilità di modificare gli elementi di una collezione dopo che questa viene creata;
- La possibilità di avere **duplicati**: questo è chiaro dal fatto che strutture come le mappe hash (che formano i [[Dizionari]]) sono *associative*, cioè associano valori a chiavi (non contengono collezioni arbitrarie di chiavi, possibilmente duplicate);
Notiamo inoltre che le collezioni in Python sono generalmente *variegate*, cioè possono contenere elementi di tipo diverso fra di loro nello stesso contenitore. 

### Tipi di collezioni
Vediamo quindi, come avevamo introdotto in [[Variabili in Python]], i tipi di collezioni che il linguaggio offre:
- [[Liste]]: rappresentate da array dinamiche (non linked list), sono *indicizzabili*, *mutabili* e *permettono* duplicati;
- [[Dizionari]]: rappresentati da tabelle hash, formano *associazioni* fra **chiavi** e **valori**. Sono *indicizzabili* attraverso le chiavi, *mutabili* e *non permettono* duplicati (almeno alle chiavi, nessuno ci vieta di duplicare valori);
- [[Tuple]]: sono liste con elementi variegati e *immutabili*. *Permettono* di avere elementi duplicati. A differenza delle liste, possono essere usate come record di dizionari;
- [[Insiemi]]: rappresentati ancora da tabelle hash (sono effettivamente dizionari verso booleani), rappresentano oggetti sulla base della loro appartenenza o meno all'insieme. Per questo motivo, come i dizionari, sono *mutabili* e *non permettono* duplicati. Notiamo che, a differenza dei dizionari, non possono essere indicizzati (si usa l'operatore `in` per valutare l'appartenenza);

Possiamo riassumere le caratteristiche delle collezioni nella seguente tabella:

| Tipo    | Indicizzabile | Mutabile | Duplicati           |
| ------- | ------------- | -------- | ------------------- |
| `list`  | Si            | Si       | Si                  |
| `tuple` | Si            | No       | Si                  |
| `set`   | No            | Si       | No                  |
| `dict`  | Si            | Si       | Si *(per i valori)* |
