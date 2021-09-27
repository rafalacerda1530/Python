"""
Set Comprehesion

- Set só possui valor entre as chaves

set = {1, 2, 3, 4, 5}
"""

numeros = {valor: valor ** 2 for valor in range(10)}
print(numeros)

letras = {letra for letra in "RAFAEL"}
print(letras)

# Conjuntos não tem repetições e não possuem ordem
