# Given a tuple of ints, remove the char and substitute with the missing int

tup = (1, 2, 3, 's', 5, 6, 7)
idx = 3

print(f"Tuple is: {tup}")

new_tup = tup[:idx] + (idx + 1,) + tup[idx+1:] 

print(f"New tuple is: {new_tup}")
