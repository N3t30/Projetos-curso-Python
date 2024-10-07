import math

print('digite a Altura e o Raio de um cilindro circular')

print('Digite a Altura')
Altura = float(input())

print('Digite o Raio')
Raio = float(input())

Volume = math.pi * Raio** 2 * Altura
print(f' O volume do cilindro é {round(Volume)}')

