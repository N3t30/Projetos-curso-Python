



'''
Conjuntos
 - conjuntos em qualquer linguagem de programação, estamos fazendo referencia a teoria dos conjuntos de matematica

 _ Aqui no python o conjuntos são chamados de Sets.

Disto isso da mesma forma que em matematica

 - Sets (conjuntos) não possuem valores duplicados.
 - Sets (conjuntos) não possuem valores ordenados.
 - Elementos não são acessados via indice, ou seja, conjuntos não são indexados

 conjuntos são bons para se utilizar quando precisamos armazenar elementos
 mas não nos importamos com a cordenação deles, Quando não precisamos se preucupar com chaves, valores e itens duplicados

Os conjuntos (stes) são referencia em python com chaves {}

Diferencia entre conjuntos (Set) e mapas (dicionarios) em python
  - Um dicionario tem chave/valor
  - Um conjunto tem apenas valor

  # Definindo um conjunto
# forma 1

s = set({2, 5, 6, 3, 8, 2, 6}) # valores repetidos

print(s)
print(type(s))

# valor repetido sera ignorado

# podemos verificar se determinado eleento esta contido no coonjunto

if 3 in s:
    print('tem o 3')
else:
    print('não tem o 3')

# alem de não termos valores duplicados não temos ordem

# listas, tuplas e dicionarios seguem a ordem informada
# Ja o conjunto da uma ordem aleatoria

# listas aceitam valores duplicados
lista = [56, 36, 32, 32, 25, 98]
print(f'lista: {lista} com {len(lista)} elemnetos' )

# tupls aceitam valores duplicados
tupla = (56, 36, 32, 32, 25, 98)
print(f'tupla: {tupla}  com {len(tupla)} elemnetos ')

# Não aceitam cahves duplicadas
dicionario = {}.fromkeys([56, 36, 32, 32, 25, 98], 'dict')
print(f'dicinario: {dicionario}  com {len(dicionario)} elemnetos')

# conjuntos não aceitam valores duplicados
conjunto = {56, 36, 32, 32, 25, 98}
print(f'conjunto: {conjunto}  com {len(conjunto)} elemnetos' )

# assim como todo outro conjunto python podemmoos colocar tipos de dados misturados em sets
s = {1,'b', True, 35.58, 44}
print(s)
print(type(s))

# podemos iterar em um set normalmente
for valor in s:
    print(valor)


# imagine que fizemos um formulario de visitantes em um museu e os visitantes informam normalmente a cidade de onde
# vieram
# Nós adicionamos cada cidade em uma lista python, ja que em uma lista podemos adicionar novos elementos
# e ter repetição

cidades = ['belo horizonte', 'são paulo', 'campo grande', 'são paulo', 'rio de janeiro', 'campo grande']
print(cidades)
print(len(cidades))

# Agora precisamos saber qunatas cidades distintas, ou seja, unicas
# podemos utilizar o set paara isso

print(len(set(cidades)))

# Adicionando elementos em um conjunto
s = {2, 6, 3}

s.add(5)
s.add(5) # Não podemos adicionar o mesmo numero e não gera erro
print(s)

# remover elemento
s = {2, 6, 3}
print(s)
# forma 1
s.remove(6) # não é indice, conjuntos não são indexados e nenum valor é retornado
print(s)

# forma 2
s.discard(3)
print(s)

# copiando um conjunto para outro
s = {2, 3, 8,}
print(s)

# forma 1 - deep cpý
novo = s.copy()
print(novo)

novo.add(5)

print(novo)
print(s)

# forma 2 - shallow copy
sallow = s
sallow.add(5)

print(sallow)
print(s)

s = {2, 3, 8}
print(s)

# podemos remover todos os items de um conjuntos

s.clear()
print(s)

# metodos matematicos de conjuntos
# imagine que temos dois conjuntos um contendo estudantes de python e java
# precisamos gerar um conjunto com nomes de estudantes unicos

estudantes_python = {'Lucas', 'Lusn', 'Pedro', 'Gui', 'Neto', 'fabio', 'Dalia'}
estudantes_java = {'Lucas', 'carlos', 'junior', 'Gui', 'Neto', 'zé', 'Dalia'}

# forma 1
# utilizando union

todos = estudantes_java.union(estudantes_python) # ou vice e versa
print(todos)

# forma - utilizando o caractere pipe |
todos_2 = estudantes_java | estudantes_python
print(todos_2)

# Gerar um conjunto de estudantes que estão em ambos os cursos

# forma 1 - utilizando intersection

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# forma 2

ambos1 = estudantes_python & estudantes_java
print(ambos1)

# Gerar um conjunto de estudantes que não estão no outro curso
# usando difference

python = estudantes_python.difference(estudantes_java)
print(f'Só python{python}')

java = estudantes_java.difference(estudantes_python)
print(f' Só java {java}')

# soma*, valor max*, valor min* e tamanho
# se os valores forem todos inteiros ou reais

s = {2, 6, 5, 8, 3, 7, 4}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))
'''

















