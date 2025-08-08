usuario_correto='admin'
senha_correta='admin'

usuario = input('Digite o usuario: ')
senha = input('Digite a senha: ')

if usuario == usuario_correto and senha == senha_correta:
    print('Login realizado com sucesso')
else:
    print('Falha no login. Tente novamente')