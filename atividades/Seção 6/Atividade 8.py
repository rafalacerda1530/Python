"""
Programa que leia a quantidade de um numero e imprima o maior deles
e quantas vezes ele foi lido, a quantidade de numeros lidos,
deve ser indicada pelo usuário
"""

num1 = int(input('digite o primeiro num: '))
num2 = int(input('digite o segundo num: '))
num3 = int(input('digite o terceiro num: '))
rept = 0

if num1 > num2 and num1 > num3:
    print(f'{num1} é o maior')

elif num2 > num1 and num2 > num3:
    print(f'{num2} é o maior')

else:
    print(f'{num3} é o maior')

qntd = int(input("quantas vezes repetilos?: "))

while qntd != rept:
    print(num1, num2, num3)
    rept = rept +1

if num1 > num2 and num1 > num3:
    print(f'o numero {num1} foi lido {qntd} de vezes')

elif num2 > num1 and num2 > num3:
    print(f'o numero {num2} foi lido {qntd} de vezes')

else:
    print(f'o numero {num3} foi lido {qntd} de vezes')

