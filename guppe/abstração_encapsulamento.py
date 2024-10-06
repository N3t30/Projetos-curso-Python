"""
poo - ABstração e encapsulamento

O grande objetivo POO é encapsular nosso codigo dentro de um grupo lódico e hierarquico utilizando
classes

Encapsular -> capsula


print(conta1.__dict__)
conta1.extrato()

conta1.sacar(50)
conta1.extrato()
conta1.depósito(500)
conta1.extrato()
conta1.sacar(700)
print(conta1.__dict__)
"""

class conta:

    contador = 500                                  # atributos de classe

    def __init__(self, titular, saldo, limite):
        self.__numero = conta.contador
        self.__saldo = saldo
        self.__limite = limite                      # atributos de instancias
        self.__titular = titular
        conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo}, do titular {self.__titular}, com limite de {self.__limite}')

    def depósito(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('Deposito invalido')              # tres metodos de instancias

    def sacar(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
        else:
            print('saldo insuficiente')


    def transferir(self, valor, conta_destino):
        if self.__saldo >= valor:
            self.__saldo -= valor
            conta_destino.__saldo += valor
        else:
            print('Valor insuficiente')


# testando

conta1 = conta('Neto', 150.00, 1500)
conta1.extrato()
conta2 = conta('jose', 800, 20000)
conta2.extrato()

conta2.transferir(500, conta1)
conta1.extrato()
conta2.extrato()