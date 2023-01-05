'''Lojas Tabajara
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00
...'''


def conveniencia():
    preco_mercadoria = []
    # produtos_dict = {}
    while True:
        preco = float(input('Digite o preço do produto: R$ '))
        if preco not in [-1, 0]:
            preco_mercadoria.append(preco)
            # produtos_dict[]
        elif preco == 0:
            total = sum(preco_mercadoria)
            print(f'O total da sua compra foi {total}')
            break
    dinheiro = float(input('valor da cedula que o cliente forneceu : '))
    troco = dinheiro - total
    print(f'O seu troco será de {troco:.2f}')
    print(preco_mercadoria)
    opcao = input('quer continuar S/N: ').upper().strip()[0]
    if opcao in 'S':
        conveniencia()
    else:
        print('volte sempre')
        for _ in range(len(preco_mercadoria)):
            print(f'Produto {_+1}: R$: {preco_mercadoria[_]:.2f}')
conveniencia()