# Given a list of numbers from 1 to 10, create a new list of odd numbers only 
# using comprehensions

SIZE = 10

lst = list(range(1, SIZE + 1))
siz = len(lst)

print(f"List is: {lst}")

odd = [i for i in lst if i % 2 != 0]

print(f"Odd list is: {odd}")
