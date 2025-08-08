idade=int(input('Digite idade: '))

if 0 < idade <= 12:
    print(f'idade:{idade} é criança')
elif 12 < idade < 18:
    print(f'idade: {idade} é adolescente')
elif idade >=18:
    print(f'idade:{idade} é adulto')
else:
    print('Valor inválido')