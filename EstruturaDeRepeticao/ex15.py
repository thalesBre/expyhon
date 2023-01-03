cache = {}
def fibonacci(n):
    if n in cache:
        return cache[n]
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)
    if value > 500:
        return value

    cache[n] = value
    return value

for n in range(1, 21):
    print(n , fibonacci(n))