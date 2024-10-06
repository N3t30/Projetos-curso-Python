'''
OBS; não confunda, apesar do nome, com a função sort que passou em listas, o sorte so funciona em listas

podemos utilizar o sorted em qualquer iteravel

como proprio nome diz o sorted serve para ordenar

OBS; o sorted, sempre retorna uma lista com elementos iteravel ordenados

# Exemplos
numeros = [1, 5, 6, 2, 3, 2]
print(numeros)
print(sorted(numeros))
print(numeros)

numeros = [1, 5, 6, 2, 3, 2]
print(numeros)
# adicioanando parametros ao sorte
print(tuple(sorted(numeros)))


print(sorted(numeros, reverse=True)) # ordena do maior para o menor
'''

# podemos utilizar sorted() para coisas mais completas

usuarios = [
     {'username': 'Gabriel', 'twiters':["Eu sou timido", "Gosto de futebol"]},
     {'username': 'doggo', 'twiters':[]},
     {'username': 'carlaa', 'twiters':["Eu sou timido"]},
     {'username': 'julius', 'twiters':["Eu sou timido", "Gosto de futebol"]},
     {'username': 'gal', 'twiters':[]},
     {'username': 'pedro', 'twiters':["Eu sou timido", "Gosto de futebol"]},
     {'username': 'gaaal', 'twiters': [], 'cor':['amarelo'], 'atividade':['futebol']}
]

print(usuarios)

print(sorted(usuarios, key=lambda usuario: usuario['username']))