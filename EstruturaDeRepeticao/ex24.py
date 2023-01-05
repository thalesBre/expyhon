from random import randint
def calcular_media ():
    notas_lista = [randint(1,10) for _ in range(1, 6)]
    #soma = notas_lista[0]
    for _ in notas_lista[:]:
        #soma += 1
        media = sum(notas_lista) / len(notas_lista)

    print(notas_lista,media)
calcular_media()