# Given a list of numbers from 1 to 10, generate a new list with the same 
# numbers in inverted order using loops

SIZE = 10

lst = list(range(1, SIZE + 1))
siz = len(lst)

print(f"List is: {lst}")

inv = [0] * siz 
for i in range(0, siz):
    inv[i] = lst[siz - i - 1]

print(f"Inverted list is: {inv}")
