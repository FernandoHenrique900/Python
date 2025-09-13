#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER

from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print('O Atleta tem {} anos.' . format(idade))

if idade <=9:
    print('Atleta Mirim')
elif idade >=9 and idade <= 14:
    print('Atleta Infantil')
elif idade >=14 and idade <= 19:
    print('Atleta Júnior')
elif idade >=19 and idade <= 25:
    print('Atleta Sênior')
elif idade > 25:
    print('Atleta Master')