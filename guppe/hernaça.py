"""
POO -  herança

A ideia de hernaça é a de reaprobeitar codigo, tambem extender nossas classes

Com a herança, a partir de uma classe existente, mós extendemos outra classe que passa a herdar
atributos e metodos de classe herdada

OBS: quando uma classe herda de outra classe ela herda TODOS os atributos
quando uma classe herda de outra classe, a classe herdada é conhecida como
classe (Pessoa)
super classe, classe mãe, classse genericos, classe pai pu classe base

Quando uma classe herda de outra classe ela é chamada
sub classe, classe filha, classe especifica




"""
class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Cliente(Pessoa):
    """cliente herda de pessoa"""
    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)          # modo de fazer acesso a super classe
        self.__renda  = renda


class Funcionario(Pessoa):
    """funcionario  herda de pessoa"""

    def __init__(self, nome, sobrenome, cpf,  matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula


cliente1 = Cliente('jose', 'peixoto', '458.542.658-58', 8525)
funcionario1 = Funcionario('pedro', 'raul', '874.658.985-58', 58745)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

print(cliente1.__dict__)
print(Funcionario.__dict__)












