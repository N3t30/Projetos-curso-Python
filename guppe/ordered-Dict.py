
'''
modulo collections Ordered Dict

# EM um dicionario a ordem de inserção dos elementos não é garantida
dicionario = {'b': 2, 'f':58,'y': 0, 'j': 5, 'p': 5}
for chave, valor in dicionario.items():
    print(f'chave = {chave}:valor = {valor}')

PBS => OrderedDict é um dicionario, que nos garante a ordem de inserção dos eleemntos

from collections import OrderedDict
dicionario = OrderedDict({'b': 1, 'f':2,'y': 3, 'j': 4, 'p': 5})

for chave, valor in dicionario.items():
    print(f'chave={chave}:vslor={valor}')

'''

from collections import OrderedDict
# entendendo a diferencai entre dict e orderedDict
# Dicionarios comum
dic1 = {'a': 2, 'b': 1}
dic2 = {'b': 1, 'a': 2}

print(dic1 == dic2)

# Ordered dict

dict1 = OrderedDict({'a': 2, 'b': 1})
dict2 = OrderedDict({'b': 2, 'a': 1})

print(dict1 == dict2)











