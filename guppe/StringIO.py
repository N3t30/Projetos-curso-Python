'''
StringIO
ATENÇÃO     para ler ou escrever dados em arquivos do sistema o software precisa ter permição
permissão de leitura -> para ler
permisssão de escrita -> para escrever o arquivo

stringIO -> utilizado para ler e criar asquivos em memoria
primeiro fazemos o import
from
# primeiro fazemos o import
from io import StringIO

mensagem = 'string normal'

arquivo = StringIO(mensagem)
print(arquivo.read())
arquivo.write(' Outro arquivo')
arquivo.seek(0)
print(arquivo.read())
'''
from random import randint
from time import sleep

item2 = randint(0, 2)
item1 = ('pedra', 'papel', 'tesoura')

print('''SEJA BEM VINDO AO JOKENPO''')
print('-=' * 10)
print('''
SUAS OPÇÕES
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

print('-=' * 10)

jogador = int(input('Qual a sua opção? :'))
print('-=' * 10)

print(f'O jogador escolheu {item1[jogador]} ')
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

computador = randint(0, 2)
print(f'O computador escolheu {item1[computador]}')
print('-=' * 10)


if computador == 0:
    if jogador == 0:
        print('EMPATADOS')
    elif jogador == 1:
        print('VOCE VENCEU')
    elif jogador == 2:
        print('CPU VENCEU, VOCE É RUIM')
    else:
        print('JOGADA INVALIDA')

elif computador == 1:
    if jogador == 0:
        print('CPU VENCEU, VENCEU É RUIM ')
    elif jogador == 1:
        print('EMPATADOS')
    elif jogador == 2:
        print('VOCE VENCEU')
    else:
        print('JOGADA INVALIDA')

elif computador == 2:
    if jogador == 0:
        print('VOCE VENCEU')
    elif jogador == 1:
        print('VOCE PERDEU, VOCE É RUIM')
    elif jogador == 2:
        print('EMPATADOS')
    else:
        print('JOGADA INVALIDA')

















