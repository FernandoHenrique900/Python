#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeHomemMaisVelho = ''
mulherMenor = 0
for i in range (1,4):
    print('------ {}ª Pessoa ----'.format(i))
    nome = str(input('Nome: ')).strip().upper()

    idade = int(input('Idade: '))
    somaIdade += idade
    sexo = str(input('[M/F]: ')).strip().upper()
    
#TESTE HOMEM MAIS VELHO
    if i == 1 and sexo == 'M':
        maiorIdadeHomem = idade
        nomeHomemMaisVelho = nome
    if sexo == 'M' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeHomemMaisVelho =nome

#TESTE MULHER ABAIXO DE 20
    if sexo == 'F' and idade < 20:  #caso nao tenha tratamento do input pra UPPER usar in 'Ff' feminino ou 'Mm' para masculino
        mulherMenor +=1
mediaIdade = somaIdade/i
print(somaIdade)
print('A media da idade do grupo e: {:.2f}'.format(mediaIdade))
print('O homem mais velho tem {} anos e se chama {}'.format(maiorIdadeHomem,nomeHomemMaisVelho))
print('No grupo temos {} mulheres abaixo dos 20 anos'.format(mulherMenor))