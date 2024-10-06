'''
funções com paramnetros ( de entrada )

- funções que recebem dados para serem processados dentro da mesma.

se agente pensar em um programa qualquer, temos:
 emtrada -> processamneto -> saida
 - Não possuem entrada.
 - Não possuem saida.
 - Possuem entrada mas não possuem saida
 - Não possuem entrada mas possuem saida
 - Não possuem entrada não possuem saida
 - Possuem entraad e saida

# refatorando função
def quadrado(numero):
    # return numero * numero
    return numero ** 2

print(quadrado(8))
print(quadrado(8))
print(quadrado(2))

def cantar_parabens(nome):
    print('parabens para voce')
    print('nesta data querida')
    print('muitas felicidades')
    print('muitos anos de vida')
    print(f'viva o {nome}')

print(cantar_parabens('Neto!'))


# funções podem ter n parametros de entrada, ou seja, podemos receber como entrada
# em uma função quantos parametros fore necessarios, elas são separados por virgula

# Exemplo

def soma(a, b):
    return a + b

def multiplicação(a, b):
    return a * b

def outra(num1, num2, msgm):
    return (num1 + num2) * msgm

print(soma(5, 6))
print(soma(5, 9))

print(multiplicação(8, 6))
print(multiplicação(8, 4))

print(outra(8, 6, 'python '))
print(outra(2, 6, 'neto '))

# OBS se agente informar um numero errado de parametro ou argumento, teremos error

# print(soma(1, 2, 5)) # typeerror -> passando argumnetos a mais
    print(soma(1)) # type error -> passando argumentos a menos

# nomeando parametros

def nome_completo(nome, sobrenome):
    return f' seu nome completo é {nome} {sobrenome}'


# A diferencia entre paramentros é argumentos
# paramnetros são variaveis declaradas na defiunição de uma função
# Argumnetos são dados pessoais durante a execução de um função

# A ordem dos parametros importa
# Argumentos nomeados

nome = 'josé'
sobrenome = 'peixoto'

# caso utilizemos nomes nome dos parametros mos argumentos para imforma-los, podemos
# utilizar qualquer ordem

print(nome_completo(nome='josé', sobrenome='peixoto'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome='peixoto', nome='Neto'))
'''

# Erro comum na utilização do return

def impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total

if __name__=='__Main__':
    tupla = (2, 3, 6, 5, 3, 6, 5)
    print(impares(tupla))



















