#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

#– à vista dinheiro/cheque: 10% de desconto

#– à vista no cartão: 5% de desconto

#– em até 2x no cartão: preço formal 

#– 3x ou mais no cartão: 20% de juros


print('{:=^40}'.format(' WAL-MART SUPERMARKET '))

valProd = float(input('Digite o preço das compras:'))
print(''' FORMAS DE PAGAMENTO 
[ 1 ] à vista DINHEIRO / CHEQUE
[ 2 ] à vista CARTÃO
[ 3 ] 2x no CARTÃO
[ 4 ] 3x ou mais no CARTÃO ''')

opcao = int(input('Qual o opção de pagamento ? '))

if opcao == 1:
    total = valProd * 0.9
elif opcao == 2:
    total = valProd * 0.95
elif opcao == 3:
    total = valProd 
    parcela = valProd / 2
    print('Sua compra será parcelada em 2x de R${:.2f} S/ JUROS'.format(parcela))
elif opcao == 4:
    total = valProd * 1.2
    totparc = int(input('Quantas parcelas ?'))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} C/ JUROS'. format(totparc, parcela))
else:
    total = valProd
    print ('Digite uma opção válida para prosseguir com a forma de PAGAMENTO')



print('Sua compra  de R${:.2f} vai custar R${:.2f} no final'.format(valProd, total))