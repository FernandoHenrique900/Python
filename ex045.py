#Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.


from random import randint
from time import sleep
itens =('Pedra','Papel','Tesoura')
computador = randint(0,2)

print('''Suas opções: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jogador = int(input('Qual a sua Jogada? '))

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ !!!')
sleep(0.5)

print('-=' * 15)
print('A Máquina foi de {}'.format(itens[computador]))
print('O Jogador foi de {}'.format(itens[jogador]))
print('-=' * 15)

if computador == 0: # COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2: 
       print('COMPUTADOR VENCE')
    else:
        print ('JOGADA INVÁLIDA!')

elif computador == 1: # COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print ('JOGADA INVÁLIDA!')

elif computador == 2: # COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print ('JOGADA INVÁLIDA!')
