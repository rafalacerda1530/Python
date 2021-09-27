"""
Debugando com pdb

- para debuggar clicamos do lado de fora da coluna perto do numero da linha

- para o python debbuger, importar a biblioteca pdb, e utilizar a função ser_trace()

- comando do pdb:
l: para listar onde estamos no código
n: proxima linha
p: imprime variavel
c: continua a execução - finaliza o debbug

# se a vaariavel ainda n existe, ele da nameerror

# a pertir do python 3.7 não precisa importar o pdb, pois ele se tornou built-in breakpoint()
"""

"""
# EX com Pycharm


def dividir(a,b):
    try:
        return int(a) / int(b)
    except ValueError as err:
        return f'ocorreu um erro: {err}'


print(dividir(4, 'a'))
"""

"""
# EXEMPLO1 PDB

importteste pdb

nome = 'rafael'
sobrenome = 'lacerda'
pdb.set_trace()  # coloca o trace onde vc que iniciar e utiliza os comandos
nome_completo = nome + '' + sobrenome
curso = 'python essencial'
final = nome_completo + 'faz o curso' + curso
print(final)
"""
"""
# EXEMPLO2 PDB
# o importteste do pdb, colocamos na onde vamos debbugar pois depois excluimos ele

nome = 'rafael'
sobrenome = 'lacerda'
importteste pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'python essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)
"""

"""
# EXEMPLO3 PDB
# o importteste do pdb, colocamos na onde vamos debbugar pois depois excluimos ele
# a pertir do python 3.7 não precisa importar o pdb, pois ele se tornou built-in (breakpoint())
nome = 'rafael'
sobrenome = 'lacerda'
breakpoint()  # igual o pdb
nome_completo = nome + ' ' + sobrenome
curso = 'python essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)
"""


# cuidado com os conflitos entre nome de variaveis e os comandos do pdb


def soma(l, n, p, c):  # não conseguimis verificar as variaveis e teriamos conflitos
    return l + n + p + c


print(soma(1, 2, 5, 3))
