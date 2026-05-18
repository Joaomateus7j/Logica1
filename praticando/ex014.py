estoque = ['Arroz', 'Feijão', 'Macarrão']

produto = input('Digite o produto: ')

if produto in estoque:
    print('Produto disponível')
else:
    print('Produto indisponível')