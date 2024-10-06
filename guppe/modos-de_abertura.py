'''
modos de abertura de arquivos

r -> Abre para leitura
w -> Abre para escrita
x -> Abre para escrita somente se o qrquivo não existir, caso o arquivo existir gera fileError
A -> Abre para escrita adicionando ao final do arquivo
+ -> Abre para o modo de atualização, leitura e escrita
OBS -> Abrindo com o modo "a" -> append, se o arquivo não existir será criado, caso exista, o novo conteudo
será adcionaado ao final.
# Exomplo 'x'
try:
    with open('modox.txt', 'x') as arquivo:
        arquivo.write('testando arquivo.\n')
except FileExistsError:
    print('esse arquivo ja existe')

# Exomplo "a"

with open('pereciveis.txt', 'a') as arq:
    while True:
        perecivel = input('Digite seus produtos pereciveis ou sair: ')
        if perecivel != 'sair':
            arq.write(perecivel)
            arq.write('\n')
        else:
            break
'''





