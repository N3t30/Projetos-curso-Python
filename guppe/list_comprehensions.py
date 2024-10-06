'''
list comprehension parte 1

- utilizando liost comprehension nos podemos gerar novas listas com dados processados as partiri de outro iteravél

# Sintaxe da list comp

[dado for dado in iretavél]

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]

print(res)

# para enttender melhorr oq estar acontececndo devemos dividir a expressão
# -  'p1, for numero in numeros'
# -  ' p2, numero * 10'

# list comp versus loop

# loop
numeros = [1, 2, 3, 4, 5, 6]
numeros_dois = []

for numero in numeros:
    numero_dois = numero * 2
    numeros_dois.append(numero_dois)

print(numeros_dois)

# list comprehensions
print([numero * 2 for numero in numeros])

'''

# outros Exemplos
# 1
nome = 'neto peixoto'
print([letra.upper() for letra in nome])

# 2
print([numero * 3 for numero in range(1, 11)])

# 3
print([bool(valor) for valor in [0, 1, [], '', True, 1, 3.14]])

# 4

print([str(numero) for numero in [1, 2, 3, 4]])

















