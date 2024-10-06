"""
poo - objetos
Objetos -> são instancias de classes, ou seja, após o mapeamento de objeetos do mundo real para a sua representação
computacional, devemos poder criar quantos objetos forem necessarios, podemos pensar nos objetos de uma classe como
variaveis do tipo definifo na classe


# Instancias
lamp1 = Lampada('Branca', 110, 60)

lamp1.ligar_desligar()
print(f'A lampada esta ligada? {lamp1.checa_lampada}')

cc1 = ContaCorrente(5000, 2000)
user = Usuario('neto', 'peixoto', 'josen@gmail.com', 15425)

print(lamp1)

"""

class Lampada:

    def __init__(self, cor, luminosidade, voltagem):
        self.__cor = cor
        self.__luminosidade = luminosidade
        self.__voltagem = voltagem
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


class Cliente:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz(self):
        print(f' O cliente é `{self.__nome}, diz oi')


class ContaCorrente:

    contador = 5000

    def __init__(self, saldo, limite, Cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__saldo = saldo
        self.limite = limite
        self.__Cliente = Cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'O cliente é {self.__Cliente._Cliente__nome}')


class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


cli1 = Cliente('josé peixoto', '482.468.254-52')

cc = ContaCorrente(5000, 20000, cli1)

print(cc.mostra_cliente())
