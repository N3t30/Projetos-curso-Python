import math

print(' Digite a Altura de um degrau')
degrau = int(input())

print(' Agora digite a altura que voce deseja alcançar')
Altura = int(input())

Resultado = math.ceil (Altura / degrau)
print(f' A quantidade de degraus é {Resultado}')
