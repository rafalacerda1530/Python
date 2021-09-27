"""
Metadata e Wraps

Metadata - são informações do arquivos, como propriedades e mais...

Wraps - São funções que envolvem elementos com diversas finalidades

o wraps vai mostrar a documentação de cada decorator, assim não confunde quem for ler a documentação do seu código

"""

"""
# Problema


def ver_log(funcao):
    def logar(*args, **kwargs):  # utilizamos args e kwargs para poder utilizar a quantidade de elementos qualquer
        ""Eu sou uma função Logar dentro da outra""
        print(f'você esta chamando {funcao.__name__}')  # __name__ da o nome da função
        print(f'Aqui a documentação: {funcao.__doc__}')  # __doc__ da a documentação
        return funcao(*args, **kwargs)

    return logar


@ver_log
def soma(a, b, c):  # por utilizarmos args e kwargs, podemos colocar qualquer numero aqui
    "soma dois numeros"
    return a + b + c


# print(soma(10, 30, 2))

print(soma.__name__)  # deveria ter soma
print(soma.__doc__)  # deveria ter "soma dois numeros"

# obs: o erro é que ao verificarmos a documentação da função, ela vai apresentar a documentação(metadados) da função
ver_log, e o certo seria da propria funçãosoma
"""

# Solução

from functools import wraps


def ver_log(funcao):
    @wraps(funcao)  # ao utilizar o wrap ele trás a documentação de cada função
    def logar(*args, **kwargs):  # utilizamos args e kwargs para poder utilizar a quantidade de elementos qualquer
        """Eu sou uma função Logar dentro da outra"""
        print(f'você esta chamando {funcao.__name__}')  # __name__ da o nome da função
        print(f'Aqui a documentação: {funcao.__doc__}')  # __doc__ da a documentação
        return funcao(*args, **kwargs)

    return logar


@ver_log
def soma(a, b, c):  # por utilizarmos args e kwargs, podemos colocar qualquer numero aqui
    "soma dois numeros"
    return a + b + c


# print(soma(10, 30, 2))

print(soma.__name__)  # deveria ter soma
print(soma.__doc__)  # deveria ter "soma dois numeros"
