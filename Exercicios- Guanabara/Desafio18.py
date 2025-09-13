from math import radians, cos, sin, tan
ang = float(input('Digite o ângulo que você desaja: '))
sen = sin(radians(ang)) #convertendo para radianos
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang,sen))
cos = cos(radians(ang)) #convertendo para radianos
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang,cos))
tan = tan(radians(ang)) #convertendo para radianos
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(ang,tan))
