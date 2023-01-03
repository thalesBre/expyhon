from random import randint
num_lista = [randint(0,10) for num in range(0,5)]
maior = num_lista[0]
for _ in num_lista:
    if maior < _:
        maior = num_lista[1]