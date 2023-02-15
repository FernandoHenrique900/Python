"""Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Coritiba."""


times = (
'Palmeiras',
'Atlético-MG',
'Corinthians',
'Internacional',
'Fluminense',
'Athletico-PR',
'Flamengo',
'Bragantino',
'São Paulo',
'Santos',
'Botafogo',
'Avaí',
'Goiás',
'Ceará',
'Cuiabá',
'Coritiba',
'América-MG',
'Atlético-GO',
'Fortaleza',
'Juventude'
)

print('-=' *15)
print(f'Lista de times{times}')
print('-=' *15)
#for t in times:
#   print (t)

#a) Os 5 primeiros times.
print('-=' *15)
print(f'Os 5 primeiros são{times[0:5]}') # lembrando que o fatiamento ignora o ultimo elemento
print('-=' *15)

#b) Os últimos 4 colocados.
print('-=' *15)
print(f'Os 4 últimos colocados são{times[-4:]}')
print('-=' *15)

#c) Times em ordem alfabética.
print('-=' *15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' *15)

#d) Em que posição está o time da Coritiba.
print('-=' *15)
print(f'O Coritiba está na {times.index("Coritiba")+1} posição')
print('-=' *15)