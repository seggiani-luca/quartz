# Write a Python script to print a dictionary where the keys are numbers 
# between 1 and 15 (both included) and the values are square of keys

MAX = 15

d = {i: i * i for i in range(1, MAX + 1)}
print(f"Dictionary is: {d}")
