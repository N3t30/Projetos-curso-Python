'''
Dicitionary comprehensions

se quisermos criar uma lista fazemos :
lista = [ 1, 2, 5]

uma tupls :
tupla = (1, 2, 3, 4)

um conjunto :
conjunto = {1, 2, 3, 4, 5}

um dicionario :
dicionario = {'a':1, 'b': 2, 'c': 3}

# Sintaxy
{cahve:valor for valor in iteravel}

# Exemplos

numeros = {'a': 1, 'b': 2, 'c': 3}

Quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}

print(Quadrado)

numeros = {1, 2, 3, 4, 5} # listas, tupls e conjunto

quadrado = {valor: valor ** 2 for valor in numeros}
print(quadrado)

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mix = {valores[i]: chaves[i] for i in range(0, len(valores))}
print(mix)

# Exemplpo com logica condicional

numeros = [1, 2, 3, 4, 5]

res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}
print(res)

'''

def subtrair(a, b):
    return a - b




























