"""
List Comprehesion

- podemos gerar listas com dados processados a partir de outros iteraveis

# Sintaxe da list
[para dados for dado in iteravel]
"""


"""
# Exemplo

numeros = [1, 2, 3, 4]

res = [numero * 10 for numero in numeros]

print(res)

# [numero * 10 for numero in numeros] lemos a partir do for ex:
# para cada numero in numeros faça numero * 10

res = [numero / 2 for numero in numeros]
print(res)


# Exemplo com função


def funcao(valor):
    return valor * valor


res = [funcao(numero) for numero in numeros]  # a Fnçao ja esta na variavel
print(res)
"""


"""
# LIst comprehenion versus Loop

# Loop
numeros = [1, 2, 3, 4, 5]
numero_dob = []


for numero in numeros:
    numero_dob.append(numero * 2)
# para cada numero na variavel numeros faça:
# o resultado de numero * 2 ele vai apendar em numerodob


print(numero_dob)


# List comprehesion
print([numero * 2 for numero in numeros])
"""

"""
nome = 'Rafael'

print([letra.upper()for letra in nome])
# para cada letra na variavel nome, print elas em uma lista com letra maiuscula
"""

"""
# Funções em List comprehesion

def caixa_alta(nome):
    nome = nome.replace([0], nome[0].upper())  # o nome vai ser recolocaqdo
    # na posição zero por, a letra de nome na posição zero em maiusculo
    return nome


amigos = ["maria", 'pedrao', 'julia', 'Guilherme']

print([caixa_alta(amigo) for amigo in amigos])
# o amigo vai ser recolocado na posição zero pela letra da posição zero de amigo
# em maiusuclo
"""

"""
# Range em LIst comprehesion

print([numero * 3 for numero in range(1, 6)])
"""


print([str(numero) for numero in [1, 2, 3, 4, 5]])
# para cada numero na lista, jogue ele como string na lista numero

