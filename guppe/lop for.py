''' loop for'''

qtd = int(input( ' imforme quantas vezes esse loop deve rodar ?'))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'imforme o {n}/{qtd} valor'))
    soma = soma + num
print(f' A soma é {soma}.')

