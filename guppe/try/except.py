'''
o bloco try/excepet

utilizamos o bloco try/except pára testar erros que podem ocorrer em nosso codiog pevinindo assim que
o programa pare de funcionar e o usuario receba msgns de erros inesperadas

 A forma geral mais simples

try:
    //execusão problematica
wxcept
    //o que deve ser feito em caso de problema

# Exemplpo 1 - trantando um erro genérico

try:
    geek()
except:
    print('deu algum problema')

# tratar erro de forma genérica não é ideal
sempre tratar de forma especifica


# Exemlpo 1 trantando um erro especifico

try:
    geek()
except NameError:
    print('voce se está utilizando uma função inexistente')

# Exemlpo 2 trantando um erro especifico

try:
    len(5)
except TypeError:
    print('voce se está utilizando uma função inexistente')

# Exemlpo 3 trantando um erro especifico
try:
    len(5)
except TypeError as err:
    print(f'a aplicação gerou um {err}')

# podemos efetuar varios traramentos de erros em uma fubção

try:
    # len(5)
    geek()
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu typeError: {errb}')
'''


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None

dic = {"bome": "neto"}

print(pega_valor(dic, 'alfredo'))




