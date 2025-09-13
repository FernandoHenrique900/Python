from math import floor,ceil,trunc

num = float(input('Digite um numero: '))
#Parte inteira
print('O numero é: {}, e a parte inteira é: {}'.format(num,trunc(num)))

#Outra maneira de pegar parte inteira, sem usar modulos
print('O numero é: {}, e a parte inteira é: {}'.format(num,int(num)))

#Pra cima ou pra baixo
print('O numero: {},  pra cima: {}, e pra baixo: {}'.format(num,ceil(num),floor(num)))
