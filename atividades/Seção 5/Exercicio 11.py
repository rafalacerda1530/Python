"""
Digite um numero e devolva a soma de seus algarismos ex:
215 = 2+1+5 = 8
"""
numero = input('Número: ')

if len(numero) == 8:  # LEN LE OS CARACTERES
    print(sum(map(int, numero)))
else:
    print('NAO SEI')
