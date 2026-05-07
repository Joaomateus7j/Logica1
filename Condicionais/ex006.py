# O Classificador de Atleta
'''
O Problema: O programa deve ler o ano de nascimento de um atleta e mostrar sua categoria de acordo com a idade.

Esse exercício simula um sistema de inscrição em uma academia ou clube esportivo.
'''

jogador = int(input('Qual e a sua idade'))

if jogador <= 14:
    print('Faixetaria de Infantil')
elif jogador <= 19:
    print('Faixetaria de Junior')
else:
    print('A faixetaria de Senior')