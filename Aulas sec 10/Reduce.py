"""
- precisa ser importado do functools
- recebe dois parametros (função, Iteravel)
- precisamos pasar dois parametros
ex:

etc = [a1, a2, a3]

def func(x, y):
    return x * y

reduce vai pegar da coleção etc e fazer da seguinte forma:

ele pega os dois primeiros valores da coelçao (a1, a2) aplica a função
o resultado ele guarda na variavel e utiliza esse resultado como parametro
da função para o proximo valor (a3), e isso se aplica sucetivamente

ele utiliza o resultado anterior como parametro para a função e o proximo valor
e assim sucetivamente
"""

# Exemplo
# multiplicando todos os numeros da lista

from functools import reduce

dados = [2, 3, 7, 8, 10, 15, 28, 37, 45]

# para utilizar o reduce utilizamos um função de 2 parametrs

multi = lambda x, y: x * y  # dois parametros (x, y)

res = reduce(multi, dados)
print(res)

res = 1

for n in dados:
    res = res * n

# para cada valor in dados faça: res vai ser igual a res vezes cada valor
# vai pegar o 2 e fazer vezes 1 o resultado ele adiciona em res
# e depois faz o res vezes o proximo valor

print(res)