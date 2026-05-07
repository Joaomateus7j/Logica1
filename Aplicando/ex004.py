# Desafio: Sistema de Categoria de Atleta 

nome = input('Poderia dizer o seu nome')
experiencia = input('qual o nível de experiência entre (Basico, Intermediario. Avancado): ').lower()

if experiencia == 'basico':
    print(f'{nome}, você está na fase de adaptação. Foco na técnica! ')
elif experiencia == 'intermediario':
    print(f'{nome}, hora de aumentar a intensidade e a carga! ')
elif experiencia == 'avancado':
    print(f'{nome}, você atingiu o nível de performance. Continue focado! ')
else:
    print('Nível não reconhecido. Tente digitar Basico, Intermediario ou Avancado. ')