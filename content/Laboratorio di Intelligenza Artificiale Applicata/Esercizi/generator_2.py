# Write a generator function prime_numbers(limit) that yields all prime numbers 
# up to a given limit

def prime_numbers(limit):
    i = 0
    primes = [1]

    while i < limit:
        if any([i % p == 0 for p in primes]):
            i += 1
        primes.append(i)
        yield i

for p in prime_numbers(10):
    print(p)
