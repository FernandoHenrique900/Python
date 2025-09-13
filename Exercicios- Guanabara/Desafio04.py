#TESTANDO PRIMITIVOS
n = input('Digite qualquer coisa: ')


print('O tipo primitivo é', type(n))
#teste se é numeral
print ('É numérico ?', n.isnumeric())
#teste se é espaço
print ('É espaço ?', n.isspace())
#teste se é alfabetico
print ('É alfanbético ?', n.isalpha())
#teste se é alfanumerico
print ('É alfanumerico ?', n.isalnum())
#teste se é minusculo
print ('É minusculo ?', n.islower())
#teste se é maiusculo
print ('É MAIUSCULO ?', n.isupper())

#teste se é capitalizada
print ('É capitalizado ?', n.istitle())