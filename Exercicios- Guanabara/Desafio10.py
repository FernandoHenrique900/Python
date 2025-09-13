#Ler valor na wallet e mostrar qtos dollares da pra comprar
#dolar 5.23 24/07/2020

val = float(input('Digite quanto vc tem na wallet = '))

dol = val / 5.30

print('Valor em BRL - R${:.2f} da para comprar USA US${:.2f}' .format(val,dol))
