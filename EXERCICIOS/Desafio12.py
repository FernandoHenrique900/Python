#Ler o preço de um produta e dar 5% de desconto

preço = float(input('Digite o preço do produto: '))

desc = preço *0.95

print('Valor original =R${}, com desconto de 5% fica R${} '.format(preço,desc))