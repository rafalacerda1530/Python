"""
DADOS CONSIDERADOS STRING

QUANDO ESTÃO ENTRE:

ASPAS SIMPLES ''
ASPAS DUPLAS ""
ASPAS SIMPLES TRIPLAS ''' '''
ASPAS DUPLAS TRIPLAS """ """
- variavel.strip remove espaços de ums string
- variavel.title tornar a primeira letra do nome maiusculo

help = informa o que uma função faz
"""

"""
nome = 'rafael'
print(nome)
print(type(nome))

nome2 = "gina's bar"
print(nome2)
print(type(nome2))

nome3 = 'rafael \nlacerda'  # o "\n" pula uma linha
print(nome3)

nome4 = """rafa
lacerda"""  # pula uma linha
print(nome4)

nome5 = 'rafa lacerda'
print(nome5.upper())  # muda tudo para maiusculo

nome6 = 'RAFA LACERDA'
print(nome6.lower())  # tudo para monusculo

nome7 = 'rafa lacerda'
print(nome7.split())  # lista os nomes  ['rafa', 'lacerda'] rafa = posi 0, lacerda pos =1

#  slice de string
nome8 = 'rafa lacerda'
print(nome8[0:5])  # ele vai printar o nome da letra na posição 0 = R
# até a posição 5 = noca so é o espaço mas ele vai mostrar uma antes ou seja o A
print(nome8[::-1])  # comece do primeiro elemento va até o ultimo e inverta,
#  ou seja inverte as palavras
print(nome8.replace('r', 'l'))  # subistituir o r pelo l

print(''.join(list(reversed('rafael'))))  # vai juntar os espaços da lista
"""

A = int(input())

B = int(input())

SOMA = A + B

print("SOMA =", SOMA)  # PODE SER PRINTADO ASSIM