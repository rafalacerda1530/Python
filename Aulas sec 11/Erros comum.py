"""
Erros mais comuns

SyntaxError - ocorre quando você escreveu algo que não é do python

NameError - ocorre quando uma variavel ou função não foi definido

TypeError - quando é aplicado a um tipo errado

IndexError - quando tentamos acessar um elemento utilizando indice incorreto

ValueError - quando uma função built-in recebe valores inapropriados

KeyError - quando tentamos acessar um dict com uma chave que n existe

AtributeError - quando a var não tem atributo/função

IndententionError - Quando não respeitamos a indentação de 4 espaços
"""

"""
# ex SyntaxError

def error:
    print("Teste")
"""
"""
# SyntaxError palavra reservada não pode ser utilizada
None = 1
"""

"""
# EX NAME ERROR de variavel não definida

print(rafael)
"""

"""
# Como o a não é menor que 10, ele vai igrnorar pois não entra no if e a variavel msg não vai existir
a = 10

if a < 10:
    msg = 'é menor'

print(msg)
"""

"""
# TypeError

print(len(5))

print('Rafael' + 4)
"""

"""
# IndexError
lista = ['Rafael']

print(lista[2])
"""

"""
# ValueError

print(int('RAFAEL'))
"""

"""
# KeyError

dici = {}

print(dici['Rafa'])
"""

"""
# AtributeError
tupla = (1, 2, 3, 4)

print(tupla.sort)
"""