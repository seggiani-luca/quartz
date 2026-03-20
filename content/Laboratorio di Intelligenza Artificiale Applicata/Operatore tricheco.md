![Tricheco|800](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.orlandosentinel.com%2Fwp-content%2Fuploads%2Fmigration%2F2019%2F07%2F16%2FXMN3JFI6YJA5HDELIEDSI5RHK4.jpg&f=1&nofb=1&ipt=56c1f958afcc717830544bd6b50f901c6cca20ac86b8a92c03cb529e813f16fe)

L'assegnamento in [[Python]] non è un espressione, ma uno statement. In altre parole, il simbolo `=` non rappresenta un *operatore* (utilizzabile in espressioni arbitrarie), ma segnala uno *statement* (appunto, lo statement di assegnamento), in un contesto fisso.

Se si volesse avere un espressione che effettua un assegnamento e quindi restituisce il valore assegnato, come in altri linguaggi fra cui ad esempio il C/C++, l'`=` non sarebbe allora lo strumento adatto.

Per ovviare a questo problema, il [[Python]] offre il cosiddetto *walrus operator*, o **operatore tricheco**, indicato come `:=` (che ricorda vagamente un tricheco con due denti sporgenti). Questo rappresenta un operatore vero e proprio, che assegna il valore destro al valore sinistro, restituendo il nuovo valore assegnato.

Ricordiamo quindi alcune linee guida per l'utilizzo di questo operatore. Conviene usarlo quando:
- elimina calcoli ridondanti;
- riduce violazioni del principio **DRY** (*Don't Repeat Yourself*) nei cicli;
- semplifica i pattern dei cicli `while`;
- lo scope della variabile è chiaro;
mentre è sconsigliato nei casi in cui:
- una semplice assegnazione sarebbe più chiara;
- rende una riga eccessivamente complessa;
- peggiora la leggibilità senza reali vantaggi;
- si finisce per utilizzare operatori tricheco annidati.
In genere, l'operatore tricheco è una concessione che il Python ci fa, solo nei casi in cui ci aiuta a rispettare lo [[Zen di Python]].

### Nei `while`
L'operatore tricheco risulta particolarmente utile nei cicli `while`, usandolo come si farebbe in C:

```python
# senza operatore tricheco (:=)
line = input("Enter text: ")
while line != "quit":
	print(f"You said: {line}")
	line = input("Enter text: ")

# con operatore tricheco (:=)
while (line := input("Enter: ")) != "quit":
	print(f"You said: {line}")
```

In questo caso si ha che la sintassi è molto più compatta e comprensibile.

### Nelle [[List comprehension]]
Nelle [[List comprehension]], l'operatore tricheco permette di risparmiare chiamate a funzione inutile all'interno della (già ristretta) sintassi:
```python
# senza operatore tricheco (:=)
results = [compute(x) for x in data if compute(x) > threshold]

# con operatore tricheco (:=)
results = [y for x in data if (y := compute(x)) > threshold]
```

### Negli `if`
Infine, notiamo l'esempio di utilizzo dell'operatore tricheco per calcolare valori direttamente nei blocchi condizione degli if (caso simile al precedente):

```python
env = os.environ
if (db := env.get("DATABASE_URL")): # db creato qui
	connect(db)
elif (db := env.get("DB_FALLBACK")): # idem
	connect(db)
else:
	raise RuntimeError("No DB")
```

Una cosa importante da notare in questo contesto è che, a differenza delle altre variabili di blocco, le variabili assegnate dall'operatore tricheco fuoriescono all'interno dello scope di visibilità esterno (vedere [[Funzioni#Visibilità]]). Questo vale anche per l'operatore tricheco nelle [[List comprehension]] (paragrafo precedente).