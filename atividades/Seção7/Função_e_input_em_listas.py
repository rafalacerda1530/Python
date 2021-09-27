"""
Teste de função com input em listas
"""


def listas(a):
    pri1 = 1
    while len(a) != 10:
        a = a + [int(input(f'dite o {pri1} valor para a: '))]
        pri1 += 1
    return a


print(listas(a=[]))


