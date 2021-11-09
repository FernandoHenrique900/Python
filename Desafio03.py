numero1 = int(input ('Digite o primeiro numero: ')) #tipo primitvio
numero2 = int(input ('Digite o segundo numero: '))  #tipo primitvio

soma = numero1 + numero2

#print('A soma entre: ', numero1,' e ', numero2, 'vale = ' , soma)

print('A soma entre: {} e {} vale {}' .format(numero1, numero2 , soma)) #bem melhor

# informa o tipp usa

print(type(soma)) #mostra que tipo é o objeto