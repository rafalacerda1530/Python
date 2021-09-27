"""
Map

- fazemos mapeamento de valores para função
- recebe dois parametros: uma função, o iteravel(valor)
- tipo map object, se for printar os valores, precisa colocar em uma lista
ou alguma coleção
- após utilizar a função map ele não salva a variavel ou seja ele zera
- map recebe funão e valor
"""

"""
# calculando a area de um circulo

importteste math


def area(r):
    Calcula a area de um circulo com raio r
    return math.pi * (r ** 2)'


print(area(2))
print(area(5.3))


# abaixo uma lista com varios raios

raios = [2, 5, 7, 10, 44, 0.3]


#  utilizando map

#  - recebe dois parametros: uma função, o iteravel (no caso a lista raios)
areas = map(area, raios)  # ele vai pegar cada valor de raios e colcoar
#  como parametro para a entrada da função e armazenar em um objeto do
# tipo map, que no print abaixo colocamos em uma lista


print(areas)
print(type(areas))
print(list(areas))


# MAP COM LAMBDA


# abaixo é o mesmo
print(list(map(lambda r: math.pi * (r ** 2), raios)))
#  ele pega o valor de raios e adiciona em r e faz o calculo
#  adicionamos os resultados em uma lista
"""

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ("Los angeles", 26), ('Tokio', 27), ('New york', 28)]

# f = 9/5 + c + 32

# Lambda


c_para_f = lambda dado: (dado[0], (9 / 5 * dado[1] + 32))
# a lambda dado vai pegar o dado na posição 0 que é o nome e manter, e vai pegar o valor(dado[1])
# na posição 1 e realizar o calculo : 9 / 5 * dado[1] (obs: esse valor é para o c da formula: f = 9/5 + c + 32)

print(list(map(c_para_f, cidades)))
# aqui ele esta passando a função e utilizando a lista de cidades como parametro
