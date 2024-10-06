'''
filter
# fazendo a media

import statistics
notas = 1, 2, 3, 4, 8, 5, 6.5, 5.6, 8.1, 7.8, 6.8

media = round(statistics.mean(notas))
print(media)

res = filter(lambda x: x > media, notas)
print(list(res))

# OSB: assim como na função map apos ser utilizados os dados de filter eles sõa excluidos da memoria

paises = ['', 'bolivia', '', 'equador', '', 'brasil', 'china', '', 'argentina']
print(paises)
res = filter(None, paises)
print(list(res))

paises = ['', 'bolivia', '', 'equador', '', 'brasil', 'china', '', 'argentina']

# a DIFERENCIA ENTRE MAP E FILTRER É
# No map().....-> recebe dois parametros, uma função e um iteravel e retorna um objeto mapeando a função para cada
# elemento iteravel

# No filter().....-> Recebe doi parametros, uma função e um iteravele e  retorna um objeto filtrando apenas os elementos

# Exemplos mais complexos
usuarios = [
     {'username': 'Gabriel', 'twiters':["Eu sou timido", "Gosto de futebol"]},
     {'username': 'doggo', 'twiters':[]},
     {'username': 'carlaa', 'twiters':["Eu sou timido"]},
     {'username': 'julius', 'twiters':["Eu sou timido", "Gosto de futebol"]},
     {'username': 'gal', 'twiters':[]},
     {'username': 'pedro', 'twiters':["Eu sou timido", "Gosto de futebol"]},
     {'username': 'gaaal', 'twiters':[]}
]
print(usuarios)

# filtar os usuarios que estão inativos no twiter
# forma 1
# inativos = list(filter(lambda usuario: len(usuario['twiters']) == 0, usuarios))

# print(inativos)

inativos = list(filter(lambda usuario: not usuario ['twiters'], usuarios))
print(inativos)
'''

# combinar filter e map

nomes = ['vanessa', 'Ana', 'maria']

# Devemos criar uma lista contendo "sua professora é" + o nome da professora

lista = list(map(lambda nome: f' Sua professora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista)































