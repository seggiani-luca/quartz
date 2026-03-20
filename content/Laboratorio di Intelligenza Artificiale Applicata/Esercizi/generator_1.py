# Create a generator function fibonacci(n) that yields the first n Fibonacci 
# numbers

# iterative
def fibonacci_iter(n):
    a, b = 0, 1 # state
    i = 0       # counter
    
    while True:
        yield a
        
        # update state
        a, b = a + b, a
        
        # update counter 
        i += 1
        if i >= n:
           return 

# tail recursion (no real recursion possible)
def fibonacci_recu(n, a=0, b=1):
    # base case
    if n == 0:
        return

    yield a
    
    # recurse
    yield from fibonacci_recu(n - 1, a + b, a) 

for f in fibonacci_recu(10):
    print(f)
