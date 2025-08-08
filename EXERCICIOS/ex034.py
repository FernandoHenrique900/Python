#Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
sal =int(input("Digite o valor do salário atual: "))

reaj = sal *1.15 if sal <= 1250 else sal*1.1 

print("Seu salario era R${} de R${}".format(sal,reaj))