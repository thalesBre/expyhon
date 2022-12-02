'''28. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.'''

def mercado(tipo_de_carne: str, quantidade_kg: int, forma_de_pagamento: str):
    tipos_de_carne = ['filé duplo', 'alcatra', 'picanha']

    if quantidade_kg <= 5:
        preco_file = quantidade_kg * 4.90
        preco_alcatra = quantidade_kg * 5.90
        preco_picanha = quantidade_kg * 6.90
    else:
        preco_file = quantidade_kg * 5.80
        preco_alcatra = quantidade_kg * 6.80
        preco_picanha = quantidade_kg * 7.80

    precos_carnes = [preco_file, preco_alcatra, preco_picanha]

    precos_zip = list(zip(tipos_de_carne, precos_carnes))
    tipos_e_precos = dict(precos_zip)

    preco_sem_desconto = tipos_e_precos.get(tipos_de_carne, 0) * quantidade_kg

    if forma_de_pagamento == 'sim':
        desconto = preco_sem_desconto * 0.05
        valor_desconto = preco_sem_desconto - desconto
        print(valor_desconto)
    elif forma_de_pagamento == 'nao':
        print(preco_sem_desconto)


mercado('filé duplo', 4, 'sim')