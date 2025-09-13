
from random import randint
computador = randint(0,10)
print ('Sou eu, o seu computador...Acabei de pensar em um numero entre 0 e 10.')
print('Sera que vc consegue advinhar qual foi ?')
acertou = False
palpites = 0
while not acertou:
    jogador = int (input('Qual e seu palpite?'))
    palpites +=1
    if jogador == computador:
        acertou = True
#logica para classificar se esta mais perto do valor    
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print ('Acertou com {} tentativas. Parabens!.'.format(palpites)) 