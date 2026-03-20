# Given a list of strings, use a list comprehension with := to collect only 
# those strings whose length (as computed by len()) exceeds 5, storing the 
# lengths alongside the strings as tuples: [(string, length), ...

strings = ["Eiffel", "Tangier", "Oran", "Damascus"]
tuples = [
    (string, length) 
    for string in strings
    if (length := len(string)) > 5
]
print(tuples)

