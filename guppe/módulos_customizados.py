'''
Módulos customizados

Como módulos python nada mais são do que arquivos, então TODOS os arquivos que criamos nesse curso
são Módulos python prontos para serem utilizados

# importando um modulo especifico de nossos modulos

from funções_com_parametro import impares

print(impares([1, 2, 3, 4, 5, 6, 8, 58, 65, 91, 81, 81]))

# Importando todos o módulo, temos todo acesso ao módulo
import funções_com_parametro as fcp

# Estamos acessando e imprimindo uma variavel de um módulo
print(fcp.tupla)
print(fcp.impares(fcp.tupla))
'''

from map import cidades, c_para_f

print(list(map(c_para_f, cidades)))

