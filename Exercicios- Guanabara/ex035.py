#Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('-=' * 15)
print('Analisador de triângulos')
print('-=' * 15) 
r1 = float(input('Digite o primeiro seguimento: '))
r2 = float(input('Digite o segundo seguimento: '))
r3 = float(input('Digite o terceiro seguimento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos de reta R1:{}, R2:{} e R3:{} PODEM fomrmar um triângulo'. format(r1,r2,r3))
    if r1 == r2 == r3:
        print('EQUILATERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os seguimentos de reta R1:{}, R2:{} e R3:{} NÃO fomrmam um triângulo'. format(r1,r2,r3))


#elif r1==r2 and r1==r3:
    #print('Os seguimentos de reta R1:{}, R2:{} e R3:{}  fomrmam um triângulo ISOCELES'. format(r1,r2,r3))