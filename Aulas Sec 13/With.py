"""
With

serve para executar o processo e fechar em seguida

após a conclusão, automaticamente ele fecha
"""

with open('texto.txt') as arquivo:
    print(arquivo.readlines())
