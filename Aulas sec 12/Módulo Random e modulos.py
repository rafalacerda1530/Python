"""
Módulo Random e Módulos

Random, funções para gerar numeros pseudoaleatórios
"""

"""
# forma 1 não recomendado

importteste random

# random() > gera um numero pseudo aleatório entre 0 e 1

# ao importar todo o módulo, ele arquiva em memória todas as propriedades

print(random.random())
# para utilizaro random, colocamos o nome do pacote e o nome da função separados por ponto
"""

"""
# forma 2, importando uma função específica
from random importteste random

for i in range(0, 11):
    print(random())
"""

"""
from random importteste uniform

# uniform gera um numero pseudo-aleatorio entre valores estabelecidos reais (com virgula)

for i in range(0, 11):
    print(uniform(3, 10))  # ele vai somente até o 9
"""

""""
from random importteste randint

# gera valores pseud-aleatorios inteiros, entre valores estabelecidos

for i in range(6):
    print(randint(1, 61), end=' , ')  # começando de 1 e indo até 60
"""

"""
# choice mostra um valor aleatorio entre um iterável

from random importteste choice

jogadas = ['pedra', 'papel', 'tesoura']

print(f'o jogador 1 escolheu {choice(jogadas)}')
print(f'o jogador 2 escolheu {choice(jogadas)}')

print(choice('RAFAEL'))  # ELE ESCOLHE UMA LETRA
"""

# shuffle tem a função dem embaralhar dados

from random import shuffle

cartas = ['k', 'q', 'j', 'a', '2', '3', '4', '5']

print(cartas)
shuffle(cartas)

print(cartas[0], cartas[4], cartas[5])