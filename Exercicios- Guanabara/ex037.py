#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input("Digite um número inteiro: "))

print('''Escolha uma das bases para conversão: 
[1] Converter para BINÁRIO 
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    #bin é um conversor direto do python
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)))
elif opcao ==2:
    #oct é um conversor direto do python
    print('{} convertido para BINÁRIO é igual a {}'.format(num, oct(num)))
elif opcao ==3:
     #hex é um conversor direto do python
    print('{} convertido para BINÁRIO é igual a {}'.format(num, hex(num)))
else:
    print('Opção inválida.Escalha umas das bases opcionais de 1 á 3')