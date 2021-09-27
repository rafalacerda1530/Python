"""
leia um numero entre 100 e 999 e imprima cada caracter dele
"""

num = int(input('digite um numero entre 100 e 999 : '))


if num < 100 or num > 999:
    print('valor incorreto')

while num < 100 or num > 999:
    print(f'por gentileza insira um valor que esteja entre 100 a 999')
    num = int(input())

y = str(num)  # Varoável que transforma o num que é int em str

for i in range(len(y)):
    print(f' os caracteres que compõe o numero {num} são {y[i]}')
