'''
Criando sua propria versão de loops


'''
def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

meu_for('Neto Peixoto')

numeros = [1, 2, 3, 5, 4, 20, 12]
meu_for(numeros)