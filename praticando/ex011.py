convidados = []

for i in range(5):

    nome = input('Digite o nome do convidado: ')
    convidados.append(nome)

print('\nConvidados cadastrados:')

for convidado in convidados:
    print(convidado)