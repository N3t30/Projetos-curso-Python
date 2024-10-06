'''
min e max

max() retorna o maior valor em um iteravel ou um maior de dois ou mais elementos


lista = [1, 20, 65, 25, 25, 52]
print(max(lista))

tupla = (1, 20, 65, 25, 25, 52)
print(max(tupla))

conjunto = {1, 20, 65, 25, 25, 52}
print(max(conjunto))

dicionario = {'a': 1, 'b': 20, 'c': 65, 'd': 25, 'e': 25, 'f': 52}
print(max(dicionario))

# faça um programa que receba dois valores do usuario e mostre o maior
valor1 = int(input('imforme sua idade Gabriel'))
valor2 = int(input('informe sua idade Desconhecido'))

if valor1 < valor2:
    print('Gabriel voce é mais novo')
else:
    print('Gabriel voce é mais velho')


valor1 = int(input('imforme sua idade Gabriel'))
valor2 = int(input('informe sua idade Desconhecido'))

print(max(valor1, valor2))

min() -> REtorna o menor valor em um iteravel ou o menor entre dois ou mais elementos


# Exemplos
nomes = ['Aria', 'juilos', 'tim', 'yu']
print(max(nomes))

print(min(nomes))

print(max(nomes, key=lambda nome: len(nome)))

print(min(nomes, key=lambda nome: len(nome)))


'''































