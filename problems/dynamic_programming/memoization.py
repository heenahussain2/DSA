import time
from functools import lru_cache

"""
Memoization - How to avoid repeating yourself
Store everything in a cache or memory
This is the Top Down approach to solving problems where a
subproblem is solved only once

Here we will implement the fibonacci function in 3 ways
1. without cache or storing the solution.
2. LRU cache
3. with a dictionary
"""


def fibonacci(n):
    """
    Returns the n-th Fibonacci number.
    """
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@lru_cache
def fib_lru(n):
    """
    Returns the n-th Fibonacci number.
    """
    if n == 0 or n == 1:
        return n
    return fib_lru(n - 1) + fib_lru(n - 2)


# Manual caching using a dictionary.
def fib_cache(n, cache=None):
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]
    if n == 0 or n == 1:
        return n
    result = fib_cache(n - 1, cache) + fib_cache(n - 2, cache)
    cache[n] = result
    return result


n = 40

start = time.perf_counter()
res = fibonacci(n)  # will take the most amount of time
end = time.perf_counter()
print("Plain recursive version. Seconds taken: {:.7f}".format(end - start))

start = time.perf_counter()
fib_lru(n)
end = time.perf_counter()
print("lru cache version. Seconds taken: {:.7f}".format(end - start))

start = time.perf_counter()
fib_cache(n)
end = time.perf_counter()
print("Manual cache version. Seconds taken: {:.7f}".format(end - start))
