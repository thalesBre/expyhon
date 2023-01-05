from statistics import mean
def colecao_cds():
    qtd_cds = int(input('Informe a quantidade de CDs : '))
    valores_cds =[]
    for i in range(qtd_cds):
        vlr_cd = float(input('valor do CD: '))
        valores_cds.append(vlr_cd)
    vlr_total = sum(valores_cds)
    media = mean(valores_cds)
    #vlr_medio = sum(valores_cds)/len(valores_cds)
    print(f'O valor total investido em Cds foi de R$ {vlr_total:.2f} e seu valor médio gasto foi R${media:.2f}.')
colecao_cds()