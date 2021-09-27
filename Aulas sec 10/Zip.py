"""
Zip

- tipo: <zip object at 0x7fdb1b53c820>

- ele pega os elementos e forma pares:

lista1 = [1, 2, 3]
lsita2 = [4, 5, 6]
[(1, 4), (2, 5), (3, 6)]

- ele forma tuplas

- ele some da memória após execução

- se os elementos de algum iteravel for maior que outro, ele ignora
"""

"""
lista1 = [1, 2, 3]
lsita2 = [4, 5, 6]

zip1 = zip(lista1, lsita2)
print(zip1)

print(list(zip1))


lista3 = [7, 8, 9, 10]

zip1 = zip(lista1, lsita2, lista3)
print(list(zip1))
"""

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

final = {dado[0]: max([dado[1], dado[2]]) for dado in zip(alunos, prova1, prova2)}
print(final)

# esta como se fosse uma matriz a posição 0 é a lista alunos, o 1 é a prova 1, e o 2 é a prova 2
# dado na posição 0 (alunos sera a chave), coloque para dado na posição 0 os valores do zip
# da posição 1 (prova1) e posição 2 (prova2),

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
# o zip de prova 1 e prova 2 esta sendo passado como parametro para o map,
# que vai pegar a maior nota e distribuir no zip de alunos

print(dict(final))