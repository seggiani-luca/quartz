**Python** è un linguaggio di programmazione ad alto livello, orientato a oggetti, multiparadigma e *general-purpose*. Risulta adatto, tra gli altri usi, a sviluppare applicazioni distribuite, scripting, computazione numerica e system testing.
Il linguaggio supporta una vasta quantità di costrutti sintattici, e per Python sono state sviluppate una vasta gamma di librerie (native Python o wrapper per librerie C o di altri linguaggi), che lo rendono un linguaggio estremamente flessibile e versatile.

### Interpretazione
Queste caratteristiche positive sono bilanciate dal fatto che Python è interpretato (nell'implementazione più diffusa da un interprete scritto in C), soluzione che dà dei chiari *tradeoff* in termini di prestazioni.

### Indentazioni
La prima differenza che noteremo dai linguaggi a cui siamo abituati è l'uso delle *indentazioni* per delimitare il codice, anziché le parentesi graffe dei linguaggi *c-like*. Ad esempio, avremo:
```python
n = 10
for i in range(n):
	print(i) # indentazione
```
La discussione su *indentazioni* contro *spazi* è giunta in Python a preferire come delimitatore 4 spazi (Python style guide, [PEP 8](https://peps.python.org/pep-0008/)).