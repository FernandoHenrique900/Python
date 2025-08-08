#Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint #BIBLIOTECA DE RANDON
from time import sleep   #BIBLIOTECA DE TIMER

computador = randint(0,5) 

print('=*=*' * 15)
print('Vou pensar em um número entre 0 e 5. Tenta adivinhar...')
print('=*=*' * 15)

jogador = int(input('Em que número eu pensei "?')) #USUARIO TENTANDO ADIVINHAR

print ('PROCESSANDO...')
sleep(1)

if jogador == computador:
    print('Parabéns! Você teve sorte e venceu a máquina')
else:
    print('Deu ruim! Você perdeu')
