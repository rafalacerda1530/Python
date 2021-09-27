"""
Tuplas

Se parecem com listas, diferenças:
-Tuplas são representadas por "()"
- Tuplas são imutáveis, toda operação gera uma nova Tuplaa
- TUplas podem ser representadas da seguinte forma tambem:
tupla1 = 1,  2, 3 isso também é uma tupla
a "," define o que é uma tupla
- tupla = (5) não é uma Tupla, tupla = (5,) isso é uma tupla
precisa da ","
_ Adição e remoção não existe nas Tuplas, elas são imutaveis

"""

"""
# Tuplas com range
tupla = tuple(range(0, 10))
print(tupla)  # ele gera uma tupla do 0 a 10
"""

"""
# Desempacotamento de tupla
tupla = ('rafael', 'lacerda')

nome, sobrenome = tupla

print(nome)
print(sobrenome)
# ele atribui o indice 1 na primeira variavel(nome)
# e o segundo indice para a segunda variavel(sobrenome)
# OBS: Tem que ter a mesma quantidade de indice e várivel
"""

"""
# Soma, Valor maximo, Valor minimo, tamanho
tupla = 1, 2, 3, 4, 5, 6

print(sum(tupla))  # Soma
print(max(tupla))  # Maximo valor
print((min(tupla)))  # Minimo valor
print(len(tupla))  # Tamanho da lista
# somente para valores int e Float
"""

"""
# concatenar Tuplas
tupla1 = 1, 2, 3
tupla2 = 4, 5, 6

print(tupla1 + tupla2)  # ela concatena mas n altera a Tupla

print(tupla1)
print(tupla2)

tupla1 = tupla1 + tupla2
print(tupla1)
# unica forma de alterar(sobreescrever)
"""

"""
# verficar se tem um elemento na tupla
tupla1 = 1, 2, 3
print(3 in tupla1)  # tem o 3 na tupla1?
"""

"""
# Iterando nas Tuplas
tupla1 = 1, 2, 3

for n in tupla1:
    print(n)  # para cada numero(n) in tupla print este numero

for indice, valor in enumerate(tupla1):
    print((indice, valor))
# enumerate mostra o indice e o valor que tem nele
"""

"""
# Contando elementos dentro de um Tupla
tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tupla.count('a'))  # Quantos "a" eu tenho na var tupla

tupla2 = tuple('rafael rodrigues')  # transforma a tupla em str
print(tupla2)
print(tupla2.count('a'))  # conta quantos "a" tem
"""

"""
# Tuplas são usadas quando não precisamos alterar os dados
# de uma coleção ex:

meses = ('jan', 'fev', 'mar', 'abr', 'mai', 'jun')
# não faz sentido modificar a lista quando ela esta completa
"""

"""
# acesso de elementos
meses = ('jan', 'fev', 'mar', 'abr', 'mai', 'jun')
print(meses[0])  # meses no indice 0
"""

"""
# iterando com indices
meses = ('jan', 'fev', 'mar', 'abr', 'mai', 'jun')
i = 0

while i < len(meses):
    print(i)
    i = i + 1
"""

"""
# verificando o indice de um elemento
meses = ('jan', 'fev', 'mar', 'abr', 'mai', 'jun')
print(meses.index('abr', 1))
# em qual indice esta o elemento abr a partitr do indice 1
"""


# copiando uma Tupla para outra
tupla = 1, 2, 3
print(tupla)

nova = tupla

print(nova)

outra = 4, 5, 6

nova = nova + outra
print(nova)

