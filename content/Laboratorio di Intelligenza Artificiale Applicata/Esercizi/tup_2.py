# Repeat the previous example but this time you don't know where the char is. 
# tup = (1,2,3,'s',5,'b',7,'k',9,10,'d',12)

tup = (1, 2, 3, 's', 5, 'b', 7, 'k', 9, 10, 'd', 12)

print(f"Tuple is: {tup}")

new_tup = [val if type(val) is int else idx + 1 for idx, val in enumerate(tup)]

print(f"New tuple is: {new_tup}")
