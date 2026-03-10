# Write a function to obtain a list from the numerical values of a dictionary
# converted into strings

def to_str(d):
    return map(lambda x: str(x), d.values())

my_dict = {
    "a": 12,    
    "b": 13,    
}

print(list(to_str(my_dict)))
