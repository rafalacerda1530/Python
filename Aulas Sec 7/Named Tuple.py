"""
Named Tuple - Tupla Nomeada

- São Tuplas diferentes, Onde especificamos um nome e parametros
"""
# importando

from collections import namedtuple

# precisamos definimir o nome e parametros

# Forma 1: declaração named tuple

cachorro = namedtuple('cachorro', 'idade raca nome')

# forma 2 declaração named tuple

cachorro1 = namedtuple('cachorro', 'idade, raca, nome')

# forma 3 declaração named tuple

cachorro2 = namedtuple('cachorro', ['idade', 'raca', 'nome'])

ray = cachorro(idade='2 anos', raca='chowchow', nome='Ray')

print(ray)

# acessando os dados
print(ray[0])  # idade
print(ray[1])  # raca
print(ray[2])  # nome

# Forma 2

print(ray.idade)
print(ray.raca)
print(ray.nome)

# forma 3

print(ray.index('chowchow'))  # Index mostra o indice do valor
print(ray.count('chowchow'))  # mostra quantas ocorrencias desse valor
