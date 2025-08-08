#valores = list()
#valores.append(5)
#valores.append(9)
#valores.append(4)

'''for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posicao {c} encontrei o valor 1{v}!')
print('Cheguei ao final da lista.')'''

#Exemplo de peculiaridade

a = [2, 3, 4, 7]
b = a[:] #colocando os pontos, ele recebe todos os itens fazendo uma copia
b [2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')