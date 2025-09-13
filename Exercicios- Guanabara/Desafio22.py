#DESAFIO 22
#Crie um programa que leia um nome completo de uma pessoa e mostre:
#O nome dela com todos os caracteres maiúculos
#Quantos caracteres tem (desconsidere espaços)
#Quantas Letras tem o primeiro nome. 


nome=str(input('Digite seu nome: ')).strip() #ELIMINEI OS ESPAÇOS (INICIO E FIM) NA RAIZ

print("Nome em maiusculo: {}" .format(nome.upper()))

print("Nome em minúsculo: {}" .format(nome.lower()))

print("Nome tem : {} caracteres" .format(len(nome) - nome.count(' '))) #ELIMINANDO ESPAÇOS ENTRE

#1º - JEITO DE SEPARAR / CALCULAR CARACTERES
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

#2º - JEITO DE SEPARAR / CALCULAR CARACTERES
separa = nome.split()

print ('Seu primeiro nome é {} e ele tem {} caracteres'.format(separa[0], len(separa[0])))