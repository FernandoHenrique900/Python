#Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

n = cont = soma = 0
n = int(input('Digite um número [999 = sair]: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número [999 = sair]: ')) #mesmo comando inicio e fim, fazendo q a condição 999 não entre no laço do while

print('Você digitou {} números e a soma entre eles foi {}'.format(cont,soma))
 