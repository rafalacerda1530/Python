"""
POSSUI TRUE OR FALSE

True e FAlse - sempre com a inicial maiusculo

utilizado para operações basicas
"""

ativo = True

print(ativo)

###########

#  Negação - se o valor booleano for True o resultado é False
#  se for False o resultado é True

print(not ativo)  # ele era True e virou Falseou seja sempre o contrário

#####################

# Operação OR / operação binária depende de dois valores
# um ou outro deve ser verdadeiro

# True or True  DOIS VERDADEIROS É VERDADEIRO3
# True or False  Um verdadeiro e um falso = verdadeiro
# possuindo qualquer verdadeiro, o resultado é verdadeiro
# se possuir os dois falsos ele é falso

logado = False

print(ativo or logado)  # result é TRUE poq a Var ativo é true
# ou seja possuindo qualquer verdadeiro, o resultado é verdadeiro

###################################3

# AND - Uma operação Binária / ambos os valores devem ser iguais
# ou seja, para ser true deve ser true and true
# fora isso o resultado sera false

