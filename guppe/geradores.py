'''
GERADORES

 - GERADORES são iterators ( iteradores )

OBS: O contrariop não é verdadeiro, ou seja, nem todo iterator é um generator.
- generators podem ser criados com funções geradoras :
- funções geradoras utilizam a palavra reservada yield :
- Generators podem ser ciradas com Expressões geradoras :

diferencias entre funções e Generator functions ( funções geradoras )


FUNÇÕES -> utilizam Return, retorna uma vez, quando executada retorna um valor

GENERATOR FUNCTIONS -> utilizam yield, podem utilizar yield multiplas vezes, quando  executada retorna um valor

gem = conta_ate(5)

print(next(gem))
print(next(gem))


for num in gem:
    print(num)

'''

# Exemplo de Generator functions

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1

# OBS: uma Generator functions não é um Generator, ela gera um generator
gem = conta_ate(5)

