pais_a = 80000
pais_b = 200000
cont = 0
while pais_a <= pais_b:
    pais_a += pais_a * 0.3
    pais_b += pais_b * 0.015
    cont += 1
print(f'pais A ultrapassa ou iguala o Pais B em {cont} anos')
