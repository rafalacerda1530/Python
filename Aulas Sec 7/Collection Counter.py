"""
Counter - High performance container datetype
- Recebe um iteravel com parametro e cria um onjeto do
tipo collections counter parecido com dicionarios,
contendo chave e elemento da lista passada como parametro,
e como valor a qyuantidade de ocorrencias

- Podemos utilizar qualquer Iterável

- chave: ocorrência
"""

"""
# utilizando o Counter

from collections importteste Counter  # importando a biblioteca

lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

res = Counter(lista)

print(type(res))
print(res)
#  ele vai printar informando: pro elemento 1 eu encontrei 6 ocorrencias ou seja:
# ele encontrou o numero 1 seis vezes, igualmente para os outroas numeros
# ele encontrou uma chave e colocou como valor o numero de ocoorrencias
"""

"""
from collections importteste Counter  # importando a biblioteca

print(Counter('Rafael Lacerda'))
# ele vai pegar cada letra e colocar como chave e como valor vai colocar a ocorrencia
# ou seja quantas vezes é repetido e ordenar do maior para menor
"""


from collections import Counter  # importando a biblioteca

texto = """Old pirates, yes, they rob I
Sold I to the merchant ships
Minutes after they took I
From the bottomless pit
But my hand was made strong
By the and of the almighty
We forward in this generation
Triumphantly
Won't you help to sing
These songs of freedom?
'Cause all I ever have
Redemption songs
Redemption songs"""

palavras = texto.split()

res = Counter(palavras)
print(res)

#  vai pegar cada palavra e colocar como chave e quantas vezes essa palavra
# aparece como ocorrencia

# encontrando as 5 palavras com mais ocorrencias (mais comuns)
print(res.most_common(3))
