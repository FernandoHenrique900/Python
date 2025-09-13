#Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint

print('=-' * 20)
print('VAMOS JOGAR PAR OU IMPAR')

v=0
while True:
    player = int(input('Diga um valor: '))
    npc = randint(0,10)
    total = player + npc
    choice =' '
    while choice not in 'PI':
        choice = str(input('Par ou ímpar? [P/I]: ')).strip().upper()[0]
    
    print(f'Voce jogou {player} e o computador {npc}.Total de {total}')

    if choice == 'P':
        if total%2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif choice =='I':
        if total%2== 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
    
print(f'GAME OVER! Você vencen {v} vezes.')
    
