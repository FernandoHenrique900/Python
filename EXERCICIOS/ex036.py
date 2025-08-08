#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
from time import sleep
valor =float(input("Digite o valor do imóvel a ser financiado R$ "))
sal = float(input("Digite a renda financiador R$ "))
tempo = int(input("Quantos anos desejar realizar o financiamento? "))
parcela = valor/ (tempo*12)
print('Processando...')
sleep(1)

if parcela >= sal*0.3:
    print("\033[1;30;41m 'EMPRESTIMO NEGADO' \033[m. Para pagar um imóvel de {} em {} anos, a prestação será de \033[1;30;41m{:.2f}.\033m".format(valor,tempo,parcela))
else:
    print("\033[1;30;44m 'EMPRESTIMO CONCEDIDO' \033[m. Para pagar um imóvel de {} em {} anos, a prestação será de \033[30;44m{:.2f}\033m".format(valor,tempo,parcela))