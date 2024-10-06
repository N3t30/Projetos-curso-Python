'''
Escrevendo em arquivos

OBS: Ao abrir um arquivo para leitura, não podemos escrever apenas ler
e o verso

OBS: Ao abrir um arquivo para escrita o arquivo é criado no sistema

Para escrevermos dados em um arquivo após abrir um arquivo
utilizamos a função write(), esta função só recebe string

Abrindo um arquivo para escrita com o modo 'w' se não existir arquivo um novo será criado, caso ele ja exista o anterior
será apagado e um novo será criado, perdendo o conteudo do anterior

with open('novo,txt', 'w') as arquivo:
    arquivo.write('novos dados.\n')
    arquivo.write('outros parametros.\n')
    arquivo.write('terceira vez.\n')
'''
with open('pereciveis.txt', 'w') as arquivo:
    while True:
        produtosp = input('Digite seus produtos pereciveis ou sair: ')
        if produtosp != 'sair':
            arquivo.write(produtosp + '\n')
        else:
            break







