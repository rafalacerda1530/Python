"""
RANGES - FUNÇÃO AUXILIAR
Range é para gerar sequeências numéricas não de forma aleatória,
mas de maneira especificada

Forma geral:

range(valor de inicio, valor de parada)
ele sempre para um valor antes do digitado ex:
range(1, 11) o valor final vai ser 10 o 11 não é mostrado
você precisa indicar o valor de inicio, no caso acima é o 1

for num in range(4, 101):
    print(num)

caso quiser começar do zero é só n especificar o valor de inicio:
for num in range(101)
    print(num)
"""

# RAnge pulando de 2 em 10:

for num in range(1, 10, 2):  # ele tipo soma ex: 1+2 = 3+2 = 5 ...
    print(num, end='')

print('\n')

for num in range(10, 100, 10):  # de 10 até 100 pulando de 10 em 10
    print(num, end='')

print('\n')

# forma inversa
for num in range(10, 0, -1):  # começa em 10 vai até 0 diminuindo de 1 em 1
    print(num, end='')

print('\n')

lista = list(range(1, 11))  # vai criar uma lista com o range de 1 a 10
print(lista)
