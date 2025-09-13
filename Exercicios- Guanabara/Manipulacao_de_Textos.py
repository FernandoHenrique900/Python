#Aula de Manipulação de textos

frase = " Curso em Vídeo Python "
print(frase)

#CARACTERE ESPECIFICO
print(frase[3])

#FATIANDO
print(frase[3:14])

#DO INICIO ATÉ DETERMINADA POSICÃO
print(frase[:14])

#DETERMINADO PORTO ATÉ O FINAL
print(frase[15:])

#INICIANDO DE CERTA POSIÇÃO E PULANDO DE 2 EM 2
print(frase[0:15:2])

#FRASE INTEIRA E PULANDO DE 2 EM 2
print(frase[::2])

#USANDO ASPAS DUPLAS (3 VEZES (""")) ELE IMPRIME O TEXTO INTEIRO SEM PRECISAR QUEBRAR LINHA

print("""Muitos que vivem merecem a morte. E alguns que morrem merecem viver. 
Você pode dar-lhes a vida? Então não seja tão ávido para julgar e condenar alguém a morte. 
Pois mesmo os muitos sábios não conseguem ver os dois lados.""")

#PYTHON TRATA TUDO COMO OBJETO ENTÃO PODE USAR FRASE.FUNÇÃO
print(frase.count('o'))

#FUNCAO MAIUSCULO
print(frase.upper())

#FUNÇÃO DE ANALISE DE TAMANHO
print(len(frase))

#REMOVER ESPAÇOS
print(frase.strip())

#SOBRESCREVER
print(frase.replace('Python','Android'))

#ACHAR PALAVRA DENTRO DE FRASE
print('Curso' in frase)

#ACHAR PALAVRA DENTRO DE FRASE NA POSIÇÃO INICIAL
print(frase.find('Vídeo'))

#DIVIDIR A FRASE 
print(frase.split())

#DIVIDIDO ATRIBUIDO A UMA VARIAVEL
dividido = frase.split()
print(dividido[0])

#DIVIDIDO ATRIBUIDO A UMA VARIAVEL E MOSTRAR UMA LETRA ESPECIFICA DA POSICAO JÁ DIVIDIDA
dividido = frase.split()
print(dividido[2][3])

#DUAS FUNCOES
print(frase.lower().find('vídeo'))