"""
Ordered Dict

"""

"""
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for chave, valor in dicionario.items():
    print(chave, valor)

# ele não garante esta ordem
"""
"""
# importando
from collections importteste OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(chave, valor)

# ele garante a ordem do dicionario
"""


from collections import OrderedDict
# Diferença entre dict e ordered dict

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
print(dict1 == dict2)  # True pq ele n armazena ordem

# ordered dict

dict3 = OrderedDict({'a': 1, 'b': 2})
dict4 = OrderedDict({'b': 2, 'a': 1})
print(dict3 == dict4)
# False pois a ordem dos elementos importa para o Ordered Dict
