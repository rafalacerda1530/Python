"""
List comprehesion parte 2

podemos adicionar estrutura condicionais logicas as lists
"""


numeros = [1, 2, 3, 4, 5]

pares = [numero for numero in numeros if numero % 2 == 0]
# for = para cada numero in numeros, salva ele em numero se o resto for igual a 0
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
# Lembrando de começar pelo for, para cada numero in numeros faça numero* 2:
# se numero % 2 == 0 se o resto divido por 2 for diferente de zer faça
# numero / 2
print(res)