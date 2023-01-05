def lojinha_um_real():
    qtd_produtos =int (input('Digite  a quantidade de produtos: '))
    vlr_produto = 1.99
    if qtd_produtos <= 50:
        print('Lojas Quase Dois - Tabela de preços')
        for item in range(1,qtd_produtos+1):
            print(f'{item} - {vlr_produto} = R$ {item * vlr_produto}')
    else:

        print('precisa ate  50 itens')
lojinha_um_real()