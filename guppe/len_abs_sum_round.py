"""
len, abs, sum, round

# len
len() -> retorna o tamanho (ou seja, o numero de um iteravel)

print(len('neto peixoto'))
print(len([1, 2, 3, 63, 3 ]))

# por de baixo dos panos, quando utilizamos a função len o  python faz o seguinte

print('neto peixoto'.__len__())

# abs()
ela retorna o valor absoluto de um nuumero inteiro ou real,

print(abs(5))
print(abs(8))
print(abs(5.25))

sum() -> Recebve como parametro um iteravel, podendo receber um valor inicial, e retorna a soma total dos elementos

print(sum([1, 2, 3, 4, 5, 5]))
print(sum([1, 2, 5, 6, 5, 5], 8))
print(sum({'a': 1, 'b': 8, 'c': 48, 'd': 58}.values()))

round-> Retorna um numero arrdondado para n digitos de precisão após a casa decimal, se a precisão não for
imformada retorna o inteiro mais proximo da entrada

print(round(15.5))
print(round(58.219999))
print(round(18.12))

"""






