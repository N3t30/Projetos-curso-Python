'''
sistema de manipulação

# Descobrindo se um arquivo ou diretorio existe

# Arquivo
print(os.path.exists('Arquivo.lele')) # Retorna True ou false

# Diretorio
print(os.path.exists('geek'))

import os

# Criando arquivos

# forma 1
open('novo.text', 'w').close()

# forma 2
open('novo2.text', 'a').close()

# forma 3
with open('novo3.text', 'w') as arquivo:
    pass
'''
import os

os.mknod('novo4')