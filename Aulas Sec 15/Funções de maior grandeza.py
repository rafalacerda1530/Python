"""
Higher Order Function

- Funções que retornam funções ou funções como argumentos para outras funções
"""

"""
# definindo as funções


def somar(a, b):
    return a + b


def dim(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def calcular(num1, num2, func):  # no campo func ele vai executar a função colocada
    return func(num1, num2)


# testando

print(calcular(4, 3, somar))  # aqui ele vai utilizar a função somar

print(calcular(4, 3, dim))

print(calcular(4, 3, mul))

print(calcular(4, 3, div))
"""

"""
# Nested Functions - Inner functions - funções dentro de funções


from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(('Eai ', 'Suma daqui ', 'Gosto muito de você '))
    return humor() + pessoa


print(cumprimento('Rafael'))

print(cumprimento('Karen'))

print(cumprimento('Dilma'))
"""

"""
# Retornando funções de outras funções

from random import choice


def faz_me_rir():
    def rir():
        return choice(('hahahahahaha ', 'kkkkkkkkkkkkkkkkkkkkk', 'hehehehehehe'))
    return rir


rindo = faz_me_rir()

print(rindo())
"""

# Inner functions - podem acessar funções externas


from random import choice


def faz_me_rir(pessoa):
    def dando_risada():
        risada = choice(('hahahaha', 'kkkkkkkkk', 'hehehehehe'))
        return f'{risada} {pessoa}'
    return dando_risada()


rindo = faz_me_rir

print(rindo('Rafael'))
print(rindo('Rafael'))
print(rindo('Rafael'))