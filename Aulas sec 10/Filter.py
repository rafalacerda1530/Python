"""
Filter

- Serve para filtrar dados de uma coleção
- Filter recebe uma função e um iterável
- os valores no filter são utilizaqdos apenas uma vez,
se ṕrintar ele duas vezes ele some


"""
import statistics

"""
#dados coletados de um sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# calculando a media com a função mean() que é importada da biblioteca statistics
media = statistics.mean(dados)  # ele vai somar todos os valores e dividir pela
# quantidade de posições

print(media)

res = filter(lambda x: x > media, dados)  # ele vai utilizar a função lambda
# no iteravel dados, ou seja, dados como parametro para executar a função lambda
# o X é os valores em dados, ou seja o 1.3, 2.7 ... etc

print(list(res))
"""

"""
# removendo valores vazios
paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

filtro = filter(None, paises)  # ele vai remover os tipos Nones(vazios) da lista paises

print(paises)
print(list(filtro))
"""

"""

# Exemplo mais complexo
usuarios = [
    {"username": "Samuel", "Tweets": ["Eu adoro Bolos", "Eu adoro Pizzas"]},
    {"username": "Carla", "Tweets": ["Eu amo meu gato"]},
    {"username": "Jeff", "Tweets": []},
    {"username": "Bob123", "Tweets": []},
    {"username": "Doggo", "Tweets": ["Eu adoro cachorros", "Vou sair hoje"]},
    {"username": "Gal", "Tweets": []}
]

# FIltrar os usuários que estão inátivos no TWitter


# Forma1
filtro = list(filter(lambda user: len(user["Tweets"]) == 0, usuarios))
# crie uma lista de usuários, filtrando : adicione na variavel user os valores que estão em usuários,
# se o valor da chave "Tweets" for igual a zero, quando for dar o print ele vai printar a variavel user
# OBS: precisa colocar em uma lista se não o Filter retorna somente o valor filter

print(filtro)


# Forma 2
filtro = list(filter(lambda user: not user["Tweets"], usuarios))
print(filtro)

"""


# Combinando Filter e Map

nomes = ['Vanessa', 'Ana', 'Maria', 'Mari', 'Sil']

# criar uma lista com "SUa intrutora é + o nome da instrutura" desde que o nome tenha menos
# de 5 caracteres

filtro = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
# o filter esta dentro de Map, dentro da lista nomes ai filtrar se os nomes são menores que 5,
#  aplicar a função do map, ou seja, se o nome for menor que 5 ele vai adicionar na variavel nome
# que vai gerar o print f'Sua intrutura é {nome que o  len é < 5}

print(filtro)
