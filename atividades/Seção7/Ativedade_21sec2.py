"""
uma matriz 2x2 oferece as opções
a) somar as duas matrizes
b) subtrair a primeira da segunda
c? adicionar um valor em uma das matrizes
d) imprimir as matrizes
"""

matriz = [0, 0], [0, 0]

for l in range(0, 2):
    for c in range(0, 2):
        matriz[l][c] = int(input(f'digite um valor para [{l},{c}]: '))

menu = input('Deseja verificar o menu?: ')

while True:
    if menu == 'sim':
        print("""
    deseja:
    a) somar as duas matrizes
    b) subtrair a primeira da segunda
    c) adicionar um valor em uma das matrizes
    d) imprimir as matrizes : """)
        res = input()
        if res == 'a':
            soma = sum(matriz[0]) + sum(matriz[1])
            print(soma)
        elif res == 'b':
            soma = sum(matriz[0]) - sum(matriz[1])
            print(soma)
        elif res == 'c':
            print('deseja adocona na matriz a ou b?: ')
            res2 = input()
            if res2 == 'a':
                valor = int(input('digite o valor inteiro da matriz A: '))
                valor = matriz[0].append(valor)
                print(matriz)
            elif res2 == 'b':
                valor = int(input('digite o valor inteiro da matriz B: '))
                valor = matriz[0].append(valor)
                print(matriz)
        elif res == 'd':
            print(matriz)
    print('Processo finalizado, Deseja sair?: ')
    sair = input()
    if sair == 'sim':
        print('Agradeçemos a visita')
        break




