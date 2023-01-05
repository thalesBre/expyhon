from random import randint
idades_lista = [randint(0,100) for _ in range(1,10) ]
for _ in idades_lista[:]:
    media = sum(idades_lista)/len(idades_lista)
if media < 25:
    print('VOCÊS SÃO JOVENS AINDA!!')
elif media > 60:
    print('idosos !!')
elif media >= 25:
    print('ADULTOS!!')

print(idades_lista, media)