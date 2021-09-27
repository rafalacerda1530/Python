"""
entendendo iterator e iterables

iterator:
- Um objeto que pode ser iterado
- um objeto que retona um dado em uma função
- todos os valores como tuplas, listas e etc
- o retorno do dado seria algum valor dentro do iteravel
- quando podemos utilizaar a função next()

iterables:
- um objeto que retorna um iterator quando a função iter() é chamada
- ele vai retornar um iterator e o iterator vai retornar o dado
"""

"""
nome = 'rafael'  # é um iterable mas não é um iterator
numeros = [1, 2, 3, 4, 5]  # é um iterable mas não é um iterator

it1 = iter(nome)  # a função iter() torna ele um iterável
it2 = iter(numeros)

print(next(it1))  # ele vai printar cada letra do nome ex: aqui ele printa a letra r
print(next(it1))  # letra a
print(next(it1))  # letra f
print(next(it1))

print(next(it2))  # ele vai printar o numero 1 e assim sucessivamente
"""

