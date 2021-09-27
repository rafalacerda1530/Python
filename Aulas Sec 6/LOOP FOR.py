"""
Loop e For= estrutura de repetição

Valor Iterável = pode alterar qualquer caracter
Ex nome = rafa print(nome[0]) = ele vai trazer a letra na posição 0
Ou seja pode percorrer cada caracter

"""

"""
nome = 'Rafa'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

# Exemploes de FOR
for letra in nome:  # Para letra dentro deste iteral
    print(letra)    # Print as letras

print(f'\n')

# For iterando sobre uma lista
for numeros in lista:
    print(numeros)

print(f'\n')
{"TItulo": "Forro Boys", "Tocou": 17},
# FOR iterando sobre um Range
for numeros in range(1, 11):
    print(numeros)

print(f'\n')

for valor in enumerate(nome):  # o Enumrate gera uma tupla
    print(valor)  # ou seja cada letram na sua posição

qtd = int(input('quantas vezes deve rodar este loop?'))

for n in range(1, qtd+1):  # informar +1 pois o range para um valor antes
    print(f'imprimindo {n}')

print(f'\n')

qtd2 = int(input('quantas vezes deve-se somar??'))
soma = 0

for n in range(1, qtd2+1):  # informar +1 pois o range para um valor antes
    num = int(input(f'informa o {n}/{qtd2} valor:'))
    soma = soma + num
print(f'a soma é {soma}')

print(f'\n')

name = 'RAFAEL'
for letra in name:
    print(letra, end='')  # para não pular uma linha

print(f'\n')

# EMOJIS:
# ORIGINAL U+1F60D
# MODIFICADO U0001F60D

for _ in range(3):  # vai executar 3 vezes
    for num in range(1, 11):
        print(f'\U0001F60D' * num)  # em vez de mostrar os numeros ele vai mostrar o emoji
# e fazer o range ou seja 1 x 1, 1 x 2, 1 x 3 e o resul é a qntd de emoji
# ele vai fazer ex:
# 1 x 1, 1 x 2, 1 x 3 e assim por diante até 0 10, ou seja:
# para numer no range de 1 a 10 faça o Emoji vezes o numero.
# se fosse assim: print(f'\U0001F60D' * num)
"""

musicas = [
    {"TItulo": "Forro Boys", "Tocou": 17},
    {"TItulo": "manu gavassi", "Tocou": 5},
    {"TItulo": "Djonga", "Tocou": 9000},
    {"TItulo": "iron", "Tocou": 950},
    {"TItulo": "XAND", "Tocou": 850}
]

maxi = 150
for musica in musicas:
    if musica['Tocou'] < maxi:
        maxi = musica['Tocou']
#  acima ele esta verificando o menor valor comparado a maxi e adicionando o valor da chave tocou em maxi

for musica in musicas:
    if musica['Tocou'] == maxi:
        print(musica['TItulo'])
#  aqui ele pega esse menor valor e printa o titulo