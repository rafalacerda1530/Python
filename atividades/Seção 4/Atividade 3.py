"""
CAlcule um sário com adicionamento de 5%
porém ele tem um multa de 7%
"""
print('INSIRA O SALÁRIO')

sal = float(input())

sal = sal * 5 / 100 + sal
print('Seu salario com a gratificação é', sal, 'reais \n')

desc = sal - sal * 7 / 100
print('Seu salário com o desconto é', desc)