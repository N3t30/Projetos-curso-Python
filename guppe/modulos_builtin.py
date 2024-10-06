'''
builtin são modulos integrados em python
_________________________
/python/Módulos builtin/

# podemos importar todas as funções de um módulo utilizando o *
from random import *

print(random())

# utilizando alias (apelido para Módulos e funções
import random as rdm
print(rdm.random())

# utilizando alias (apelido para Módulos e funções

from random import randint as rdi
print(rdi(5, 98))
'''

# costumamos utilizar tuple para colocar multiplpos de um memos módulos

from random import (
    random,
    randint,
    shuffle,
    choice,
)

print(random())

lista = ['neto', 'peixoto', 'Almeida']
shuffle(lista)
print(lista)

print(randint(5, 25))

print(choice('neto peixoto'))