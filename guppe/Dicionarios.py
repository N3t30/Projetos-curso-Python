'''
Sicionarios
Em algumas linguagens de programação, os dicionarios python são conhecidas por mapas

Dicionarios são coleções de tipo chave/valor

Dicionarios são reprsentados por chaves {}

sobre dicionarios
- chave e valor são separados por : 'chave:valor'
- tanto chave quanto valor podem ser de qualquer tipo de dados
- podemos misturar qualquer tipos de dados

# criação de dicionarios

# forma 1 (mais comun)
paises = {'br': 'Brasil', 'eua': 'Estados unidos', 'py': 'paraguai'}

print(paises)
print(type(paises))

# forma 2 (menos comun))

paises = dict(br='Brasil', eua='Estados unidos', py='paraguai')
print(paises)
print(type(paises))

# acesssando elementos

# forma 1 : acessando via chave. da mesma forma que lists/tupla
print(paises['br'])
print(paises['py'])

# caso tentarmos fazer um acesso utilizando uma chave que não existe teremos o error keyError

# forma 2 : acessando via get - Recomnendado

print(paises.get('br'))

# podemos definir um valor quando nãoi encontramos o objeto com a chave infromada
pais = paises.get('ry', 'Não encontrado')
print(f'Encontrei o pais {pais}')

paises = {'br': 'Brasil', 'eua': 'Estados unidos', 'py': 'paraguai'}

# podemos verificar se uma derteminada chave se enontra em um dicionario

print('br' in paises)
print('ru'in paises)
print('Estados unidos' in paises)

# podemos utilizar qualquer tipo de dado (int, float, string, boolean, inclusive  listas, tuplas e dicionarios,
# como chaves de dicionarios
# tupls por exemplo são bastente interessantes de serem usadas para chave de dicionarios pois são imutaveis
localidades = {
    (585.5465, 25.2569): 'Escritorio em city',
    (585.5465, 65.3658): 'Escritorio em são paulo',
    (585.5465, 98.56452): 'Escritorio em maceió',
}
print(localidades)

# adicionar elementos em um dicionarios

receita = {'jan': 100, 'fev': 150, 'mar': 350 }
print(receita)
# forma 1 - mais comum
receita['abr'] = 450
print(receita)

# forma 2

novo_dado = {'mai': 580}
receita.update(novo_dado) # receita.update({'mai': 500})
print(receita)

# atuailazando dados em um dicionario
# forma 1
receita['mai'] = 550
print(receita)

receita.update({'mai': 900})
print(receita)

# conclusão 1 - A froma de atualizar e adcionar elementos são as mesmas.
# conclusão 2 - Em dicionarios, não podemos ter chaves repetidas.

# Remover dados de um dicionario

receita = {'jan': 100, 'fev': 150, 'mar': 350 }
print(receita)

# forma 1 - mais comum

ret = receita.pop('mar')  # precisamos sempre informa a chave
print(ret)                # Ao removermos um objeto, o valor desse objeto sempre e retornado.

print(receita)


# forma 2

del receita['fev']  # del: deletar
print(receita)

# se a chave não existir será gerado um keyError
# Neste caso o valor removido não e retornado


# imagine quw voce tem um comercio eletronico, onde temos varios produtos

# feito com tuplas e listas

carrinho = []

produto1 = ['playstation 4', 1, 2300.00]
carrinho.append(produto1)
print(carrinho)

carrinho = ()
produto2 = ('God of war', 1, 250.00)
carrinho = produto2

print(carrinho)

carrinho = []

produto1 = {'nome': 'playstation  4', 'quantidade': 1, 'preço': 2300.00}
produto2 = {'nome': 'God of war  4', 'quantidade': 1, 'preço': 230.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Desta forma, facilmente adicionamos ou removemos produtos do carrinho e em cada produto
# podemos ter a certeza sobre cada informação

# limpar dicionario
d.clear()
print(d)

# Metodos de dicionarios

d = dict(a=8, d=8, o=9)
print(d)
print(type(d))

# copisndo dicionarios para outro
# forma 1
novo = d.copy() # deep copy

print(novo)
novo['f'] = 5
print(d)
print(novo)

# forma 2 shallow copy
novo = d
novo['f'] = 8

print(d)
print(novo)

'''

# fotma não usual de criação de dicionarios

outro = {}.fromkeys('a', 'u')
print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'email', 'telefone', 'cidade'],'Desconhecido')
print(usuario)
print(type(usuario))

# o metodo fromkeys recebe dois dados: um iteravel e um valor
# ele vai gerar para cada valor do iteravel uma chave e irá atribuir a esta chave o valor informado

veja = {}.fromkeys('tsete', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)

