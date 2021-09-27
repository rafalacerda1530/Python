"""
Objetos - São instancias da classe, podemos pensar em objetos como variaveis inidas na classe
"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def check_lampada(self):
        return self.__ligada

    def ligar_desliga(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


class Contacorrente:
    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = Contacorrente.contador + 1  # para icrementar o contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__ligada = False
        Contacorrente.contador = self.contador  # para icrementar o contador + 1


class Produto:
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id + 1

    def desconto(self, porcentagem):
        return (self.__valor * (100 - porcentagem)) / 100


"""
lamp1 = Lampada('Azul', 120, 'Alta')

print(f'A lampada esta ligada? {lamp1.check_lampada()}')

conta = Contacorrente(50000, 2000)

prod = Produto('Play 4', 'slim', 2300)
"""
