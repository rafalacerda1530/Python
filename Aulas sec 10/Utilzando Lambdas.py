"""
Lambdas

- Funções anonimas (sem nome)
- Podemos ter lambdas com multiplas entradas
- variavel.strip remove espaços de ums string
- variavel.title tornar a primeira letra do nome maiusculo
- utilizadas mais para filtragem de dados e ordenação

print(max(musicas, key=lambda musica: musica['Tocou'])['TItulo'])  # desse objeto informe somente a chave titulo
"""

"""
# Jeito não correto

complete_name = lambda name, last_name: name.strip().title() + " " + last_name.strip().title()


print(complete_name('rafael', 'lacerda'))
"""

"""
autores = ['rafael lacerda', 'givaldo rodrigues', 'edilma santos', 'karen silva', 'dalva dorth']

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].title())

print(autores)
"""


# função quadratica
# f(x) = a * x ** 2 + b * x + c

def quadratica(a, b, c):
    return lambda x: a * x ** 2 + b * x +c
#  a função vai receber os valores a, b e c, e vai retornar o lambda


#  abaixo estamos colocando os valores da função (a, b, c)
teste = quadratica(2, 3, 5)


#  no print estamos colocando o valor x do lambda return lambda ''X'': a * x ** 2 + b * x +c
print(teste(3))
print(teste(5))
print(teste(7))


print(quadratica(3, 4, 7)(5))  # 3, 4, 7 São os valores da função (a, b, c) e o (5) é o valor
#  X da lambda
