'''
Definindo fubçOes
- Funçôes são pequenas partes de codigos que realizam tarefas especificas
- pode ou não recevber entradas de dados e retornar uma saida de dados
- muito uteis para executar procedimentos similares por repetidas vezes

OBS: se voce escrever uma função que realiza varis tarefas dentro delas é bom fazer uma verificação para que
a função seja simplificada

já utilizamos varias funções desde que começamos esse curso
- print()
- len()
- max()
- count()
- e outras mais
'''
# Exemplo de funções

#cores = ['amarelo', 'roxo', 'azul', 'vermelho']
# print(cores)
#cores.append('marrom')
# print(cores)
#cores.clear()
# print(cores)

# DRY -  Don't repeat yourself - Não repita voce mesmo / naõ repita seu codigo.
# mas como definir uma função?
'''
Em python, a forma geral de definir uma função é ;
def nome_da_função(parametros_de_entrada):
    bloco_de_função
    
onde:

nome_da_função -> SEMPRE, com letrs minúsculas, e se for nome composto, separados por underline (snake case)
parametros são opcionais => opcionais, onde tendo mais de um, cada um seprados por virgula, podendo ser opcionais ou não
bloco_da_função -> tambem chamados de corpo da função ou implementação, é onde o processamento da função acontece,
neste blovo, pode ter ou não retorno da função.

OBS : veja que para definir uma função, utilizamos a palavra reservada 'def' imformnando ao python que estamos
definindo um afunção, tambem abrimos o bloco de codigo com o ja conhecido dois pontos (:) que é utilizado em python 
para definir blocos
'''
# definindo a primeira função
# definição
def diz_oi():
    print('Oi!')

'''
OBS
1 - veja que, dentro das nossas funões podemos utilizar outrs funções
2 - veja que nossa função só executa 1 tarefa, ou seja, a outra coisa que ela faz é dizer oi
3 - veja que esta função não recebe nenhum parametro de entrada 
4 - veja que esta funçao não retorna nada 
'''
# utilizando funções

# diz_oi()
'''
Atenção não esqueca de utilizar os () ao executar uma função

errado
diz_oi

certo
diz_oi()
'''
# Exemplo 2
def cantar_parabens():
    print('parabens para voce')
    print('nesta data querida')
    print('muitas felicidades')
    print('muitos anos de vida')

# for n in range(3):
    # cantar_parabens()

# Em python podemos inclusive criar variaveis do tipo de uma funnção e executar esta função através de uma variavel
# Não muito usado

canta = cantar_parabens

canta()




















