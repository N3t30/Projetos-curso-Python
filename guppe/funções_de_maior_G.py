'''
funções de maior grandeza - higher order functions - HDF

o que isso significa

- Quando uma linguagem de programação suporta HOF, indica que podemos ter funções que retornam outras funções como
resultado ou mesmo que podemos passar funções como argumento para outras funções, e ate memso criar variaveis
do tipo funções nos nossos programa

OBS : nA SEÇÃO DE funções, nos utilizamos isso

# Exemplo definindo as funções

Em python as funções são cidadões de primeira classe


def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def dividir(a, b):
    return a / b

def multi(a, b):
    return a * b

def calcular(num1, num2, funcao):
    return funcao(num1, num2)

# testando as funções

print(calcular(4, 8, somar))
print(calcular(4, 8, multi))
print(calcular(4, 8, dividir))
print(calcular(4, 8, subtrair))

# nested functions - funções aninhadas

# Em python, podemos tamebm ter funções dentro de funções, que são conhecidas por nested functions
# ou tambem inner functions

from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(('Bom dia', 'Boooooom dia', 'Boooooooooooom dia'))
    return humor() + pessoa

print(cumprimento(' solange'))
print(cumprimento(' almeida'))
print(cumprimento(' soraya'))

# Retornando funções de outras funções

from random import choice

def fazer_rir():
    def rir():
        return choice(('sfdkfhjfekfj', 'dewdnhiweid', 'djdebejhdhie'))
    return rir()

rindo = fazer_rir()
print(rindo)


# inner functions podem acessar o escopo de funções externas
from random import randint

items = ('Pedra', 'papel', 'tesoura')
computador = randint(0, 2)

print("""
JOKENPO!!
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")

jogador = int(input('Qual a sua escolha? : '))

jogadas =
'''

# inner functions podem acessar o escopo de funções externas
from random import randint

items = ('Pedra', 'papel', 'tesoura')
computador = randint(0, 2)

print("""
JOKENPO!!
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")

jogador = int(input('Qual a sua escolha? : '))

jogadas = 





