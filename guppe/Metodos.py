"""
poo Metodos
_ Metodos -> Representam os comportamento dos objetos, ou seja, as ações que esse objeto pode
no seu sistema.

Em python dividimos os metodos, em dois grupos: metodos de instancia e metodos de e metodos de classe

# O metodo dunder __init__é um metodo especial chamado de construtor e sua função é construir o objeto
a partir da classe

OBS : todo elemento que se inicia com dois underkkines são chamados de dunder
ONS : Os elementos dunder em python são chamados de magicos

OBS : Metodos são escritos em minusculos e separadas pór underkine

# p1 = Produto('Playstation 4 ', 'video game', 4999)
 # print(p1.desconto(50))

# User1 = Usuario('Neto', 'peixoto', 'josen@gmail.com', '12345')
# User2 = Usuario('jose', 'almeida', 'almeidan@gmail.com', '12345')

# print(User1.nome_completo())
# print(User2.nome_completo())

nome =  input('informe o nome :')
sobrenome = input('Informe o sobrenome :')
email = input('/informe o email :')
senha = input('Informe a senha :')
comfirmar_senha = input('Comfirme a sua senha :')

if senha == comfirmar_senha:
    User = Usuario(nome, sobrenome, email, senha)
else:
    print('Acesso negado, senha não comfere')
    exit(123)

print('usuario criado com sucesso')

senha = input('Informe a senha para acesso')

if User.checar_senha(senha):
    print('Acesso permitido')
else:
    print('Acesso negado')

    # OBS > Metodos de classe em python são conhecido em outras libguagen como Metodos estatiticos

# Metodos de classe

User = Usuario('jose', 'peixoto', 'josen@!gmail.com', '54876')
User1 = Usuario('Neto', 'jose', 'netoll@gamilcom', '6587')

Usuario.contar_usuarios()
User.contar_usuarios()
"""

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrenete:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrenete.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrenete.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """RETORNAR O VALOR DO PRODUTO COM O DESCONTO"""
        return self.__valor * (100 - porcentagem) / 100

from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:

    contador = 0

    @classmethod
    def contar_usuarios(cls):
        print(f'Temos {cls.contador} usuario(s) no Sistema')

    @classmethod
    def ver(cls):
        print('teste')

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuario criado `{self.__gera_usuario}()')


    def nome_completo(self,):
        return f'{self.__nome} {self.__sobrenome}'


    def checar_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):
        return self.__email.split('@')[0]

User = Usuario('jose', 'neto', 'josemhihi@gmail.com', '45785')















