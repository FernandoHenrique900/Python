#Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

#– EQUILÁTERO: todos os lados iguais

#– ISÓSCELES: dois lados iguais, um diferente

#– ESCALENO: todos os lados diferentes

print('-=' * 15)
print('Analisador de triângulos')
print('-=' * 15) 
r1 = float(input('Digite o primeiro seguimento: '))
r2 = float(input('Digite o segundo seguimento: '))
r3 = float(input('Digite o terceiro seguimento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos de reta R1:{}, R2:{} e R3:{} fomrmam um triângulo'. format(r1,r2,r3))
else:
    print('Os seguimentos de reta R1:{}, R2:{} e R3:{} NÃO fomrmam um triângulo'. format(r1,r2,r3))