def validacao_de_dados():
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    salario = float(input('Salario'))
    sexo = input('sexo: [f]/[m]')
    estado_civil = input('estado civil [s] [c] [v] [d]')

    validar = {
        nome: len(nome) > 3,
        idade: idade in range(151),
        salario: salario > 0,
        sexo: sexo in ['f', 'm'],
        estado_civil: estado_civil in ['s', 'c', 'v', 'd']
    }
    dados_lista = ['nome', 'idade', 'salário', 'sexo', 'estado civil']

    dados = zip(validar.items(), dados_lista)
    lista_false = list()
    for (valor, booleano), chave in dados:
        if booleano == False:
            lista_false.append(booleano)
    for _ in lista_false:
        validar = input(f'{_} invalido digite novamente: ')

    if all(p is True for p in validar.values()):
        return 'cadastrado com sucesso!!!'


validacao_de_dados()