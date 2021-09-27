"""
Decorators com diferentes assinaturas

Para resolver quando temos dois objetos na função e somente um setado na função decorator pattern:

"""

"""
def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()

    return aumentar


@gritar
def saudacao(nome):
    return f'ola eu sou o/a {nome}'


@gritar
def ordenar(principal, acompanhamento):  # deve ser refatorado pois aqui ele tem 2 argumentos e na função só 1
    return f'Ola, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor'


print(saudacao('Rafael'))

print('\n')

print(ordenar('Picanha', 'Batata Frita'))
"""

"""
# Refatorando com decorator pattern *args, **kwargs

def gritar(funcao):
    def aumentar(*args, **kwargs):  # ele aceita qualquer quantidade de paramêtros
        return funcao(*args, **kwargs).upper()

    return aumentar


@gritar
def saudacao(nome):
    return f'ola eu sou o/a {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Ola, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor'


print(saudacao('Rafael'))

print('\n')

print(ordenar('Picanha', 'Batata Frita'))

print(ordenar(acompanhamento='Feijão', principal='Coxinha'))
"""


# Decorator com argumentos

def verifica(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto, primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna


@verifica('pizza')
def comida(*args):
    print(args)


@verifica(10)  # aqui o primeiro argumento precisa ser 10, se não entra no erro f'Valor incorreto
def soma_dez(num1, num2):
    return num1 + num2


print(soma_dez(10, 12))

print(soma_dez(1, 12))

print(comida('pizza', 'churrasco'))

print(comida('carne', 'churrasco'))