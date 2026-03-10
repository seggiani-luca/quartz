# Write a function calculate(op, a, b) that: 
# - Supports the operations "+", "-", "*", and “/“ 
# - When dividing by zero it prints "Error: cannot divide by zero.” 
# - If the operator is invalid it prints "Error: unsupported operation.” 
# - If a or b are not valid numbers it prints “Error: only numbers are 
#   supported.”

from numbers import *

def calculate(op, a, b):
    allowed = {"+", "-", "*", "/"} 
    if(op not in allowed):
        raise ValueError("unsupported operation")
    if(not isinstance(a, Number) or not isinstance(b, Number)):
        raise TypeError("only numbers are supported")
    try:
        return eval(f"{a} {op} {b}")
    except ZeroDivisionError:
        raise ValueError("cannot divide by zero")

while True:
    op = input("Enter op: ")
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    print(calculate(op, a, b))
