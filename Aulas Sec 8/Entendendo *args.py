"""
Entendendo *args

os args começam com "*"

utilizamos *args para defini-lo

o parametro utilizado em uma função coloca os valores informados em uma tupla

# caso for utilizar todos os parametros,
# segue nessa ordem as declarações
# Parametros obrigatórios
# *args
# parametros default
# **kwargs

"""

"""
def soma(*args):
    total = 0
    for num in args:
        total = total + num
    return total


print(soma(1, 2, 3))


refatorado:

def soma(*args):
    return sum(args)


# ele vai somar os valores numericos, ou seja pq tupla pode ser somada

def soma(a, b, *args):
    return sum(args)
# caso for assim, é necessário colocar os valore no print ex:

print(rafa, carlos, 12, 3, 4, 5)  ele não apresenta erro pois os valores
de a & b que são obrigatorios ja estão setados
"""

"""
def info(*args):
    if 'rafa' in args or 'lacerda' in args:
        return 'Bem vindo'
    return 'Quem é vc ?'


a = 'rafa'
b = 'lacerda'
print(info(a))
"""


# desempacotamento de listas
def soma(*args):
    return sum(args)


num = [1, 3, 3, 4, 5]
print(soma(*num))   # o "*" vai desempacotar a lista, pois se deixarmos a lista
# ele da erro pois vai adicionar a lista assim ([lista...])
