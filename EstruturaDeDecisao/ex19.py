'''19 Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades'''

def rreplace(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)

def numero(entrada: int):
    if entrada > 999:
        return '[ERRO] A entrada devera ser menor que 1000'
    elif entrada < 1:
        return '[EEO] O número precisa ser positivo'
    else:
        centenas, resto = divmod(entrada, 100)
        dezenas, resto = divmod(resto, 10)
        unidades = resto

        '''operador ternario python'''
        centenas_str = 'centenas' if centenas > 1 else 'centena'
        dezenas_str = 'dezenas' if dezenas > 1 else 'dezena'
        unidades_str = 'unidades' if unidades > 1 else 'unidade'

        lista = [centenas, dezenas, unidades]
        lista_str = [centenas_str, dezenas_str, unidades_str]

        mensagem = ''
        for count, value in enumerate(lista):
            if value > 0:
                mensagem += f'{lista[count]} {lista_str[count]}, '
        # mensagem = mensagem[:-2]
        '''altera a última ocorrência de ", " por string vazia'''
        mensagem = rreplace(mensagem, ', ', '', 1)

    return f"{entrada} = {rreplace(mensagem, ', ', ' e ', 1)}"
numero(456)