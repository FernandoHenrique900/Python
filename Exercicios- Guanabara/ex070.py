#Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

#A) qual é o total gasto na compra.

#B) quantos produtos custam mais de R$1000.

#C) qual é o nome do produto mais barato.

print('-' * 40)
print('           LOJA SUPER BARATÃO           ')
print('-' * 40)

tot=  totMil = menor = cont =0
barato=' '


while True:
    prod = str(input('Nome do produto: '))
    preco = int(input('Preço: '))
    cont +=1
    tot += preco
    if preco >=1000:
        totMil +=1
    #LOGICA PRA ACHAR O PRPDUTO MAIS BARATO    
    if cont == 1 or preco < menor:
        menor = preco
        barato = prod 

    resp=' '
    while resp not in 'SN':
        resp = str(input('Gostaria de continuar comprando? ')).upper().strip()[0]
    if resp =='N':
        break
print(f'Total da compra R${tot:.2f}')
print(f'Total de produdos que custo mais que R$1000 = {totMil}')
print(f'O produto mais barato é {barato} custando R${menor:.2f}')
print('{:-^40}'.format('FIM DO PROGRAMA'))

