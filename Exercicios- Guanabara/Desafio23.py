# Forma String nunérica, faça um programa que leia de 0 a 9999 
# e separe cada um dos digitos separados

#STRING , obs: da erro se usar numeros acima ou abaixo de 4 digitos
num = int(input('Informe um numero: '))
n = str(num)
print('Analisando o número: {}'.format(num))
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena: {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))

#NUMERICA USANDO A MATEMÁTICA

num1 = int(input('Informe um numero: '))
unid = num1  // 1 % 10
dez = num1  // 10 % 10
cent = num1  // 100 % 10
mil = num1  // 1000 % 10 

print('Analisando o número: {}'.format(num1))
print('Unidade: {}'.format([unid]))
print('Dezena: {}'.format([dez]))
print('Centena: {}'.format([cent]))
print('Milhar: {}'.format([mil]))