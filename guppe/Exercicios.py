"""
Exercicio python seção 16

"""

class Pessoa:

    Pessoas = 0

    def __init__(self, nome, idade, altura):
        self.__id = Pessoa.Pessoas + 1
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura
        Pessoa.pessoas = self.__id


    def get_nome(self):
        return self.__nome


    def get_idade(self):
        return self.__idade


    def get_altura(self):
        return self.__altura


    def set_nome(self, nome):
        self.__nome = nome


    def set_idade(self, idade):
        self.__idade = idade


    def set_altura(self, altura):
        self.__altura = altura


    def dados(self):
        print(f'Dados\nNome : {self.__nome}\nIdade : {self.__idade}\nAltura : {self.__altura} ')


class Agenda:

    __contatos = []

    def armazenar(self, pessoa):
        if len(self.__contatos) < 10:
            self.__contatos.append(pessoa)
        else:
            print('Não é possivel adcionar mais ninguem')

    def remove(self, nome):
        if pessoa in self.__contatos:
            if pessoa.get_nome() == pessoa:
                self.__contatos.remove(pessoa)
                print('Pessoa removida')
                return True
            print('pessoa não encontrada')
            return False

    def buscar(self, pessoa):
        if pessoa in self.__contatos:
            if pessoa.get_nome() == nome
                print(f'Pessoa encontrada esta na posição {self.__contatos.index(pessoa)} ')


























