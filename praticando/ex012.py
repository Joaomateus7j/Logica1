medias = []

for i in range(3):

    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Segunda nota: '))

    media = (nota1 + nota2) / 2
    medias.append(media)

print('\nMédias:')

for media in medias:

    print(media)

    if media >= 7:
        print('Aprovado')
    else:
        print('Reprovado')