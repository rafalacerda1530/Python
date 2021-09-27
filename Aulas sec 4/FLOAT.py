"""
Tipo FLOAT/ REAL/ DECIMAL

O separador de decimais é o ponto e não virgula

#  dupla atribuição de valores da variavel
valor1, valor2 = 1, 44

Numeros complexos = varJ = variavel+j
"""

"""
valor = 1.44  # O separador de decimais é o ponto e não virgula
print(type(valor))

#  dupla atribuição de valores da variavel
valor1, valor2 = 1, 44
print(valor1)
print(valor2)

res = int(valor)
print(res)
print(type(res))  # ao converter FLoat para INT perdemos precisão
"""

raio = float(input())

n = 3.14159

area = (raio ** 2) * n

# print('A={:.4f}'.format(area))  # :.4f serve para colocar 4 casas após o decimal

print(f'A={area:.4f}')  # :.4f serve para colocar 4 casas após o decimal, o 4 smostra a quantidade
# de casas

print('A={:.4f}'.format(area))

# PODEMOS UTILIZAR DA SEGUINTE FORMA TBM

print('AREA = %.4f' % area)
