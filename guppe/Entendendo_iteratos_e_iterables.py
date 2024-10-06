'''
entendendo iteratos e iterables

iterator
    -> é um objeto que pode ser iterado
    -> um objeto que retorna, um dado sendo uma elemento por vez quando uma função next() for chamada
iterable
    -> um objeto que ira retornar um iterator quando a função iter() for chamada

nom = iter(nome)
print(next(nom))

'''

nome = 'geeh' #  é um iterable mas nçao é um iterator

for letra in nome:
    print(f'{letra}')


