'''26. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.'''

def posto():

    litro = float(input('litros: '))
    combustivel = input('digite : [A] para Álcool [G] Gasolina: ').upper().strip()[0]
    if combustivel == 'A':
        preco = litro * 1.90
        desconto = preco * 0.03 if litro <= 20 else preco * 0.05

    elif combustivel == 'G':
        preco = litro * 2.50
        desconto = preco * 0.04 if litro <= 20 else preco * 0.06

    preco_final = preco - desconto
    print(preco_final)
posto()