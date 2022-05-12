#Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

c = s = 0
while True: #loop infinito c/ flag do break sendo 999
    n= int(input('Digite em número(-0 p / parar): '))
    if n == -0:
        break
    c+=1
    s+=n
print(f'Foram digitados {c} valores, e a soma de todos é {s}') #jeito novo de fstring do python 3.6+
