'''
listas aninhadas
- Algumas lingunagens de programação (c/java) possuem uma estrutura de dados chamaos de arrays
   - unidimensionais (Arrays/vetores)
   - multidimensionais (Matrizes)

Em python nós temos listas

numeros = [1, 2, 3, 4, 5, 6]

print(listas)
print(type(listas))

# como fazemos para acessar od dados ?
print(listas[0][1])
print(listas[2][1])

# iterando com loops em uma lista aninhada
for listas in listas:
    for num in listas:
        print(num)

# Exemplo
listas = [[1, 2, 3], [5, 6, 3], [78, 98, 65]]


# lists comprehensions

[[print(valor) for valor in lista] for lista in listas]
'''

# Gerando um tabuleiro/matrix 3x3

tabuleiro = [[numero for numero in range(1, 5)] for valor in range(1, 5)]
print(tabuleiro)

# Gerando jogadas jogo da velha
velha = [['X' if numero % 2 == 0 else'O' for numero in range(1, 5)] for valor in range (1, 5)]
print(velha)

#  GErando valores iniciais

print([['*' for i in range(1, 4)] for j in range(1, 4)])



























