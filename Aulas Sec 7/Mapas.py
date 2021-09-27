"""
MAPAS = DICIONÁRIOS
"""

"""
# ITERAR SOBRE DICIONARIOS
receita = {'jan': 100, 'fev': 120, 'mar': 300}

for chave in receita:
    print(chave)  # imprimindo as chaves

for chave in receita:
    print(receita[chave])
# imprimindo os valores das chaves em receita

for chave in receita:
    print(f'{chave} : {receita[chave]}')
# vai imprimir a chave e o valor
"""

"""
# printar somente as chaves
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita.keys())  # vai printar só as chaves do dic
"""

"""
# acessando os valores
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita.values())
# vai printar todos os valores

for valor in receita.values():
    print(valor)
"""

""""""

"""
# SOma, valor max, valor min, tamanho
# utilizamos somente se os valores forem int ou float

receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(sum(receita.values()))  # precisamos apontar que é
# somente o valor, pois esses comendos são para numeros
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
"""

