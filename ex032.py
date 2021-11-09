#Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
#FORMULA SE O ANO  DIVISIVEL POR 4 FOR IGUAL A O (ZERO) é BISSEXTO 
#Primeira situação: Se o ano de 2015 ou 2016 for uma divisão exata em relação a 4, deveremos verificar, em seguida, se não é divisível por 100. Se não for, o ano será bissexto;
#Segunda situação: Se o ano de 2015 ou 2016 não for divisível por 4, então deveremos verificar se ele é divisível por 400. Se também não for divisível, o ano de 2015 não será bissexto;
#Terceira situação: Se o ano de 2015 ou 2016 não for divisível por 4, então devemos verificar se ele é divisível por 400. Caso seja, o ano de 2015 é bissexto.
    from datetime import date
    ano =int(input('Qual ano quer analisar? '))
if ano == 0:                   #condição para pegar o ano atual no lugar do zero
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano %400  == 0: 
    print('O ano {} é bissexto'.format(ano)) 
else: 
    print ('O ano {} NÃO é bissexto'.format(ano))
