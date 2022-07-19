#TUPLAS  - OBS:SÃO IMUTAVEIS
# ()-TUPLA []-LISTA {}-DICIONÁRIO 

lanche = ('hamburger','juice','pizza','pudim')
print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])

#####EXEMPLO DE FOR ########
for comida in lanche:
    print(f'I will eat {comida}')
print (f'Eat a lot!!')

#####EXEMPLO DE FOR ########
for cont in range(0, len(lanche)):
    print(f'I will eat again {lanche[cont]} at position {cont}')

#####EXEMPLO DE FOR ######## usando ENUMERATE
for pos, comida, in enumerate(lanche):
    print(f'I will eat {comida} na posicao {pos}')
print(f'Eat a lot again and again - Fat life style Rules!')

####EXEMPLO DE ORGANIZAÇÃO USANDO SORTED#####
print (sorted(lanche))

#####EXEMPLO DE ELEMENTOS NA TUPLA########
pessoa = ('Toddy', 30, 'M', 99.88)

#####EXEMPLO DE SOMA DE TUPLAS ####
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a  #SOMENTE SOMA, MEIO QUE CONTATENA
print(c)

