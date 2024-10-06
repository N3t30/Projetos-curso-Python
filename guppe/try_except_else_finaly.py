'''
try /  except / else / finally

dica de quando e onde tratrar codigo

TODA ENTRADA DEVE SER TRATATDA!

# else é executada somente se não ocorrer o erro.

try:
    num = int(input("Digite um numero"))
except ValueError:
    print('valor incorreto')
else:
    print(f'voce digitou o numero {num}')

try:
    num = int(input("Digite um numero"))
except ValueError:
    print('valor incorreto')
else:
    print(f'voce digitou o numero {num}')
finally:
    print('Executando o finally')

# OBS: o bloco finally é sempre executado, independente se houver execução ou não

# O blovo finally, geraçmnete, é utilizado para fechar ou deslocar recursos.

# Exemplos mais complexo ERRADO


def dividir(a, b):
    return a / b

num1 = int(input('Digite um numero'))
try:
    num2 = int(input('Digite o segundo numero'))
except ValueError:
    print('O valor precisa ser numérico')

try:
    print(dividir(num1, num2))
except NameError:
    print('valor incorreto')

# Exemplos mais complexo CORRETO
# OBS: voce é responsavel pelas entradas da suas funções, então, trate_as!

def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'valor incorreto'
    except ZeroDivisionError:
        return 'Não é posiivel ralizar uma divisão por zero'


num = input('Digite um numero')
num2 = input('Digite o segundo numero')

print(dividir(num, num2))

'''
# Exemplos mais complexo CORRETO
# OBS: voce é responsavel pelas entradas da suas funções, então, trate_as!

def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'valor incorreto'
    except ZeroDivisionError:
        return 'Não é posiivel ralizar uma divisão por zero'


num = input('Digite um numero')
num2 = input('Digite o segundo numero')

print(dividir(num, num2))