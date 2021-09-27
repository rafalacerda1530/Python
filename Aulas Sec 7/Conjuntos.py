"""
Conjuntos
São referência aos conjutnos da matematica
- no python são chamados de Sets
- não possuem valores duplicado
- não possuem valore ordenados
- elementos não são acessados via indice
- São bons para utilização quando precisamos armazenar elementos
mas não precisamos ordenar eles
- são referênciado com {}
- ACeita qualquer tipo de valor

# ele não aceita = set + set

Diferênça entre mapas:
DIcionario te chave/valo
conjunto tem valor
"""
"""
# Definindo um conjunto
 
s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})
print(s)

# se tiver valor repetido, ele é ignorado sem erros
# ele não aparece no print

# forma 2 mais comum
s = {1, 2, 3, 4, 5, 6, 7, 2, 5, 6}
print(s)
# se tiver valor repetido, ele é ignorado sem erros
# ele não aparece no print
"""

"""
# Iterando em um set
s = {1, 2, 3, 4, 5, 6, 7, 2, 5, 6}

for valor in s:
    print(valor)
"""

"""
# add em um conjunto
s = {1, 2, 3}

s.add(4)
print(s)
"""
"""
# remover elementos
s = {1, 2, 3}
s.remove(3)  # o 3 é valor
print(s)
# se o valor n for encontrado gera erro

# forma 2
s.discard(2)
print(s)
# se o valor n for encontrado não gera erro
"""

"""
# metodo matematico de conjunto
# 2 conjuntos, estudantes do curso python e do curso java

estd_py = {'MArcos', "Julia", 'CARLOS', 'Patricia'}
estd_java = {'Gabriel', 'Julia', 'Ana'}

# gear um conjunto unico

# forma 1 Union
unico1 = estd_py.union(estd_java)
print(unico1)

# forma 2 caractere pipe "|"
unico2 = estd_py | estd_java
print(unico2)

# ele não aceita = set + set
"""

"""
# gerar um conjunto dos estundates que estao nos 2 cursos
# intersction
estd_py = {'MArcos', "Julia", 'CARLOS', 'Patricia'}
estd_java = {'Gabriel', 'Julia', 'Ana'}

intr = estd_py.intersection(estd_java)
print(intr)

# forma 2 &
intr2 = estd_py & estd_java
print(intr2)
"""

"""
# gerar um conjunto de alunos que estão só em um curso
estd_py = {'MArcos', "Julia", 'CARLOS', 'Patricia'}
estd_java = {'Gabriel', 'Julia', 'Ana'}

sopy = estd_py.difference(estd_java)
sojava = estd_java.difference(estd_py)
print(sopy)
print(sojava)  # esta verificando se o mesmo valor esta em ambos conjuntos
# deixando quem esta somente em um
"""

