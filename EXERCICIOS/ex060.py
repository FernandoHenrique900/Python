#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

#jeito facil
#from math import factorial
#n = int(input('Digite um numero para calcular seu fatorial: '))
#f = factorial(n)
#print ('O fatorial de {} e {}.'.format(n, f))


n = int(input('Digite um numero para calcular seu fatorial: '))
i = n
f = 1
print('Calculando {}! = '.format(n, end=''))
while i > 0:
    print('{}'.format(i), end='')
    print(' x 'if i > 1 else ' = ', end='')
    f *= i
    i -= 1
print('{}'.format(f))
