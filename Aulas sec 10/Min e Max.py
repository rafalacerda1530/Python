"""
Min e Max
max() -> retonar o maior valor em um iteravel, ou o maior de dois elementos

- posso passar quantos valores eu quiser

- qualquer dado

Min() - > retorna o menor valor em um iteravel ou entre dois ou mais elementos

help para verificar o que a função faz

dir mostra oq vc pode utilizar com o iteravel
"""

# MAX
"""
lista = [1, 8, 4, 99, 34, 129]
print(max(lista))
#  printa o maior numero

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionario.values()))
"""

"""
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

print(max(valor1, valor2))
"""

# MIN

"""
lista = [1, 8, 4, 99, 34, 129]
print(min(lista))
#  printa o maior numero

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(min(dicionario.values()))

valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

print(min(valor1, valor2)),
"""

"""
nomes = ['Rafael', 'Dora', 'João', 'Bob', 'Carlos Augusto']

print(max(nomes))  # ele vai puxar pela primeira letra, a que for maior no alfabeto ele printa, no caso Rafael
print(min(nomes))  # ele vai puxar pela primeira letra, a que for menor no alfabeto ele printa, no caso Bob

print(max(nomes, key=lambda nome: len(nome)))  # ordena pelo tamanho adicionando em nome

print(min(nomes, key=lambda nome: len(nome)))
"""

musicas = [
    {"TItulo": "Forro Boys", "Tocou": 17},
    {"TItulo": "manu gavassi", "Tocou": 5},
    {"TItulo": "Djonga", "Tocou": 9000},
    {"TItulo": "iron", "Tocou": 950},
    {"TItulo": "XAND", "Tocou": 850}
]

"""
print(max(musicas, key=lambda musica: musica['Tocou']))
print(min(musicas, key=lambda musica: musica['Tocou']))

# imprima somente o titulo da musica mais e menos tocada

print(max(musicas, key=lambda musica: musica['Tocou'])['TItulo'])  # desse objeto informe somente a chave titulo
print(min(musicas, key=lambda musica: musica['Tocou'])['TItulo'])  # printe em musicas e armazene na variavel
# musica as que possuem o menor valor e apresente somente o titulo
# OBS: o KEY é a forma que ele vai buscar esses resultados

# APRESENTE A MAIS TOCADA SEM MAX, MIN E LAMBDA
"""

maxi = 150
for musica in musicas:
    if musica['Tocou'] < maxi:
        maxi = musica['Tocou']
#  acima ele esta verificando o menor valor comparado a maxi e adicionando o valor da chave tocou em maxi

for musica in musicas:
    if musica['Tocou'] == maxi:
        print(musica['TItulo'])
#  aqui ele pega esse menor valor e printa o titulo
