"""
SORTED

-Serve para ordenar elementos
- O Sorted não altera o ITERAVEL, APENAS ORDENA E DEPOIS VOLTA AO NORMAL
"""

"""
numeros = (0, 1, 5, 3, 4)

print(sorted(numeros))
"""

"""
# adicionando parametros do maior para menor

numeros = (0, 1, 5, 2, 3, 4)

print(sorted(numeros, reverse=True))  # ordena do maior para o menor
"""

"""
# exemplo mais complexo

usuarios = [
    {"username": "Samuel", "Tweets": ["Eu adoro Bolos", "Eu adoro Pizzas"]},
    {"username": "Carla", "Tweets": ["Eu amo meu gato"]},
    {"username": "Jeff", "Tweets": []},
    {"username": "Bob123", "Tweets": []},
    {"username": "Doggo", "Tweets": ["Eu adoro cachorros", "Vou sair hoje"]},
    {"username": "Gal", "Tweets": []}
]

print(sorted(usuarios, key=lambda usuario: usuario["username"], reverse=True))

# ordenando pelo Usuário
print(sorted(usuarios, key=lambda usuario: len(usuario["Tweets"])))  # usuario como chave para o len tweets como valor
"""

musicas = [
    {"TItulo": "Forro Boys", "Tocou": 17},
    {"TItulo": "Djonga", "Tocou": 9000},
    {"TItulo": "iron", "Tocou": 950},
    {"TItulo": "XAND", "Tocou": 850}
]

print(sorted(musicas, key=lambda musica: musica['Tocou'], reverse=True))  # ELE VAI ORDENAR PELA CHAVE "Tocou"
