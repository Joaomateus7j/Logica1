# Sistema que soma notas de alunos

soma = 0

for i in range(1, 6):
    nota = float(input(f'Digite a nota do aluno {i}: '))
    soma += nota

media = soma / 5

print(f'\nA média da turma foi: {media:.2f}')