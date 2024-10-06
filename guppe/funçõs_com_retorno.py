'''
funções com retorno

numeros = [1, 2, 3]

print(numeros)

ret_pop = numeros.pop()

print(f'retorno do pop {ret_pop}')

ret_pr = print(numeros)

print(f'retorno do print {ret_pr}')

OBS : Em python, qunado uma funçõa não retorna nenhum valor, o retorno é NONE

obs : funções python que retornam valores, devem retornar esses valores com a palavra
reservada return

OBS : Não prcisamos necessariamente criar u,a variavel para receber o retorno
de uma função, podemos passar a execução da função para outras funções


# Vamos refatorar esta função, para que ela retorne o valor

def quadrado_de_7():
    return 7 * 7

# Criando uma variavel para receber o retorno da função
ret = quadrado_de_7()
print(f'retorno {ret}')

print(f'retorno {quadrado_de_7() + 1}')

# refatorando a primeira função
def diz_oi():
    return 'Oi'

alguem = 'Pedro'
print(diz_oi() + alguem)

OBS: Sobre a palavra return

1 - Ela finaliza a função, ou seja, ela sai da execução da função
2 - POdemos ter, em uma função, diferentes Returns
3 - POdemos em uma função retornasr qualquer tipo de dado e ate mesmo multiplos valores

# Exemplo 1
def diz_oi():
    print('EStou dendo executado antes do retorno')
    return 'Oi!'
    print('EStou sendo executado depois do retorno')

print(diz_oi())

# Exemplo 2


def nova_fnução():
    variavel = True
    if variavel:
        return 'ativo'
    elif variavel is None:
        return 'não logado'
    return 'offline'

print(nova_fnução())

# Exemplo 3

def outra_função():
    return 2, 3, 4, 5


# num1, num2, num3, num4 = outra_função() # deempacotando
# print(num1, num2, num3, num4)
print(outra_função())

from random import random

# vamos criar uma função para jogar a moeda
def jogar_moeda():
    if random() > 0.5:
        return 'cara'
    return 'coroa'

print(jogar_moeda())

# pera papel tesoura
def pedra_papel_tesoura():
    if random() <= 0.35:
        return 'pedra'
    elif random() <= 3.65:
        return 'papel'
    return 'tesoura'

from random import random
def pedra_papel_tesoura():
    if random() <= 0.35:
        return 'pedra'
    elif random() <= 0.65:
        return 'papel'
    return 'tesoura'


print(pedra_papel_tesoura())
print(pedra_papel_tesoura())

'''

def cantar_parabens(nome):
    print('parabens para voce')
    print('nesta data querida')
    print('muitas felicidades')
    print('muitos anos de vida')
    print(f'viva o {nome}')

print(cantar_parabens('Neto!'))






















