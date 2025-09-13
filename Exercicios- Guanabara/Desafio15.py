dias = int(input('Quantos dias alugados: '))
km = float(input('Digite a kilometragem rodada: '))

print('Você alugou o carro por {} dias e rodou {} kilometros.O custo final é R${}'.
format(dias,km,(dias*60) + (km*0.15)))