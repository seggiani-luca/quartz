# Implement a @retry(n) decorator that retries a function up to n times if it 
# raises an exception

import functools
import random

def retry(n=1):
    def decorator(func):
        @functools.wraps(func) 
        def wrapper(*args, **kwargs):
            for _ in range(n):
                try:
                    yield func(*args, **kwargs)
                    return
                except Exception as e:
                    yield e
            return None 
        return wrapper
    return decorator

@retry(6)
def mule(n):
    for _ in range(n):
        if random.random() > 0.75:
            raise Exception("Il mulo si è bloccato")
    return "Il mulo è arrivato in cima alla salita"

for trie in mule(5):
    print(trie)
