'''
teste de velocidade com expressões geradoras
# Generators (geradores)

def nums():
    for num in range(1, 10):
        yield num

ge1 = nums()

print(ge1)
print(next(ge1))

# generator expression

ge2 = (num for num in range(1, 10))

print(ge2)
print(next(ge2))

'''

# realizando o teste de velocidade

import time
# generatot expression
gen_inicio = time.time()
print(sum(num for num in range(1000000)))
gen_tempo = time.time() - gen_inicio

# list comprehenions
list_inicio = time.time()
print(sum(num for num in range(1000000)))
list_tempo = time.time() - list_inicio

print(f'generator expressions levou {gen_tempo}')
print(f'List comprehensions levou {list_inicio}')