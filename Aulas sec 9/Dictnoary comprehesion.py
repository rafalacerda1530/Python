"""
Dictionary Comprehesion

Sintaxe = {chve : valor for valor in iteravel}
"""

"""
# Exemplos

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}  
# .item devolve cada chave e valor dentro de uma tupla
print(quadrado)
"""

"""
numeros = {1, 2, 3, 4, 5}

quadrado = {valor: valor ** 2 for valor in numeros}
# para cada valor in numero: coloque valor como chave e o valor ** 2 como valor

print(quadrado)
"""

"""
chave = 'abcde'

valores = [1, 2, 3, 4, 5]

mistura = {chave[i]: valores[i] for i in range(0, len(chave))}
#  para i no range de 0 até o len de chave, mostre chave na posição i e valor
#  na posição i

print(mistura)
"""

# exemplo com logica condicional
numeros = [1, 2, 3, 4, 5]

res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}
# para cada numero na variavel numero faça: adicione o num em num e
# verifique se le é impar ou par, ou seja, quando o num passar por 1
# ele vai adicionar esse valor na variavel num e chechar se é impar ou par
