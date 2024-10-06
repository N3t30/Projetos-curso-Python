'''
escrevedno um iterador customizado

class contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration

for n in contador(1, 58):
    print(n)

with open('abrir.4', 'w') as arquivo:
    while True:
        produtos = input('Adiocone seus produtos ou sair')
        if produtos != 'sair':
            arquivo.write(produtos)
            arquivo.write('\n')
        else:
            break
'''
from random import randint
from time import sleep

item = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''SUAS OPÇÕES:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')
jogador = int(input('Qual a sua jogada? : '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')


print('-=' * 10)
print(f' O computador jogou {item[computador]}')
print(f' O jogador jogou {item[jogador]} ')
print('-=' * 10)

if computador == 0:
    if jogador == 0:
        print('EMPATADOS')
    elif jogador == 1:
        print('VOCE VENCEU')
    elif jogador == 2:
        print('CPU GANHOU, VC É RUIM')
    else:
        print('jogada imvalida')

elif computador == 1:
    if jogador == 0:
        print('CPU GANHOU, VOCE É RUIM')
    elif jogador == 1:
        print('EMPATADOS')
    elif jogador == 2:
        print('VOCE VENCEU')
    else:
        print('JOGADFA INVALIDA')

elif computador == 2:
    if jogador == 0:
        print('VOCE VENCEU')
    elif jogador == 1:
        print('CPU GANHOU, VOCE É RUIM')
    elif jogador == 2:
        print('EMPATADOS')
    else:
        print('JOGADFA INVALIDA')





















