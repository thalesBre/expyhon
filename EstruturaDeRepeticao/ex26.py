def media_alunos_por_turma():
    turmas = int(input('Digite a quantidade de turmas: '))
    media_alunos= 0
    qtd_alunos = []
    for _ in range(turmas):
        alunos = int(input('Digite a quantidade de alunos por turmas: '))
        if alunos >= 40:
            print('Quantidade de aluno não permitida!')
            break
        else:
            qtd_alunos.append(alunos)
    media_alunos = int(sum(qtd_alunos)/len(qtd_alunos))
    print(qtd_alunos)
    print(f'A média de alunos  por turma')