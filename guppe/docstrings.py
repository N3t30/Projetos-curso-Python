'''
Documnetando funções com docstring
OBS podemos ter acesso a documnetação de uma função em python
utilizando a propriedade especial __doc__

ppodemoss ainda fazer aceesso a documentação com a função help
'''

def Diz_oi():
    """ums fubção simples que retorna oi"""
    return 'oi'

def exponencial(numero, potencias=2):
    """
    função que retorna por padrão o quadrado do 'numero' ou 'numero' a potencia informada
    :param numero: Numero que desejamos gerar a exponencial,
    :param potencias: potencia que queremos gerar o exponencial por padrão é 2
    :return: Retorma o exponencial do numero por potencia
    """
    return numero ** potencias