"""
LEIA UM SALÁRIO E UM VALOR DE PRESTAÇÃO DE EMPRESTIMO,
SE A PRESTAÇÃO FOR MAIOR QUE 20 % DO SALÁRIO IMPRIMA:
"EMPRÉSTIMO N CONCEDIDO"
SE NÃO:
"EMPRESTIMO CONCEDIDO"
"""

print('INSIRA SEU SALÁRIO')
salario = float(input())

print('INSIRA O VALOR DA PRESTAÇÃO')
prestacao = float(input())

if prestacao > (salario * 20) / 100:
    print('Empréstimo não concedido')
else:
    print('Empréstimo concedido')
