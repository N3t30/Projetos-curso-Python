'''
modulo colllections - counter ( contador )

collections conhecido por  -> high-perfomance container datetypes

COunter -> Recebe um iteravel com parametro e cria um objeto do tipo colllections counter que é parecido
com um dicionario, contendo como chave o elemento da lista passando como parametro e como valor e quantidade
de ocorrencia desse elemento

# Realizando o import
from collections import Counter

# exemplo 1
# podemos utilizar qualuqer iteravel, aqi usamos lista
lista = [2, 3, 6, 5, 5, 2, 2, 4, 4, 8, 8, 9, 6, 6, 5, 6, 3, 5, 8, 5, 6, 6]

# utilizando o Counter
res = Counter(lista)

print(type(res))
print(res)

# Counter({6: 6, 5: 5, 2: 3, 8: 3, 3: 2, 4: 2, 9: 1})

# veja que para cada elemento da lista o Countr criou uma chave e colocou como valor a quantidade de ocorrencias
# ( Ocorrencias ) é a quantidade de vezes que a chave se repete

# Exemplo 2
print(Counter('Neto peixoto'))
# Counter({'o': 3, 'e': 2, 't': 2, 'N': 1, ' ': 1, 'p': 1, 'i': 1, 'x': 1})

'''

# Realizando o import
from collections import Counter

# Exemplo 3

texto = """Rebel Heart é o décimo terceiro álbum de estúdio da artista musical americana Madonna. O seu lançamento
 ocorreu em 6 de março de 2015, através da editora discográfica Interscope. A artista iniciou o desenvolvimento
do disco em fevereiro de 2014, após lançar o curta-metragem secretprojectrevolution, que deu início a uma campanha
global chamada Art of Freedom. Ela divulgou fotos de diversas sessões de gravação em seu Instagram, nas quais
trabalhou com disc jockeys (DJ) como Diplo e Avicii, e produtores como Ryan Tedder e Toby Gad. Trabalhar com
diversas pessoas no projeto mostrou-se um problema para que Madonna mantivesse um som e direção coesos,
uma vez que seus álbuns anteriores haviam sido desenvolvidos com um pequeno grupo de pessoas. Tematicamente,
o material representa os dois lados diferentes da cantora: ouvir o coração de alguém e ser um rebelde, temas que
cresceram organicamente durante as sessões de gravação e composição.
Musicalmente, Rebel Heart é um álbum derivado do pop e incorpora uma variedade de gêneros, como house music, trap,
reggae e dubstep, ao passo em que apresenta um coral gospel e instrumentos como órgão e guitarra acústica. Liricamente
suas faixas falam sobre amor, reflexões pessoais, e a introspecção da carreira de Madonna; algumas delas também são
naturalmente autobiográficas. (leia mais...)"""

palavra = texto.split()











