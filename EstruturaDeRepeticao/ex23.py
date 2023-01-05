'''23 - Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa
deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.'''

num = int(input('digite um numero: '))
cont = 0
for c in range(1, num+1):
    if num % c == 0:
        cont += 1
        print(c)
if cont == 2:
    print('esse numero é primo pois se dividido somente por um oupor ele mesmo')
else:
    print(f'esse não é primo pois foi dividido {cont} vezes por esses numeros {c}')