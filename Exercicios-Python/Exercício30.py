print(' Digite um valor a ser depositado em Reais ')
valor = float(input())

print(' agora digite a cotação do dolar atualmente')
Cotação = float(input())

conversão = valor * Cotação
print(f' O valor ddepositado em Reais {valor}, corresponde a {round(conversão,2)} de dólares')


