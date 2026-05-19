notas = []

for i in range(5):

    nota = float(input('Digite a nota: '))
    notas.append(nota)

media = sum(notas) / len(notas)

print(f'Média da turma: {media}')