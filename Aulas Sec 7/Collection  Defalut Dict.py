"""
Collection Defalut Dict

Defalut DIct não apresenta KeyError pois definimos um valor default
podendo utilizar um lambda pra isso, este sera utilizado quando não houver o valor
caso tentar acessar uma chave que n existe essa chave sera criado
e o valor default utilizado

- Lambdas são funçoes sem nomes que podem ou n receber parametros de entrada
e retornar valroes
"""

"""
dicionario = {'nome': 'rafael', 'sobrenome': 'lacerda'}

print(dicionario['nome'])  # printando na lista "dicionario" o valor de curso
"""

# Fazendo importteste
from collections import defaultdict

dicionario = defaultdict(lambda: 'não sei')

dicionario['nome'] = 'rafael'

print(dicionario['outro'])  # como n tem, ele vai pegar esse "outro"
# vai jogar na lista e adicionar o valor do lambda("não sei") a chave "outro"

print(dicionario)