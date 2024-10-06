'''
poo
Atributos - representam as caracteristicas do objeto, ou seja, pelo objeto conseguimos representar
computacionalmente os estados de atributos

Em python dividimos os grupos em 3 grupos
        - Atributos de instãncia
        - Atributos de classw
        - Atributos dinamicos

# OBS : lembre-se que isso é so uma convenção, ou seja, a linguagem python não vai impedir que façamos aceeso
# aos atributos sinalizados como privado fora da classe

# Exemplo

User = Acesso('usergmail@.com', '123456')

print(User.email)

# print(user.__senha) # Gerar error

print(User._Acesso__senha) # temos acesso, mas não deveriamos  # Name manglin

User.mostra_email()

User.mostra_senha()

# O que significa atributos de instancia?
# Quando criamos instancias de uma classe, todas as instancias teram esses atributos

User1 = Acesso('user@gmail.com', '12366')
User2 = Acesso('user2@gmail.com', '123456')

User1.mostra_email()
User2.mostra_email()

p1 = Produto('plays', 'video game', 4700)
p2 = Produto('xbox S', 'video game', 2700)

# classe

print(p1.valor)  # Acesso possivel mas incorreto
print(p2.valor)  # Acesso possivel mas incorreto

print(Produto.imposto) # Acesso correto de um atributo de class
print(p1,id)
print(p2.id)

'''

class lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False

class ContaCorrente:

    def __init__(self, numeros, saldo, limite):
        self.numeros = numeros
        self.saldo = saldo
        self.limite = limite

class Produto:

    def __init__(self, nome, descricao, valor):
        self.valor = valor
        self.nome = nome
        self.descricao = descricao

class Usuario:

    def __init__(self, nome, email, Senha):
        self.nome = nome
        self.email = email
        self.Senha = Senha



# Atributos privados e publicos

# Em python ficou estabelecido que todo atributo de um classe
# pode ser acessado em todo o projeto
# Caso queiramos que o atributo seja privado, utiliza-se __ duplpo underline no inicio do nome
# Exemplo : self.__nome = npme

class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_email(self0):
        print(self0.email)

    def mostra_senha(self):
        print(self.__senha)

# Atributos de classe

# ATRIBUTOS DE CLASSE, são atributos que são declarados diretamente na classe ou seja fora do construtor gerando e
# compartilhando seu valor para os outros instancias da classe

class Produto:

    # Atributode class
    imposto = 1.05
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


# Atributo dinamicos

  #  - Um atributo de instancia que pode ser cirado em execução
# OBS : O atributo dinamico sera exclusivo da instancia que o criou

p1 = Produto('playstation', 'video game', 9500)

p2 = Produto('Xbox', 'video game', 5000)

# criando um atributo dinamico em tempo de execução
p2.peso = '5kg'  # 1não temos o atributo peso na classe produto
print(f'Produto : {p2.nome}, Descrição : {p2.descricao}, valor : {p2.valor}, peso{p2.peso} ')
 # print(f'Produto : {p1.nome}, Descrição : {p1.descricao}, valor : {p1.valor}, peso{p1.peso} ') # O peso não foi
# atribuido no p1

# deletando atributos

print(p1.__dict__)
print(p2.__dict__)

del p2.peso

print(p1.__dict__)
print(p2.__dict__)





