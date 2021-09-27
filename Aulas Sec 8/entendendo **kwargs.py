"""
**Kwargs

Diferente do *args qu coloca os valores em tuplas o **kwargs precisa de
parametros nomeados e os tranformam em dicionario

# caso for utilizar todos os parametros,
# segue nessa ordem as declarações
# Parametros obrigatórios
# *args
# parametros default
# **kwargs
"""

"""
def cor(**kwargs):
    print(kwargs)

cor(marcos='verda', gabriel='azul', julia='amarelo')
"""

""""
def cor(**kwargs):
    for pessoa, cores in kwargs.items():
        print(f'A cor avorita de {pessoa.title()} é {cores} ')


cor(marcos='verde', gabriel='azul', julia='amarelo')
"""

"""
def cumprimento(**kwargs):
    if 'rafa' in kwargs and kwargs['rafa'] == 'python':
        # acima estamos verificando se a chava 'rafa' possui o valor 'python'
        return 'Você foi comprimentado'
    elif 'rafa' in kwargs:
        return f"{kwargs['rafa']} 'rafa' "
        # acima, caso o valor não for igual a python, ele vai adicionar
        # a chave no kwargs e retornar conforme mostrado
        # print(cumprimento(rafa='oi')) no caso aqui vai retornar oi rafa
    return 'Não sei quem é vc'


print(cumprimento())
print(cumprimento(rafa='python'))
print(cumprimento(rafa='oi'))
print(cumprimento(rafa='especial'))
"""

"""
# caso for utilizar todos os parametros,
# segue nessa ordem as declarações
# Parametros obrigatórios
# *args
# parametros default
# **kwargs


# idade e noem são obrgatorios
# args vãos ser as tuplas e n são obrigatórios
# SOlteiro esta false
#kwargs não é obrigatorio e vai criar o dicionário

def func(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('solteiro')
    else:
        print('casado')
    print(kwargs)


func(8, 'julia')
func(18, 'rafa', eu='NÃO', voce="VAi")
func(18, 'fernando', 12, 15, 16, solteiro=True)
func(27, 'carla', 9, 4, 56, 7, java=True, Python=False)
"""

"""
# Desepacontando

def mostranome(**kwargs):
    return f"{kwargs['nome']}, {kwargs['sobrenome']} "


nomes = {'nome': input('DIGITE SEU NOME: '), 'sobrenome': input('DIGITE SEU SOBRENOME: ')}
print(mostranome(**nomes))  # utilizamos o "**" para desempacotar ou seja:
# na kwargs ele vai adicionar o valor para a chave nome, o kwargs sera um valor padrão
"""


list = [input()]

print(list)