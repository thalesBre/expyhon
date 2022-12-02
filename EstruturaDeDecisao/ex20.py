'''20. Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.'''
notas_aluno = []
for _ in range(3):
    nota = int(input(f'nota {_ + 1}: ' ))
    notas_aluno.append(nota)
media = sum(notas_aluno) / 3
print(media)
if media > 7 and media < 10:
    print(f'Sua média foi {media} [APROVADO]')
elif media < 7:
    print(f'Sua média foi {media} [REPROVADO]')
elif media == 10:
    print(f'sua media foi {media} [APROVADO COM DISTINÇÃO]')
