'''
list comprehension
 Nós podemos adicionar estryuturas condicionais lógicas as nossas listas comprehensions

'''

numeros =  [1, 2, 3, 4, 5, 6, 7]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

# perfomace

# Qualquer numero por modulo de 2 e 0 é 0 em python é false, not false é True
pares = [numero for numero in numeros if not numero % 2 == 0]

# Qualquer numero impar modulo de 2 é 1,  e 1 em python é True
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

# 2
res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)















