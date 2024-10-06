'''
Named tuple
#  Recap´tupla
tupla = (1, 2, 3)
print(tupla[1])

Named tupla -> São tuplas diferemciadas onde, especificamos um nome para a mesma e tambem
parametros
'''

from collections import namedtuple
# Declaração
# forma 1
cachorro = namedtuple('cachorro', 'nome idade raça')
# Declaração
# forma 2
cachorro = namedtuple('cachorro', 'nome, idade, raça')
# Declaração
# forma 3
cachorro = namedtuple('cachorro', {'nome', 'idade', 'raça'})

# Usando
ray = cachorro(nome='pld', idade=5, raça='pitibull')
print(ray)

# acessando os dados
# forma 1

print(ray[0])
print(ray[1])
print(ray[2])

# forma 2

print(ray.nome)
print(ray.idade)
print(ray.raça)

print(ray.index('pitibull'))
print(ray.count(5))













