Le [[Sequenze]] in [[Python]] presentano un operatore di indicizzazione che supporta anche lo **slicing**. In particolare, usando la sintassi basata sui due punti, si può prendere una sottosequenza con i bound forniti. L'omissione del bound prende di default l'inizio della sequenza a sinistra e la fine a destra. Ad esempio:
```python
s = "Questa è una stringa"
s[2:5] # "est"
s[:-1] # "Questa è una string"
```

### Stride
L'operatore di slicing può prendere un altro parametro detto *stride*, che indica quanti caratteri saltare ad ogni iterazione. Vediamo alcuni esempi:
```python
lista = ["banana", "mela", "avocado"]
lista[0:-1:1] # "banana", "avocado", "mela"
lista[0::2] # "banana", "avocado"
```

Notiamo che la sintassi dello slicing ricorda quella della funzione `range()` usata ad esempio nei loop [[For]]:
```python
for i in range(1, 5, 2):
	pass # vedrà 1, 3
```