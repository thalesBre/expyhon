valores = [5, 3, 1, 9, 6]
menor = valores[0]
maior = valores[0]
soma = valores[0]

# buscando o menor valor
for _ in valores[1:]:
    if _ < menor:
        menor = _

# buscando o maior valor
for _ in valores[1:]:
    if _ > maior:
        maior = _
# buscando soma
for _ in valores[1:]:
  soma += _

print(soma)
print(f'menor valor {menor}')
print(f'maior valor {maior}')

