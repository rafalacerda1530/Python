"""
DICIONÁRIOS
SÃO COLEÇÕES DO TIPO CHAVE/VALOR

SÃO REPRESENTADIS POR CHAVES {'br': 'Brasil', 'EUA': 'Estados Unidos'}

chave e valor podem ser de qualquer dado

o tipo None pode ser usado quando queremos uma variavel sem o tipo
pois eu n sei o que vai ser incluido la

Em dicionários n podemos ter chaves repetidas

- values retorna somente o valor
"""

"""
# criando dicionarios forma comum:
paises = {'br': 'Brasil', 'EUA': 'Estados Unidos'}
print(paises)
print(type(paises))
"""

"""
# forma menos comum
paises2 = dict(br='Brasil', eua='Estado unidos')
print(paises2)
"""

"""
# acessando elementos via chave
paises = {'br': 'Brasil', 'us': 'Estados Unidos', 'py': 'paraguai'}
print(paises['br'])
print(paises['py'])

# acessando elementos via get - recomendado
print(paises.get('br'))
print(paises.get('us'))
print(paises.get('ru'))  # qnd n tem o elemento ele retorna valor none
# ele não da erro

#  a variavel pais esta procurando o que tem no elemento da chave py
#  caso ele n encontre, ele retorna a segunda chave que é um valor
#  padrão definido
pais = paises.get('py', 'não encontrado')
print(f'encontrado o pais {pais}')
"""

"""
# verificar se tem a chave br no dicionario paises
paises = {'br': 'Brasil', 'us': 'Estados Unidos', 'py': 'paraguai'}
print('br' in paises)
if 'br' in paises:
    brasil = paises['br']  # a variavel brasil esta recebendo o valor
    print(brasil)          # da chave 'br'
"""

"""
# podemos utilizar tuplas pois elas n podem ser alteradas
localidades = {
    (34.0255, 12.355): 'Escritorio São paulo',
    (22.4000, 90.541): 'Escritorio São paulo',
    (37.5842, 49.548): 'Escritorio São paulo',
}
"""

"""
# Adicionar elementos em dicionários
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)

# forma1 mais utilizada
receita['abr'] = 400
print(receita)

# forma 2
receita2 = {'mai': 500}
receita.update(receita2)  # receita.update("mai": 500)
print(receita)
"""

"""
# Atualizando dados em dicionários

# forma1
receita = {'jan': 100, 'fev': 120, 'mar': 300, 'mai': 500}
print(receita)
receita['mai'] = 550
print(receita)

# forma 2
receita.update({'mai': 500})
print(receita)
"""

"""
# Removendo dados de um dicionário
receita = {'jan': 100, 'fev': 120, 'mar': 300, 'mai': 500}
print(receita)

# forma1
ret = receita.pop('mar')  # para excluir, precisa ser a chave
# no print ele vai retornar o valor que foi removido no pop
print(ret)
print(receita)

# forma2

del receita['fev']  # esta excluindo a chave e valor 'fev'
print(receita)
"""

# E-commerce

"""
produto 1, nome, qntd, preço
produto 2, nome, qntd, preço
"""

"""
# utilizando lista
carrinho = []

prod = ['Play Station4', 1, 2300]
prod1 = ['Play Station9', 1, 17300]
# em uma lista, teriamos que saber o indice de cada informação
# do produto

# Utilizando Tupla
prod1 = ('Play Station4', 1, 2300)
prod2 = ('Play Station9', 1, 17300)

carrinho = (prod1, prod2)
# também teremos que saber o indice


# Utilizando dicionário:
carrinho = []
prod1 = {'nome': 'Play Station4','qntd': 1,'prec': 2300}
prod2 = {'nome': 'Play Station9','qntd': 1,'prec': 17300}

carrinho.append(prod1)
carrinho.append(prod2)
print(carrinho)
"""

"""
# metodo n tão usual de cração de dicionarios
dici = {}.fromkeys(['nome', 'pontos', 'email'], 'desconhecido')
print(dici)  # dentro da lista "[]" viram chaves, o valor fora dela
# vira o valor dessas chaves

veja = {}.fromkeys('digame', 'valor')
# para cada letra da chave ele adiciona o valor
print(veja)

veja = {}.fromkeys(range(1, 11), 'valor')
print(veja)    # para cada valor no range, ele adiciona o "valor
# em um dicionario
"""

"""
book = {}  # empty dict!
book["title"] = input("Book title: ")

book é um dicionário vazio

book[title] = input chave = title, valor =  input
"""

def pegavalor(dic, chave):
    return dic[chave]


dic = {'nome': 'Rafael'}

print(pegavalor(dic, 'nome'))  # estou colocando a chave nome, ele retorna o valor

