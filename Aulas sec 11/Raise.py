"""
Levantando os próprios erros com Raise

apresenta erros onde você pode personaliza-los

raise -> lança excessões, é uma palavra reservada

util para criar nossas proprias excessões e mensagens de erro

raise TipodeErro(mensagem de erro)

o raise finaliza a função, nada após ele sera executado
"""
"""
# altera a mensagem do erro

raise ValueError("Valor esta incorreto")
"""

"""
# exemplo
def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError("Texto precisa ser uma string")
    if type(cor) is not str:
        raise TypeError(" Cor precisa ser uma string")
    print(f'O texto {texto} sera impresso com a cor {cor}')


colore('Rafa', 'Azul')

colore('Rafa', 4)

colore(4, 'azul')
"""


def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError("Texto precisa ser uma string")
    if cor not in cores:
        raise ValueError(f'A core precisa estar entre {cores}')
    if type(cor) is not str:
        raise TypeError(" Cor precisa ser uma string")
    print(f'O texto {texto} sera impresso com a cor {cor}')


colore('Rafa', 'azul')
colore('Rafa', 'Cinza')
