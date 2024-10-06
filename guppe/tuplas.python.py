
'''
tuplas - taple

tuplas são bastante parecidas com listas, existem basicamente duas diferencia
1 - As tuplas são representada por parenteses ()
2 - As tuplas são imutaveis, isso siguinifica que ao se criar uma tupla ela não muda,
toda operação em uma tupla gera uma nova tupla

# cuidad  1: as tuplas sõa representada por (), mas veja.
tuple = (1, 2, 5, 6, 4)
print(tuple)
print(type(tuple))

tuple1 = 1, 2, 8, 6, 6
print(tuple1)
print(type(tuple1))

# cuidado 2: tuplas com 1 elemento

tuple2 = (2) # isso não é uma tupla
print(tuple2)
print(type(tuple2))

tuple3 = (4,) # isso é uma tupla
print(tuple3)
print(type(tuple3))

# conclusõão, podemos concluir que tuplas sõa definidas pela virgula,
# e não pleo ()

# podemos gerar uma tupa dinamicamente com range(inicio, fim, passo)
tuple = tuple(range(11))
print(tuple)
print(type(tuple))

# desenpacotamento de tupla
tuple = ('Neto', 'peixoto')
nome, sobrenome = tuple

print(nome)
print(sobrenome)

# Gera valueerror se colocamos um numero diferente de elemento para desenpacotar

# Metodos para adição e remoção de elementos nas tuplas não existem, dado o fato das tuplsa serem amutaveis
# Soma, valor maximo, valor minimo, tamanho

tuple = (2, 65, 14, 36, 98)

print(sum(tuple))
print(min(tuple))
print(max(tuple))
print(len(tuple)) # numeros de caracteres

# comcatenação de tuplas

tupla1 = (1, 2, 3)
print(tupla1)


tupla2 = (2, 3, 5)
print(tupla2)

print(tupla1 + tupla2) # tuplas são imutáveis

print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2

print(tupla1)
print(tupla2)
print(tupla3)

tupla1 = tupla1 + tupla3 # tuplas são imutaveis mas podemos sobrescrever seus valores
print(tupla1)

# verificra se determinado elemento esta na lista

tuple = (2, 3, 6, 9, 8, 4, 1)
print(3 in tuple)

# iterando sobre uma tupla
tuple = (2, 3, 6, 9, 8, 4, 1)
for n in tuple:
    print(n)

for indice, valor in enumerate(tuple):
    print(indice, valor)

# contando elementos dentro de uma tupla
tupla = ('a', 'b', 'f', 'f')

print(tupla.count('f'))

escola = tuple('Geek universy')
print(escola)

print(escola.count('e'))

print(meses[1])  # acesso aos elementos de uma tupla

# itera com while

i = 0

while i < len(meses):
    print(meses[i])
    i = i + 1

# verificamos em qual indice um elemento esta na tupla

print(meses.index('junho')) # index = indice::: messes.index('junho', 5)  a partir de...

# dicas na utilização de tuplas

# Devemos utilizar tuplas sempre que não precisarnmos modificar os dados de uma coleção

meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

# slicing

# tupla[inicio.fim.passo]

print(meses[0:12]) # começa e vai até

# por que utilizar tuplas?

# - tuplas são mais rapidas do que listas
# - tuplas deixam seu codigo mias seguro
# - isso pq trabalhar com elementos imutaveis trazem mais segurança ao seu codigp

# copiando uma tupla para outra

tupla = (1, 2, 3)
print(tupla)

nova = tupla  # na tupla nçao temos o problema de shallow copy

print(nova)
print(tupla)

outra = (4, 5, 6)
nova = nova + outra
print(nova)
print(tupla)

'''





























