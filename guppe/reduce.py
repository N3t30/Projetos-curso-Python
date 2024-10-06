'''
REduce
OBS: a partir do python 3+ a função reduce() não é mais uma função integrada, agora temos que importar e utilizar esta
função a partir do modulo 'functools'

para entender o reduce
'''
# como funciona ns pratica
# vamos utilizar o reduce para multipliccar todos os numeros de uma lista

from functools import reduce

dados = [1, 2, 3, 4, 8, 6, 9, 1, 1, 26, 23]

# para utilizar o reducr temos que utilizar uma função quqe receba dois parametros
multi = lambda x, y: x * y
res = reduce(multi, dados)
print(res)

# utilizando o loop normal
res = 1
for n in dados:
    res = res * n

print(res)
