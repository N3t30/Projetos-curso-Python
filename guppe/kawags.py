"""
**kawaegs
Poderiamos chmar de qualquer nome

Este é so mais um parametro mas diferente do args que coloca os valores extras en uma tupla
o ** exige que utilizemos paramnetros nomeadps e transforma esses paramnetros extras em dicionario

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')

cores_favoritas(marcss='Azul', alyce='preto', julio='rosa', neto='vermelho')

# OBS : Nem os parametros args e **kwargs não são obrigatorios

# Nas nossas funções podemos ter, (Nesta ordem)
- parametros obrigatorios
- *args
- Parametros não obrigatorios
- **kwargs

# Entendendo porquer a impoetancia das ordem dos parametros é importante3

def mostra_info(a, b, *args, instrutor='Geek', **kwargs ):
    return 1, 2, 3, instrutor, kwargs

print(mostra_info(1, 2, 3, sobrenome='neto', cargo='instrutot' ))

# desempacotar com **kwargs
def mostra_nome(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'neto', 'sobrenome': 'peixoto'}
print(mostra_nome(**nomes))

print(mostra_nome(**nomes))

def soma_multipla(a, b, c, **kwargd):
    print(a + b + c)

lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

soma_multipla(*lista)
soma_multipla(*tupla)
soma_multipla(*conjunto)


dicionario = dict(a=1, b=2, c=3)
soma_multipla(**dicionario)  # OBS : dicionarios tem que ser com dois **

soma_multipla(**dicionario, lang='python')
"""















