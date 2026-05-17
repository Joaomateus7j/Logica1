usuario_correto = 'mateus'
senha_correta = '1234'

usuario = input('Usuário: ')
senha = input('Senha: ')

if usuario == usuario_correto and senha == senha_correta:
    print('Login realizado')
else:
    print('Usuário ou senha incorretos')