'''
raise

# Exemplo real

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('texto precisa ser uma string')
    print(f'o tecto {texto} será {cor}')

colore('gekk', 'azul')

# refatorado

def colore(texto, cor):
    cores = ('vermelho', 'azul', 'preto', 'amarelo')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError (f' a cor precisa ser uma entre: {cores}')
    print(f'o tecto {texto} será {cor}')

colore('gekk', 'marrom')
'''



