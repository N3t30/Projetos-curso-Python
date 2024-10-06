'''
seek e cursors
seek()-> é utilizada para movimentar o cursor pelo o arquivo

print(arquivo.read())

# Seek() -> serve para movimnetação do cursor pleo arquivo ela recebe um parametro que indica
# onde queremos o cursor

# Movimentando o cursor pleo arquivo com seek() => precurar em qual caractere quero iniciar

arquivo.seek(0)
print(arquivo.read())

arquivo.seek(26)
print(arquivo.read())

# readline() -> função de ler o arquivo de linha a linha

ret = arquivo.readline()
print(type(ret))
print(ret)

print(ret.split(' ')) # transformando em lista

# readlines()

linhas = arquivo.readlines()

print(len(linhas))

OBS: quando abrimos o arquivo com a função open eé criada uma conexão entre o arquivo e o seu programa
essa conexão é chamada de streaming, ao finalizar os trabalhos com os arquivos devemos fechar essa conexão com o close()
passos para trabalhar com arquivos

1 - Abrir o arquivo
2 - trabalhar o arquivo
3 - fechara o arquivo

arquivo.clos()

print(arquivo.read())

print(arquivo.closed) # False se o arquivo estiver aberto, True  se o arquivo estiver fechado
arquivo.close()
print(arquivo.closed)

print(arquivo.read()) # Após fechamento retorna um ValueError

'''
arquivo = open('texto.txt')

print(arquivo.read(60)) # limitando os caracteres com o read 



