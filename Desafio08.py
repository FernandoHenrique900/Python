#ler metragem e mostrar em centimetros e milimetros

m =float(input('Digite a metragem = '))

cm = m *100
mm = m*1000

print('Metragem inicial = {},que fica {} em Centimentros , e {} Milimetros'
.format(m, cm, mm))