#O Simulador de Empréstimo

'''
O Problema: Pergunte o valor do salário de uma pessoa e o valor da prestação da casa que ela quer comprar.

A Regra de Negócio:

O empréstimo só pode ser aprovado se o valor da prestação NÃO exceder 30% do salário.

'''

salario = float(input('Qual é o seu salario mensal? '))
prestacao_casa = float(input('Qual é o valor da prestação da casa? '))

limite = salario * 0.30

print(f'O seu limite de prestação e R$ {limite}')

if prestacao_casa <= limite:
    print('Empréstimo APROVADO! Parabéns pela nova casa.')
else:
    print('Empréstimo NEGADO. A prestação excede 30% do seu salário.')


