# Como lidar com mais que 2 condições?
'''
Eu cheguei atrasado na aula. Ainda posso entrar?

Se for a primeira ou segunda vez você chega atrasado, pode sim.
Mas se for a terceira vez, Você será suspenso.
'''

atrasos = float(input('Quantas faltas você possui?'))

if atrasos >= 3:
    print('Você esta suspenso!')
elif atrasos == 2:
    print('Mais uma falta e estará suspenso')
elif atrasos == 1:
    print('Mais duas faltas e estará suspenso')
else:
    print('Você não possui nenhuma falta, pode entrar.')