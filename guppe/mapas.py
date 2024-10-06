'''
Mapas -> conhecidos em python como dicionarios

Dicionarios em python são representados por {}

# Como intarar sobre dicionarios

for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f' Em {chave} : Recebi {receita[chave]}')

# Acessando as chaves
print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

# Acessando valores
print(receita.values())

for valor in receita.values():
    print(valor)

# desenpacotamento de dicionarios

for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')

'''

receita = {'jan': 100, 'fev': 500, 'mar': 800}
print(receita)

# soma*, valor max*, valor min*, tamanho*
# * Se os valores forem todos iinteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))

