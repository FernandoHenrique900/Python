#Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = int(input('Qual o primeiro valor: '))
b = int(input('Qual o segundo valor: '))
c = int(input('Qual o terceiro valor: '))
#VERIFICANDO QUEM É O MENOR, JÁ PRÉ-SUPONDO QUE SEJA O "A" - PRIMEIRO

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

#TESTANDO MAIOR VALOR PRÉ-SUPONDO QUE SEJA O "A" - PRIMEIRO
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O Menor valor é {}'.format(menor))
print('O Maior valor é {}'.format(maior))