#Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('GERADOR DE PA')
print('=-=' * 10)
termoInicial = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão da PA: '))
cont = 1
while cont <= 10:
    print('{} -> '.format(termoInicial), end='')
    termoInicial += razao
    cont +=1
print('FIM')