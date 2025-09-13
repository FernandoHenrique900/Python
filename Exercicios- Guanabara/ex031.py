#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

perc = float(input('Qual a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km.'.format(perc))

if perc <= 200:
    print('O valor da viagem é R${:.2f}'.format(perc*0.50))
else:
    print('O valor da viagem é R${:.2f}'.format(perc*0.45))

''' if SIMPLIFICADO
preco = perc * 0.5 if pec <=200 else perc *0.45
'''    