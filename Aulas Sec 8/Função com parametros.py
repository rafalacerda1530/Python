"""
Funções com parametros

-Funções que recebm dados

- FUnções Podem receber N parametros, podemos receber
quantos parametros quisermos e els são separados por
virgula

- o Return deve ser colocado no bloco da função
"""

"""
#  ela recebe um parametro e é obrigatorio colocar por ex: print(quadrado(2))
#  o 2 é o parametro


def quadrado(numero):  # o metodo vai receber um valor(numero) e vai fazer
    #  numero * numero
    return numero * numero  


print(quadrado(2))  # numero * mumero = 2*2
"""

"""
# refatorando


def cantar_parabens(aniversariante):
    print('Parabens para você')
    print('Nessa data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o/a {aniversariante}')


cantar_parabens('Rafael')
"""

"""
# FUnções com varios parametros


def soma(a, b):
    return a + b


def mult(num1, num2):
    return num1 * num2


def outra(num1, b, msg):
    return (num1 + b) * msg


print(soma(10, 10))  # valor de a e b
print(mult(10, 10))  # valor de num1 e num2
print(outa(10, 10, "A"))  # valor de num1 b e msg
# ta fazendo o resultado de num1 + b vez o a
# ou seja 20 vezes o B
"""

"""
# Nomeando paranmetros


def nome_completo(nome, completo):  # eles devem fazer sentido
    return f"Seu nome completo é: {nome} {completo}"


print(nome_completo(input('Digite o primeiro nome: '), input('digite o sobrenome: ')))


# A diferença entre parametros e argumentos
# Parametros são variaveis decladas na definição de uma função
# def nome_completo(nome, completo): # parametro é o nome, completo
# Argumentos são dados passados durante a execução de uma função
# print(nome_completo(input('Digite o primeiro nome: ') o input é o argumento
"""

"""
# Argumento nomeado (keyword arguments)
def nome_completo(nome, completo):  # eles devem fazer sentido
    return f"Seu nome completo é: {nome} {completo}"


a = input('Digite o nome: ')
b = input('Digite sobrenome: ')

print(nome_completo(nome=a, completo=b))
"""


