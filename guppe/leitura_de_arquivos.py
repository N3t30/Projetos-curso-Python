'''
Leituras de arquivos

para ler o conteudo em python utilizamos a função integrada open()
"Abrir":

open() -> A forma mais simples de utilização nos passamos apenas um parametro de entrada
nome do arquivo a seer lidp essa função retorna um IO.textIOrapper e é com ele que trabalhamos então

https://docs.python.orgs/3/library/functions.html#open
obs: POr padrão a função open abre o arquivo para leitura, este arquivo
ddve existir, ou então teremos o erro filenotfoundError

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>

mode r -> sigunifica leitura, r -> read() -> ler

'''

arquivo = open('texto.txt')

#print(arquivo)

#print(type(arquivo))
# para ler um conteudo de um arquivo depois da abertura devemos usar a função read()

print(arquivo.read())

# OBS: o python utiliza um recurso para trabalhar com arquivos chamado cursor
# funciona como o cursor quando escrevemos

# ONS: a função read ler todo o conteudo do arquivo
