"""
Funções com retorno

# o "return" executa o retorno da função

Return: Finaliza a função
podemos em uma funçaõ ter mais de um return
retornar qualquer tipo de dado e até mesmo multiplos valroes

"""

"""
# exemplos:
def quadrado_de_7():
    print(7 * 7)


ret1 = quadrado_de_7()  # aqui ele esta executando o print sem valor atribuido


# refatorando a função
def quadrado_de_7_2():
    return 7 * 7
# o "return" executa o retorno da função, vai retornar o result do 7 * 7


ret = quadrado_de_7_2()  # ele retorna o calculoo adicionando o resultado na var ret
print(ret)
"""

"""
# refatorando def diz_oi():  se ele for assim da erro pois staria
#     print('Oi')            somando none + string


def diz_oi():
    return 'oi '


a = 'Rafael'

print(diz_oi() + a)
"""

"""
# Return: Finaliza a função
def diz_oi():
    # print('Essa linha sera executada')
    return 'oi '  # finaliza a função
    # print('Essa linha nunca sera executada')
"""

"""
#  podemos em uma funçaõ ter mais de um return
def new():
    vari = None
    if vari:  # se variavel for Verdadeira:
        return 4
    elif vari is None:
        return 3.2
    else:
        return 'b'


print(new())
"""

"""
# retornar qualquer tipo de dado e até mesmo multiplos valroes
def outra():
    return 2, 3, 4, 5


num1, num2, num3, num4 = outra()

print(num1, num2, num3, num4)
# estou atribuindo cada valor da função a uma variavel
"""

"""
# cara ou coroa?
from random importteste random


def joga_moeda():
    # gera um numero pseud-randomico entre 0 e 1
    if random() > 0.5:
        return 'Cara'
    else:
        return 'coroa'


print(joga_moeda())
"""


#  erros de codificação desnecessaria comuns com return
def impar():
    numero = 5
    if numero % 2 !=0:
        return True
    else:  # Não precisa do else
        return False


def impar2():
    numero = 5
    if numero % 2 != 0:
        return True
    return False  # mesma utilização do Else


print(impar2())
