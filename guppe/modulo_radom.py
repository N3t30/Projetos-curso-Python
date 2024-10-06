'''
Modulo Radom e o que são modulos
 - Em python, modulos nada mais são do que outros aqruivos python

radom modulo Random = possue varias funções para gerações de numeros aleatorios

# OBS: Existem duas formas de se utilizar modulo ou função deste

# forma 1 - importando todo o modulo. (não recomnedado)

import random

# random() -> Gera um numero aleatorio entra 0, 1

# Ao realizar o import de todo o modulo, todas as funçoes, atributos, classes e porpriedades que estiverem
# dentro do modulo ficaram disponiveis, ficaram em menoria, caso voce saiba quias funçoes voce precisa utilizar
# deste modulo, então esta não seria a forma ideal de utilização, tem uma forma melhor

print(random.random())

# Veja que para utilizamos a função os random estão separadas por pontos
# OBS: nÃO COMFUNDÃO a funçao random com o pacote random

# forma 2 - importando uma função especifica do módulo
# FORMA RECOMENDADA

from random import random

for i in range(10):
    print(random())

# uniform() -> Gerar um numero real pseudo.aleatorio entre os valores estabelecidos

from random import uniform

for i in range(10):
    print(uniform(5, 10)) # não inclui o 10


# randint -> Gera valores aleatorios entre os valores estabelecidos

from random import randint
# Gerador de apostas

for i in range(6):
    print(randint(1, 61), end=', ') # comeca em 1 e vai até 60

# choice() -> mostra um valor aleatorio entreum iteravel

from random import choice

jogadas = ['pedra', 'papel', 'tesouras']

print(choice(jogadas))
'''

# shuffle() -> tem a função de embaralhar dados

from random import shuffle

cartas = ['k', 'Q', '10', 'j', '8']
print(cartas)
shuffle(cartas)

print(cartas)





