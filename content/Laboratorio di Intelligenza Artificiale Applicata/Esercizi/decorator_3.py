# Write a recursive function to calculate the n-element of the Fibonacci 
# sequence (fib(n) = fib(n-1) + fib(n-2); fib(0) = 0; fib(1) = 1). Write a 
# @memorize decorator that caches the output of the function. Show that the 
# resulting implementation is faster than the naive implementation

import time

TRIES = 10 # test tries
SIZE = 30  # test size

def fib_time(n):
    start = time.time()
    for i in range(n):
        fib(i)
    end = time.time()
    return end - start

f_map = {}

def memoize(func):
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key in f_map:
            return f_map[key]
        else:
            res = func(*args, **kwargs)
            f_map[key] = res
            return res
    return wrapper

@memoize
def fib(i):
    if i == 0 or i == 1:
        return 1
    return fib(i - 1) + fib(i - 2)

tries = [fib_time(SIZE) for i in range(TRIES)]
avg = sum(tries) / len(tries)

for i, time in enumerate(tries):
    print(f"Try:\t{i}, elapsed:\t{time}")
print(f"Average is {avg}")
