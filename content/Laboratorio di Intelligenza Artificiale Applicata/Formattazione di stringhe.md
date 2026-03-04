[[Python]] permette di concatenare stringhe con il solito operatore `+`:
```pyton
name = input("Inserisci il tuo nome")
print("Ciao " + name + "!")
```
In verità, ogni oggetto di default può sempre essere trasformato in stringa. ad esempio abbiamo visto gli interi:
```python
age = input("Quanti hanni hai?")
print("Porti molto bene i tuoi " + str(age) + " anni!")
```
dove abbiamo bisogno di effettuare il cast esplicito con `str()` per rendere disponibile l'operatore `+`.

### Funzione format()
La formattazione delle stringhe è più semplice se si usa la funzione `format()`, dal formato simile a quello della `printf()` del C:
```python
name = "Luca"
age = 21

print("Ciao {} di età {})".format(name, age));

# oppure
print("Ciao {0} di età {1})".format(name, age));
```
Notiamo che la differenza dal C sta nel fatto che la funzione è specificata come membro dell'oggetto stringa, e non come una funzione globale a parte.

### F-stringhe
Un'altra soluzione offerta dalla versioni più recenti di Python è quella delle **f-stringhe**, prefissate dal carattere `f`, dove le espressioni da convertire in stringa vengono riportate direttamente fra parentesi graffe all'interno della stringa:
```python
english = 78
maths = 55

print(f"Il tuo voto è {english + maths}")
```