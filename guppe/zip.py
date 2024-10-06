"""
zip

zip() -> ele cria um iteravel chamado zip object que agrega elementos de cada um dos iteraveis passando como entrada em pares

# Exemplos
lista1 = [1, 2, 3]
lista2 = [1, 5, 6]

zip1 = zip(lista1, lista2)

print(zip1)
print(type(zip1))

print(list(zip1))

print(tuple(zip1))

print(set(zip1))

print(dict(zip1))

lista3 = [1, 2, 3, 6, 5, 5]
zip1 = zip(lista1, lista2, lista3)
print(list(zip1))

# podemos utilizar diferentes iteraveis com zip
lista = [1, 2, 3, 4, 5, 6]
tupla = (1, 2, 3, 4, 5, 6)
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

zip1 = zip(lista, tupla, dicionario.values())
print(list(zip1))

# listas de tuplas
dados = [(0, 1), (2, 3), (5, 3)]
print(list(zip(*dados)))

# Exemploa
prova1 = [48, 70, 89]
prova2 = [58, 36, 98]
alunos = ['maria', 'jessica', 'pedrp']


final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}

print(final)

# podemos utilizar o map
final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))

print(dict(final))
"""

