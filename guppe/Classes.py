"""
classes
Em POO. nada mais são do  que modelos dos objetos do mundo real sendo representados computacionalmente

- classes podem conter
    Atributos -> representam as caracteristicas dos objetos , ou seja, pelos
    atributos conseguimos os estados de um objeto, no caso da lampada possivelmente iriamos querer saber se a lampada é
    110v ou 220v, qual cor é a dela e qual é a luminosidade dela

    - metodos - funções
    Representam os comportamento do objeto, ou seja, as ações que esse objeto pode realizar como, ligar e desligar

CLASS :Em python para definir uma clase usamos o claa
PASS - utilizamos o pass em python quando temos um bloco de codigo que ainda não esta implementado

OBS ; quando nomeamos nossas classes em python utilizamos o nome com inicial em maiusculo

DICA : Em computaçãp nao colocamos acentecuação, caracteres, espacços ou sinais
para : classes, atributos, Arquivos, diretorio e etc

OBS :  Quando estamos criando um software e definindo quais classes teremos que ter no sistema, chamamos esses objetos

class lampada:
    pass
lam = lampada()
print(type(lam))
de entidade  
"""

from random import randint
from time import sleep


items = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print("""JOKENPO!!
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")
print('-=' * 10 )

jogada = int(input('Escplha uma opção : '))
try:
    jogador = print(f'Voce escolheu {items[jogada]}')
except IndexError:
    print('Valor incorreto')

sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')

CPU = print(f'O computador escolheu {items[computador]}')

if computador == 0:
    if jogada == 0:
        print('Empatados')

    elif jogada == 1:
        print('Voce ganhou')

    elif jogada == 2:
        print('Voce conseguiu perder para o pc')

    else:
        print('jogada invalida')


elif computador == 1:
    if jogada == 0:
        print('Voce conseguiu perder para o pc')

    elif jogada == 1:
        print('Empatados')

    elif jogada == 2:
        print('Voce ganhou')

    else:
        print('jogada invalida')


elif computador == 2:
    if jogada == 0:
        print('voce ganhou')

    elif jogada == 1:
        print('Voce conseguiu perder para o pc')

    elif jogada == 2:
        print("Empatados")

    else:
        print('jogada invaloda')




























