"""
LEia um numero real, se for positivo calcule a raiz quadradad,
se for negativo mostre que o numero é invalido
"""

print('Digite um numero')

num = float(input())

if num >= 0:
    raiz = num ** 1/2
    print(f'a raiz é\n{raiz}')
else:
    print('numero invalido')
