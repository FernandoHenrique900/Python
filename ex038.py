#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior
#– O segundo valor é maior
#– Não existe valor maior, os dois são iguais

a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))

if a > b:
    print('''
    -O primeiro é maior {} 
    -O segundo {} é menor '''.format(a,b))
elif a < b:
    print('''
    -O segundo é maior {}
    -O primeiro é menor {}'''.format(b,a))
else:
    print('{} é igual á {}'.format(a,b))