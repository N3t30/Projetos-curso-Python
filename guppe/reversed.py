'''
reversed
OBS: não confunda com a função reverse() que estudamos em listas

a função reverse so funciona em listas

ja a função reversed() funciona com qualquer iteravel
sua função é inverter o iteravel
'''

listas = [3, 3, 2, 3, 3]

res = reversed(listas)
print(res)
print(type(res))

print(list(reversed(listas)))

print(tuple(reversed(listas)))

print(set(reversed(listas)))

