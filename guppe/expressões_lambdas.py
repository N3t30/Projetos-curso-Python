'''
utilizando lambdas

conhecidas por expressões lambdas são funções sem nome ou seja, funcões anonimas

# Exemplo de função

def função(x):
    return 3 * x + 1

print(função(8))
print(função(25))

# Exemplo de expressão lambda
lambda x: 3 * x + 1

# como utilizar a expressão lambda
calc = lambda x: 3 * x + 1
print(calc(8))
print(calc(25))


# podemos ter expressões lambdas com multplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + '  ' + sobrenome.strip().title()

print(nome_completo( '  angelina', ' jolie'))

# Em funções python podemos ter nenhuma ou varias entradas em lambdas tambem

amar = lambda: 'como não amar python'

uma = lambda x: 3 * x +1

duas = lambda x, y: (x * y) ** 0.5

tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

print(amar)
print(uma(9))
print(duas(5, 7))
print(tres(4, 5, 9))

# outros exemplos

Autores = ['isac anov', 'sebastian wilton', 'pedro raul', 'juilano rainho', 'david D. souza', 'ruan C. arlindo',
           'silvano sales cantor']
print(Autores)


Autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(Autores)

'''

# função quadratica
# f(x) = a * x ** 2 + b* x + c

def função_quadratica(a, b, c):
    """Retorna a função f(x) = a*x**2 + b * x + c"""
    return lambda x: a * x ** 2 + b * x + c

teste = função_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))

print(função_quadratica(3, 5, 4)(5))















