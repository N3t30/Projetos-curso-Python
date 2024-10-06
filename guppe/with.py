'''
O Bloco with
# passo para se trabalhar com arquivos
1 - abrimos o arquivo
2 - manipulamos o arquivo
3 - fechamos o arquivo

O bloco with é utilizado para criar um contexto de trabalhos onde os recursos de trabalhos
após o bloco with
'''
# O bloco with -> È a forma pythonica de se utilizar para manipular arquivo

with open('texto.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)

print(arquivo.closed) 
# print(arquivo.readlines())