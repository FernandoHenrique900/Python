#Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
anoAtual = date.today().year
maior = 0
menor = 0
for i in range (1,8):
    ano = int(input('Em que ano a {}ª pessoa nasceu ? '.format(i)))
    idade = anoAtual - ano
    if idade >= 18:
        maior +=1
    else:
        menor +=1
print('Temos {} maiores e {} menores'.format(maior,menor))
