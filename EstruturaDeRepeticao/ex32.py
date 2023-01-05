num = int(input('qual fatorial: '))
contador = 1
numero = 1

while contador <= num:
    numero *= contador
    contador += 1
print(numero)