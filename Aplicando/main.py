# O Verificador de Login

nome_na_lista = 'João, mateus, vitor'
lista_de_espera = 'Gabriel, Algusto, Miguel'

quem_chegou = input('Digite seu nome para entrar: ')

if quem_chegou in nome_na_lista:
    print('Acesso Liberado! Pode entra. ')
elif quem_chegou in lista_de_espera:
    print('Seu nome esta na lista de espera, Aguarde!')
else:
    print('Acesso Negado. Você não está na lista. ')