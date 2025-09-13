#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
from time import sleep
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
opcao = 0
while opcao !=5:
    print ('''    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NUMEROS
    [5] SAIR DO PROGRAMA''')
    opcao = int(input('Qual e a sua opcao? '))
    if opcao == 1:
        soma = num1 + num2
        print('A soma entre {} e {} e {}'.format(num1,num2,soma))
    elif opcao == 2:
        multiplicacao = num1 * num2
        print('A multiplicacao de {} x {} e igual a {}.'.format(num1,num2,multiplicacao))
    elif opcao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('O Maior numero entre {} e {} e {}'.format(num1,num2,maior))     
    elif opcao == 4:
        print('Informe os numeros novamente: ')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo Valor: '))
    elif opcao == 5:
        
        print('Finalizando...')
    else:
        print('Opcao invalida. Tente novamente')
        sleep(3)
    print('=-=' * 10)    
print('Fim do programa! Volte sempre...')


