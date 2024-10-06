'''
any all

all() Retorna True se todos os elementos do iteravel sõa verdadeiros, ou se o iteravel esta vazio

print(all([1, 2, 3, 4,])) # True
print(all([0, 1, 2, 3, 4]))# false

nomes = ['carlos', 'camila', 'cristiano']
print(all([nome[0] == 'c' for nome in nomes]))

print(all(letra for letra in 'eiou' if letra in 'aeiou')) # true

print(all([num for num in [2, 4, 6, 8, 10, 12] if num % 2 == 2]))

any() Retrona TRue se qualquer elemento do iteravel for verdadeiro, se o iteravel estiver vazio retorne False

print(any([0, 1, 2, 3, 4])) # True

print(0, False, (), {}, []) # False
'''




