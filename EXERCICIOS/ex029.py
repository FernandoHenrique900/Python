#Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
vel = int(input('Qual a velocidade atual do seu carro? '))
max = 80

if vel < max:
    print('Tenha uma boa viagem! Dirija com segurança!')
elif vel == max:
    print('Cuidado! Você está no limite de velocidade!')
else:
    print('Você está a {}km/h, ultrapassou limite de {}km/h permitido. Sua multa é de : R${:.2f}. Tenha prudencia ao dirigir!'.format(vel, max,(vel-max)*7))  