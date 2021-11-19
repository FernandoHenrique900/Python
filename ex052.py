#Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n=int(input('Digite um numero inteiro e descubra se ele é primo: '))
tot = 0
for i in range(1,n + 1):
    if n % i == 0:
        print('\033[33m', end=' ')
        tot +=1 
    else:
        print('\033[31m', end=' ')
    print('{}'.format(i), end=' ')
print('\n\033[m0 numero {} foi divisivel {} vezes'.format(n, tot))
if tot == 2:
    print('Devido a isso ele e primo!')
else:
    print('Devido a isso ele nao e primo!')