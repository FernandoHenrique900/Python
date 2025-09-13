#Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    n = int(input("Quer ver a tabuada de qual valor?(valor negativo p0/ sair): "))
    print('-' * 30)
    if n < 0:
        break #FORCANDO USAR O BREAK
    for c in range(0,10,1):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
print('Programa de taboada encerrado.')

'''
SEM USAR O BREAK PROPOSTO PELO EXERCICIO COM O MESMO RESULTADO
n=0
while n >= 0:
    n = int(input("Quer ver a tabuada de qual valor?(valor negativo p0/ sair): "))
    print('-' * 30)
    if n > 0:
        for c in range(0,10,1):
            print(f'{n} x {c} = {n*c}')
        print('-' * 30)
print('Programa de taboada encerrado.')
'''