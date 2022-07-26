#Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras=('APRENDER', 'PROGRAMAR', 'LINGUAGEM','PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR','PRATICAR', 'TRABALHAR', 'MERCADO','PROGRAMADOR','FUTURO')

for p in palavras: #FOR ANALISA CADA ELEMENTO DA TUPLA
    print(f'\nNa palavra {p} temos', end=' ')
    for letra in p: #ESSE FOR ANALISA AS VOGAIS
        if letra in 'AaEeIiOoUu':
            print(letra, end=' ')