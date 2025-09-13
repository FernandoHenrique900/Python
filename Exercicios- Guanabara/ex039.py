#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
anoNasc =int(input('Que ano vocë nasceu ? '))
anoAtual = date.today().year
idade = anoAtual - anoNasc

print ('Você tem {} anos.Voce nasceu em {}'.format(idade,anoNasc))

if idade ==18:
    print('Aliste-se imediatamente.')
elif idade < 18:
    saldo = 18 - idade
    alist = anoAtual + saldo
    print('Ainda falta {} anos para seu alistamento. Seu alistamento será em {}'.format(saldo, alist))
elif idade > 18:
    saldo = idade - 18
    alist = anoAtual - saldo
    print('Seu alistamento foi há {} , devia ter se alistado em {}'.format(saldo, alist))