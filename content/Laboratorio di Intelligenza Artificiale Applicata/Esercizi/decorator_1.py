# Implement a @deprecated decorator that issues a warning when a deprecated 
# function is called 

import functools

def deprecated(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Warning! Deprecated function")
        return func(*args, **kwargs)
    return wrapper

@deprecated
def age(name):
    return input(f"Quanti hanni hai, {name}? ")

name = "Luca"
print(f"{age(name)}? Sei proprio vecchio!")
