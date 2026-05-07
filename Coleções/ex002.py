notas = []

for i in range(4):
    nota = float(input(f'Digite a nota {i + 1}: '))
    notas.append(nota)

print('\nNotas digitadas:')
for nota in notas:
    print(nota)

media = sum(notas) / len(notas)

print(f'\nMédia final: {media:.2f}')