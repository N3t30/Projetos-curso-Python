'''
moduclo clollections - default Dict

# Recap Dicionarios

dicionario = {'curso': 'python'}
print(dicionario)
print(dicionario['curso'])
# Gerar uma chave que não existe gera o keyerror

Default Dict -> ao criar um dicionario utilizando-o, informamos um valor default,
podendo utilizar um lanbda para isso, este valor sera utilizado sempre que não houver
um valor definido, caso tentaemos acessar uma chave que não exista, essa chave sera criada e o valor
default sera atribuido
OBS -> lambda são funções sem nome, que podem ou nçao receber parametros de entrada
e retona valores
'''

# fazando o import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)
dicionario['curso'] = 'python'
print(dicionario)
print(dicionario['outro'])
print(dicionario)
















