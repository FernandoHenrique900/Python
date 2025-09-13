# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

menor = 0
maior = 0
for i in range(1,6):
    peso = int(input("Peso da {}ª pessoa: ".format(i))) 
#solucao genial
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(' FINAL - O maior peso e {}, e o menor peso e {}'.format(maior,menor))
