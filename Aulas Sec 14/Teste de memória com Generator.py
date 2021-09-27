"""
Testes de memória com geradores

Sequência de fibonacci:

1, 1, 2, 3, 5, 8, 13 # ele soma 1 + 1 = 2 e depois 2+1 = 3 e depois 3+2 = 5 ...
"""


def fibonacci_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums


# teste 1 lista (449 mb)
# for n in fibonacci_lista(100000):
#   print(n)


def fibonacci_generator(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador = contador + 1


# teste 2 generator (3 MB)
for n in fibonacci_generator(100000):
    print(n)
