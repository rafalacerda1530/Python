"""
Reversed

OBS: Não confunda com reverse # inverte a ordem da lista, o reverse só funciona em listas

-Reversed. funciona com qualquer Iterável

- o tipo do res é <class 'list_reverseiterator'>
"""

"""
lista = [1, 2, 3, 4, 5]
res = reversed(lista)
print(res)
print(type(res))

# convertendo o reversed

# lista
print(list(reversed(lista)))

#tupla
print(tuple(reversed(lista)))

# set
print(set(reversed(lista)))  # o set não define ordem então não funciona
"""

# iterando com reversed
for letra in reversed("rafael"):
    print(letra, end='')

print('\n')

# sem o uso do for
print(''.join(list(reversed('rafael'))))

print('\n')

print('rafael' [:: -1]) # vai do começo até o final ao contrário

for n in reversed(range(0, 10)):
    print(n, end='')

print('\n')

for n in range(9, -1, -1):
    print(n, end='')
# para n in range começando do 9 até o -1(ele para no 0) -1 = comece ao contrario ou seja do nove
