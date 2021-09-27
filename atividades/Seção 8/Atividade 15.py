"""
Receba 3 valores obrigatoriamente maiores que zero, representado os 3 lados de um
triangulo, elabore as funções para:

- Determinar se eles formam um triangulo sabendo que :
* o comprimento e um lado de um triangulo é menor do que a soma dos dois lados

- Determinar o tipo de triangulo:
* Triangulo: 3 lados iguais
* Isóceles: tem o cumprimento de dois lados iguais
* escaleno: cumprimento dos 3 lados diferentes
"""

lado1 = int(input("Digite o lado 1: "))
lado2 = int(input("Digite o lado 2: "))
lado3 = int(input('Digite o lado 3: '))


def confir_triangulo(lad1=1, lad2=2, lad3=3):
    if lad1 > lad2 + lad3 or lad2 > lad1 + lad3 or lad3 > lad2 + lad1:
        while lad1 > lad2 + lad3 or lad2 > lad1 + lad3 or lad3 > lad2 + lad1:
            print("Isso não é um triangulo")
            lad1 = int(input('Digite o lado 1 corretamente: '))
            lad2 = int(input('Digite o lado 2 corretamente: '))
            lad3 = int(input('Digite o lado 3 corretamente: '))


def tipo_triangulo(ladotri1=1, ladotri2=2, ladotri3=3):
    confir_triangulo(ladotri1, ladotri2, ladotri3)
    if ladotri1 == ladotri2 and ladotri1 == ladotri3:
        print("Triangulo comum")
    elif ladotri1 == ladotri2 or ladotri1 == ladotri3 or ladotri2 == ladotri3:
        print("Triangulo Isóceles")
    print("Triangulo Escaleno")

    while True:
        sair = input("Deseja sair ?: ")
        if sair != 'sim':
            tipo_triangulo(ladotri1, ladotri2, ladotri3)
        else:
            break
    return "Obrigado !"


print(tipo_triangulo(lado1, lado2, lado3))
