compras = []

while True:
    item = input('Digite um item: ')
    compras.append(item)

    continuar = input('Deseja continuar? s/n: ')

    if continuar == 'n':
        break

print('\nLista de compras:')

for item in compras:
    print(item)