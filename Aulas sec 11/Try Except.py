"""
Try EXcept

serve para tratar erros
"""

"""
try:
    len(5)
except TypeError as Err:  # o as é um alias que é apresentado
    print(f'A aplicação gero o erro {Err}')


# podemos colocar duas excessões ou mais
try:
    len(5)
except TypeError as Err:  # o as é um alias que é apresentado
    print(f'A aplicação gero o erro {Err}')
except NameError as errb:
    print(f'A aplicação gero o erro {errb}')
"""


def pegavalor(dici, chave):
    try:
        return dici[chave]
    except KeyError:
        return 'Chave não existe'


dic = {'game': 'Rafael'}

print(pegavalor(dic, 'nome'))  # estou colocando a chave nome, ele retorna o valor

