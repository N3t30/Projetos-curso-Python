"""
Módulos externos
Utilizamos o pip _ python installer package

voce pode conhecer todos os pcaotes externos pelo site
https://pypi.org

colorama -> é utilizado para permitir impressão de textos coloridos

# utilizando o pacote instalado

from colorama import init

from colorama import Fore, Back, Style

print(Fore.RED + 'neto peixoto')
print(Back.BLUE + 'neto peixoto')
print(Style.DIM + 'neto peixoto')
print(Style.RESET_ALL)
print('neto peixoto')
"""

import pydf

pdf = pydf.generate_pdf('<h1>Primeira vez<h1>')
with open('text_doc.pdf', 'wb') as f:
     f.write(pdf)

# PROGRAMA COM ERRO

