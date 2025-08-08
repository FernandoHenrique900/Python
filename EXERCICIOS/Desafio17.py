'''
#Calculo de hipotenusa sem modulo
catetoOposto=float(input('Digite o cateto oposto: '))
catetoAdjacente=float(input('Digite o cateto adjacente: '))
hipotenusa = (catetoOposto ** 2 + catetoAdjacente ** 2) **(1/2)
print('A hipotenusa medi(s/mod): {:.2f}'.format(hipotenusa)) 
'''

from math import hypot
#Calculo de hipotenusa com modulo
catOpo=float(input('Digite o cateto oposto: '))
catAdj=float(input('Digite o cateto adjacente: '))
hipotenusa = hypot(catOpo, catAdj)
print('A hipotenusa medi(c/mod): {:.2f}'.format(hipotenusa))

input("Press enter to exit ;)")