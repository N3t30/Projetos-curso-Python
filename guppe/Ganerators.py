'''
Generators

nomes = ['carlos', 'romeu', 'carlito', 'cassiano', 'camilo']

# como list comprehension
res = [nome[0] == 'c' for nome in nomes]
print(type(res))
print(res)
# Generators
res = (nome[0] == 'c' for nome in nomes)
print(type(res))
print(res)
# Generators ocupa menos recurso e memoria

# Qual é a utilidade de getsizeof()? -> Retorna a quantidade d bytes em memoria do elemento passado como parametro
from sys import getsizeof
print(getsizeof('neto'))
print(getsizeof('neto peixoto'))
print(getsizeof(58))
print(getsizeof(900))
print(getsizeof(9))


from sys import getsizeof

# Gerando uma lista de numeros com list comprehensions
list_comp = getsizeof([x * 10 for x in range(1000)])

# com set
set_comp = getsizeof({x * 10 for x in range(1000)})

# com dict
dict_cmop = getsizeof({x: x * 10 for x in range(1000)})

# com Generator
Generator = getsizeof(x * 10 for x in range(1000))

print('para fazer a mesma tarefa gastando memoria')
print(f' list comprehenion gasta {list_comp} bytes')
print(f' set comprehenion gasta {set_comp} bytes')
print(f' dict comprehenion gasta {dict_cmop} bytes')
print(f' Generator gasta {Generator} bytes')
'''

# Eu posso iterar do Generator expression? sim
gen = (x * 2 for x in range(50))
print(gen)
print(type(gen))
for num in gen:
    print(num)


