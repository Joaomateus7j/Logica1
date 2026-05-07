# Desafio: O Assistente de treino
# O objetivo é criar um sistema que sugere um treino baseado no objetivo do usuário.

# O Assistente de Treino

nome = input('Qual o seu nome? ')
print(f'Olá {nome}, vamos montar seu treino de hoje!')

# Usamos o .lower() para aceitar "Emagrecer", "emagrecer" ou "EMAGRECER"
objetivo = input('Qual seu objetivo hoje? (Emagrecer ou Hipertrofia): ').lower()

if objetivo == 'emagrecer':
    print(f'Foco total, {nome}! Hoje o treino será Cardio e exercícios de alta intensidade (HIIT)!')
elif objetivo == 'hipertrofia':
    print(f'Dia de peso, {nome}! O foco hoje é treino de força e cargas pesadas. Vamos crescer!')
else:
    print('Objetivo não reconhecido. Por favor, digite "Emagrecer" ou "Hipertrofia".')