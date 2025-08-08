#Ler altura e largura, calcular área e definir quantos litros de tinta necessita
# a cada 2 mts 1 litro de tinta

alt = float(input('Digite a altura = '))
larg = float(input('Digite a largura = '))

area = alt * larg

tinta = area / 2

print('Altura = {}, Largura = {}, Área = {}, necessita de {} litros de tinta'
.format(alt, larg, area, tinta))