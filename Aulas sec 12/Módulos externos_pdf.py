"""
Módulos externos

https://pypi.org - para onhecer todos os pacotes_teste do Pyhton
"""

"""
from colorama importteste init, Fore  # serve para colorir textos

init()

print(Fore.YELLOW + "RAFAEL")
"""

import pydf

pdf = pydf.generate_pdf('<h1>RAFAEL</h1><br/><br/><strong>Programa&ccedil;&atilde;o em python</strong>')
#  <h1> GERA UM TITULO </h1> fecha a chave
# <br/> pula uma linha
# &ccedil = Ç
# &atilde = Ã
# <strong> LETRAS EM NEGRITO </strong>

with open('teste_doc.pdf', 'wb') as f:
    f.write(pdf)
