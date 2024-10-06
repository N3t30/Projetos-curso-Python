'''
entendendo o *args
 O *args é um parametro cmo outro qualquer, isso siguinifica que voce podera chamar de qualquer
coisa, desde que comece com o *

o parametro args utilizado em uma função, coloca os valores extrs informados como entraxda em uma tupla
então desde ja lembre-se que tupla é imutavel


# Entendendop o args

def soma(*args):
    return sum(args)

print(soma(1))
print(soma(2, 5))
print(soma(3, 5, 9))
print(soma(6, 9, 8, 6, 3))


# outro exemplo de ytilização do *args

def verifica_info(*args):
    if 'neto' in args and 'peixoto' in args:
        return 'bem vindo Neto'
    return 'Não sei quem é voce'

print(verifica_info())
print(verifica_info(1, 23, 'neto', 33, 'peixoto'))
print(verifica_info(45, 325, 'peixoto'))
'''

def soma_tudo(*args):
    return sum(args)

# print(soma_tudo())
# print(soma_tudo(2, 3, 2, 6, 5))

# numeros = [3, 6, 2, 5, 6] # Modo errado
# print(soma_tudo(numeros))

# desempacotar
numeros = [3, 2, 6, 5, 3, 5]
print(soma_tudo(*numeros))