"""
ADIVINHE O NUMERO QUE ESTOU PENSANDO
"""
from os import system
from time import sleep
from random import randrange
import os


# TITULO
def titulo():
    print('-=' * 10)
    print(""""O MENTALISTA""")
    print('-=' * 10)

def Gerador_numerico():
    numero_gerado = randrange(1, 101)
    return numero_gerado


def Mentalista(numero, tentativas):
    while True:
        try:
            chute = int(input('Digite um numero entre 1 e 100 e tente adivinhar em qual estou pensando.\n Resposta : '))
            if chute > 100 or chute < 1:
                sleep(1)
                tentativas += 1
                print('Digite um numero entre 1 e 100')

            elif chute > numero:
                sleep(1)
                print(f'\n O numero que pensei é menor que, {chute}')
                tentativas += 1
                print('Tente outra vez...')

            elif chute < numero:
                sleep(1)
                print(f'\n O numero que pensei é maior que {chute}')
                tentativas += 1
                print('Tente outra vez...')

            elif chute == numero:
                sleep(1)
                tentativas += 1
                print(f'PARABENS, voce acertou com {tentativas} tentativas o numero que eu estava pensando')
                sleep(1)
                opcao = (input('Quer jogar outra vez?  (s/n): '))
                if opcao.lower() == 's':
                    print('\nReiniciando o jogo...')
                    sleep(3)
                    numero = Gerador_numerico()
                    tentativas = 0
                    os.system('cls')
                    titulo()
                    continue
                elif opcao.lower() == 'n' or 'nao':
                    sleep(2)
                    print('Ok, obrigado por jogar')
                    break
        except ValueError as err:
            print('Digite um numero inteiro')
            sleep(1)

titulo()
input('Digite "OK" para comecar o GAME')
numero = Gerador_numerico()
tentativas = 0
Mentalista(numero, tentativas)