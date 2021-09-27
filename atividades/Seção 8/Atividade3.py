"""
Uma função para verificar se um numero é positivo ou negativo,
retornar 1 se posisitivo e -1 se negativo e 0 se for igual a zero
"""


def positivo_ou_negativo(num):
    if num < 0:
        return f"Numero {num} é negativo"
    elif num == 0:
        return f"Numero {num} é Neutro"
    return f"Numero {num} é positivo"


a = int(input("Digite um numero positivo ou negativo: "))
print(positivo_ou_negativo(a))
