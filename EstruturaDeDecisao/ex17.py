## ESTRUTURA DE DECISAO PYTHON BRASIL ##
# 17 Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

for _ in range(5):
    from datetime import date
    ano = int(input('qual ano? '))
    if ano == 0:
        ano = date.today().year
    # ocorrendo a cada quatro anos. Exceto anos múltiplos de 100 que não são múltiplos de 400
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f'o ano {ano} é  bissexto')
    else:
        print(f'o ano {ano} não é bissexto')
        
