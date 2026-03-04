# Given a set of mixed types, create a list that contains all the types without
# repetition

mixed = {1, "hello", 3.14, 15, (2, 3), True, False}
print(f"Mixed set is: {mixed}")

types = list({type(item) for item in mixed})
print(f"List of unique types is: {types}")
