num = int(input('digite um numero: '))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        cont += 1
        print(c)
if cont == 2:
    print('esse numero é primo pois se dividido somente por um oupor ele mesmo')
else:
    print(f'esse não é primo pois foi dividido {cont} vezes por esses numeros {c}')


def primo(numero):
    cont = 0
    for c in range(1, numero + 1):
        if numero % c == 0:
            cont += 1
    return cont


numero = int(input('digite um numero: '))
# for n in range(1, numero + 1):
# numeros_list.append(n)
numeros_list = [n for n in range(1, numero + 1)]
primos = []
for n in numeros_list:
    cont = primo(n)
    if cont == 2:
        primos.append(n)

print(primos)

primo(10)