menor = 0
maior = 0
for i in range(1,2):
    peso = int(input("Peso da {}ª pessoa: ".format(i))) 
#solucao genial
    if i == 1:
        maior == peso
        menor == peso
        print('O maior peso e {}, e o menor peso e {}'.format(maior,menor))