from functools import lru_cache

@lru_cache(maxsize=1000)
def fibonacci(n):
    if n == 1:
     #   value = 1
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        while value < 500:
            value = fibonacci(n - 1) + fibonacci(n - 2)
        return value
fibonacci(16)