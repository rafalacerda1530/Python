"""
Default parameters

- um exemplo é o PRint que se vc não informar nada ele executa sem erro
ou seja o parametro da função é opcional

- os parametro default devem aparecer ao final da declaração:
def teste(a, b=15) se for inverso n funciona

- Podemos usar qualquer tipo de dados como valores default
- VAriavel local: somente em uma parte do codigo por exemplo se vc criar ela dentro de um loop
_variavel global :  abrange o sistema todo ex: a = 350
"""

"""
#  parametro pré definidoou valor opcional
def expo(numero=2, potencia=2):
    return numero ** potencia


print(expo(30))  # ele não vai dar erro pois a var potencia ja esta pré definida
# se eu digitar esse valor ele apenas subistitui

print(expo())  # # ele não vai dar erro pois a var numero ja esta pré definida
# se eu n digitar nada ele funciona
"""

"""
# exeplos

def info(nome='rafa', aluno=False):
    if nome == 'rafa' and aluno:
        return 'Bem vindo rafa'
    elif nome == 'rafa':
        return 'Eu pensei que vc era aluno'
    return f'Bem vindo {nome}'


print(info())
print(info(aluno=True))
print(info(nome=input('digite o nome')))
"""

"""
# FUnção em funções

def soma(n1, n2):
    return n1 + n2


def mat(n1, n2, fun=soma):
    return fun(n1, n2)


def sub(n1, n2):
    return n1 - n2


print(mat(2, 100))  # ele vai utilizar o função soma para somar o n1 e n2
print(mat(2, 100, sub))  # ele vai atribui o 2 ao n1 e o 100 ao n2
# e a fun=soma ele vai atribuir a função sub(subtração)
"""

"""

#  variavel global em funções
total = 0


def teste():
    global total  # avisando o Python qie vamos utilizar a var global
    # pois se declararmos ela local ela vai ter preferencia na local
    total = total + 1
    return total
    
se caso a variavel estiver dentro da função e você definir uma função dentro de função
e quiser reutilizar essa variavel utiliza-se "nonlical nome da variavel"

ex:


def teste():
    contador = 0

    def teste2():
        nonlocal contador

        contador = contador + 1
        return contador
    return teste2()


print(teste())
"""
