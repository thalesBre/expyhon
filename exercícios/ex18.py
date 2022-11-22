# 18 Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
#dia, mes, ano = '33/08/2000'.split('/')
datas = '10/15/2000'.split('/')
datas = [int(_) for _ in datas]
dia, mes, ano = datas
if 0 < dia > 32:
    print('dia invalido')
elif 0 < mes > 12:
    print('mes invalido')
print(datas)