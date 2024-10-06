from random import randint

def titulo():
    print("""
    Gerando senhas, numéricas""")



def Gerador_senha():
    senha = (1, 100)
    return senha


def nova_senha():
    while True:
        try:
            you = input('Digite "sim" se quiser uma senha numérica : ')
            if you == 'sim':
                print(f' Sua nova senha é {Gerador_senha()}')
            else:
                print('Ok')
        except ValueError as err:
            print('Digite sim se quiser uma senha')


titulo()
Gerador_senha()
nova_senha()


