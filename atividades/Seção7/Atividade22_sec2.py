"""
Um programa que recebe duas matrizes a e b 3x3
e calcule c = a * b
"""

matriza = [0, 0, 0], [0, 0, 0], [0, 0, 0]
matrizb = [0, 0, 0], [0, 0, 0], [0, 0, 0]

for l in range(0, 3):
    for c in range(0, 3):
        matriza[l][c] = int(input(f'digite um valor para [{l},{c}] da matriz A: '))

for l in range(0, 3):
    for c in range(0, 3):
        matrizb[l][c] = int(input(f'digite um valor para [{l},{c}] da matriz B: '))

print(matriza)
print(matrizb)

c = (sum(matriza[0]) + sum(matriza[1]) + sum(matriza[2])) * (sum(matrizb[0]) + sum(matrizb[1]) + sum(matrizb[2]))
