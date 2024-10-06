'''
listas

listas em pythion funciona como vetores/matrizes com a diferencia de serem dinamicos

Linguagens c/javas arreys
    possuem tamanho e tipo de dado fixo
    ou seja, nessas linguagens se vc criar um arrey do tipo int e com tamanho 5
    este arrey sera sempre do tipo inteiro e poderar ter sempre no maximo 5 valores

Já em python


- dINÂMICO ; não ppssiu tamanho fixo; ou seja podemos criar a lisrtae simplesmente ir adicionando elementos
- Qualquer tipo de dado, as listas não possuem tipo de dado fixo ou sej apodemos colocar qualquer tipo de dado
- As listas em python são representadas por colchetes []

Lista1 = [1, 33, 45, 54, 68, 32, 84, 54, 25]

Lista2 = ['n', 'e', 't', 'o', '', 'p', 'i', 'x', 'o', 't', 'o']

Lista3 = []

Lista4 = list(range(11))

Lista5 = list('Neto peixoto')

# Podemos facilmente checar se um derteminadpo valor esta contido na listanum =
num = 58
if num in Lista4:
    print(f'achei o {num}')
else:
    print('não achei o numero')

pop \remove o ultimo elemnento da lista

# podemos facilmnete ordenar uma lista
Lista1.sort()
print(Lista1)

# podemos facilmente contar o numero de ocorrencias de um valor em uma lista
print(Lista1.count(32))
print(Lista5.count('o'))

# adcionsr elementos em listas, utilixamos a função append

OBS com appemd, nós condeguimos adcionar um elemento por vez

print(Lista1)
Lista1.append(58)
print(Lista1)

# Atençao com append, nós so conseguimos adcionar um elemento por vez
# Lista.append[12, 21, 32]


Lista1.append([12, 21, 32]) # coloca a lista como elemento unico [sublista]
print(Lista1)
if [12, 21, 32] in Lista1:
    print('Encontrei')
else:
    print('não encontrei')

Lista1.extend([35, 54, 68]) # coloca cada eleneto da lista como valor adicional a lista


# podemos inserir um novo elemento na lista informando a posição do índice
# isso não substitui o valor inicial, O mesmo será descolocaso para a direita da lista

Lista1.insert(5, 'valor novo')
print(Lista1)
 # podemos facilmente juntar duas listas

# Lista6 = Lista1 + Lista4
Lista1.extend(Lista2)
print(Lista1)

# podemos facilmente inverter uma lista utilizando o reverse
Lista1.reverse()
print(Lista1)

# copiar uma lista

Lista5 = Lista1.copy()
print(Lista5)

# podemos contar quantos elementos existem dentro de uma lista
print(len(Lista1))

# podemos facilmnete remover ouktimo elemento de uma lista elemento de uma lista
print(Lista5)
Lista5.pop()
print(Lista5)

# podemos remover um elemneto pelo índice
# os elementos a direita deste indice serão deslocados para a esquerda
# se não ouver elemento no indice informado teremos o erro
Lista5.pop(2)
print(Lista5)

# podemos remover todos os elementos ( zerar uma lista )
print(Lista5)
Lista5.clear()
print(Lista5)

# podemos facilmente repetir elementos de uma lista
nova = [65, 98, 25]
print(nova)
nova = nova * 3
print(nova)


# podemos facilmente converter uma string para uma lista
# Exemplo 1
# por padrão, o split separa os elementos da lista pelo espaço entre elas.

curso = 'Programação em python essencial'
print(curso)
curso = curso.split()
print(curso)

# Exemplo 2

curso = 'Programação,em,python,essencial'
print(curso)
curso = curso.split(',')
print(curso)

# convertendo uma lista em string
LIsta6 = ['programaçãp', 'em', 'python', 'essencial']
print(LIsta6)
# abaixp estamos falando: pega lista6, coloca espaço emtre cada elemento e transforma em uma string
curso = ' '.join(LIsta6)
print(curso)

curso = '$'.join(LIsta6)
print(curso)

# podemos realmente colocar qualquer tipo de dado em uma lista
Lista7 = ['string', [1, 2, 1], True, 4545646]

# iterando sobre listas

# Exemplo 1
soma = ' '
for elemento in Lista5:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplpo 2
carrinho = []
produto = ''

while produto != "sair":
    print('Adicione um produto no carrinho ou Digite "sair" para sair.')
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# em listas fazemos acesso aos elementos de forma indexada
# fazer acesso aos elementod de forma indexada inversa
print(cores[0])

cores = ['verde', 'azul', 'bramco', 'preto']
print(cores[1])
print(cores[2])
print(cores[3])

cores = ['verde', 'azul', 'bramco', 'preto']

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

cores = ['verde', 'azul', 'bramco', 'preto']

# gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

# listas aceitam valores repetidos

lista = []
lista.append(45)
lista.append(54)
lista.append(98)
lista.append(65)
lista.append(65)
print(lista)

# metotodos nãoi tão importante mas também uteis

# encontrar o indice de um elemento na lista

numeros = [4, 5, 6, 6, 2, 10, 362, 12, 5, 6]

print(numeros.index(5))

# podemos fazer busca dentro de um range, ou seja, qual indice começar a buscar
print(numeros.index(5, 1))

# podemos fazer busca dentro de umn range, inicio/fim
print(numeros.index(12, 6, 9))

# Revisão de slecing

# lista(inicio:fim:passo)
# range(inicio:fim:passo)

# trabalhando com slice em lista com o paramentro "inicio"

lista = [5, 6, 5, 5]
print(lista[1:]) # iniciando no indice 1 e pegando todos os elementos restantes

# trabalhando com slice em lista com o paramentro "fim"

print(lista[:2])  # começa em 0, pega ate o indice 2 - 1

print(lista[:4]) # começa em 0, pega ate o indice 4 - 1

# trabalhando com slice em lista com o paramentro "passo"

print(lista[1::2]) # começa em 1, vai até o final, de 2 em 2
print(lista[0::2]) # começa em 0, vai até o final de 2 em 2

# invertendo valores em uma lista
nomes = ['neto', 'peixoto']
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

nomes = ['neto', 'peixoto']
nomes.reverse()
print(nomes)

# soma, preocurar o valor maximo, procurar o valor minimo e tamanho
# se os valores forem todos inteiros ou reais

lista = [25, 65, 25, 98, 78]
print(max(lista))  # valor maximo
print(min(lista))  # minimo
print(sum(lista))  # soma
print(len(lista))  # tamanho da lista

# transforma uma lista em tupla

lista = [25, 65, 25, 98, 78]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# desenpacotamento de lista

lista = [1, 2, 3]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

# se tivermos mais elemnetos para desenpacotar do que variaveis para receber os valores, teremos error

# copiando uma lista para outra ( shalloe copy e deep copy)
# forma 1 deep copy: não afeta a lista antiga

lista = [1, 2, 3]
print(lista)

nova = lista.copy()
print(nova)

nova.append(5)
print(lista)
print(nova)

# forma 2: shallow copy: afeta a lista antiga

lista = [1, 2, 3]
print(lista)

nova = lista

nova.append(4)

print(lista)
print(nova

'''































