#Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

#OBS:considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

from math import ceil


print('=' * 40)
print('           BANCO DIGITAL           ')
print('=' * 40)

valor = int(input('Qual valor você deseja sacar? R$'))
total = valor
cedula = 50
totcedula = 0
#VAI EXTRAINDO O VALOR DA CEDULA DO TOTAL ATÉ ZERAR #PUNK
while True:
    if total >= cedula:
        total -= cedula
        totcedula +=1
    else:
        if totcedula > 0:
            print(f'Total de {totcedula} cedulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totcedula = 0
        if total == 0:
            break