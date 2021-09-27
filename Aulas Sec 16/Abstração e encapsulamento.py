"""
Abstração e encapsulamento

POO - Encapsular os  códigos dentro de um grupo lógico e hierarquico

PAra acessar atributo fora da classe instancia_CLasse__atributo

Abstração : é o ato de expor apenas dados relevantes de um classe

o Atributo privado é importante para não ter alterações nos atributos fora da classe
"""


class Conta:
    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if valor > 0:
            self.__saldo -= valor
        else:
            print('o valor precisa ser maior que 0')


conta1 = Conta('Rafa', 4000, 1300)

print(conta1.__dict__)  # para verificar os atributos

conta1.depositar(150)

print(conta1.__dict__)
