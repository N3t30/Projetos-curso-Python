'''
msp
com map fazemos mapeamento de valores da função

import math
def area(r):
    """calcula a area de um circulo no valor"""
    return math.pi * (r ** 2)

print(area(2))
print(area(5.3))

raios = [2, 1, 5, 6, 8]

areas = []

for r in raios:
    areas.append((area(r)))

print(areas)

# usando o map
# map é uma funçao que recbe dois parametros, o primeiro a função, o segundo o iteravel, Retorna um mpa object
areas = map(area, raios)
print(list(areas))

# forma 3 map com lambda

print(list(map(lambda r: math.pi * (r ++ 2), raios)))

#OBS: apos utilizar a função map() depois da primeira utilização do resultado ele zera

# para fixar map
# temos dados iteraveis
# dados a1, a2, a3, ....... an
# temos uma função
# função: f(x)
# utilizamos a função amp(f, dados) onde map ira mapear cada elento dos dados e aplicar a função
# o map object: f(a10, f(a2), f(a3), ...... f(an) 
'''
# mais um exemplo
cidades = [('berlim', 25), ('tokio', 30), ('nova york', 15), ('Russia', 20)]

print(cidades)
# f = 9/5 * c + 32
# lambda

c_para_f = lambda dado: (dado[0], round(9/5 * dado[1] + 32))

print(list(map(c_para_f, cidades)))