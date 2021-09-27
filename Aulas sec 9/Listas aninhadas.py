"""
Listas aninhadas


"""

"""
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# para acessar os dados
print(listas[0][2])
# linha zero na coluna 2 vai printar o 3


# Iterando em listas aninhadas comprehesion
[[print(valor) for valor in lista] for lista in listas]
"""

# gerando tabuleiro o matriz 3x3
tabuleiro = [[numero for numero in range(1, 8)] for valor in range(1, 8)]
print(tabuleiro)
# o [for valor in range(1, 8)] cria as linhas e o [numero for numero in range(1, 8)] crias as colunas

velha = [['x' if numero % 2 == 0 else "o" for numero in range(1, 4)] for valor in range(1, 4)]
# o for valor in range (1,4) cria as linhas e o ['x' if numero % 2 == 0 else "o" for numero in range(1, 4)]
# cria as colunas
print(velha)

print([["1" if i / 2 == 1 else "*" for i in range(1, 6)] for j in range(1, 6)])
