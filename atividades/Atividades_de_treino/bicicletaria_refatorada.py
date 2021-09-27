# -*- coding: utf-8 -*-
"""
Criar um software que armazene estoque, consulte produtos, realize vendas e ao realizar a venda exclua este
produto do estoque, receba um alerta ao vender um produto se o estoque tiver menos de 10 produtos, consultar lucro do dia
"""


class Product:
    stock = []
    yes = 'y'

    @classmethod
    def remove(cls, prod):

        stoc = Product.stock
        for product in stoc:
            if product['name'] == prod:
                stoc.remove(product)
                print(stoc)

    def __init__(self, name, value, amount):
        self.__name = name
        self.__value = value
        self.__amount = amount

    @classmethod
    def add(cls):
        name = input("Digite o nome produto: ")
        value = input('digite o valor do produto: ')
        amount = input('Digite a quantidade para o estoque: ')

        prod = {'name': name, 'value': value, 'amount': amount}
        Product.stock.append(prod)
        print(Product.stock)
        res = input("do you want to add a new product (y/n) ?: ")
        if res == Product.yes:
            Product.add()
        else:
            print("BYE")


def consult_prod():  # function to consult stock

    stock = Product.stock

    if not stock:
        print("Stock empty")
        consult_prod()

    print('\n')

    product = input("Type product name or type * for all products: ")

    for prod in stock:

        if prod['name'] == product:
            print(f"Produto: {prod['name']}, Quantidade em estoque: {prod['amount']}, Valor: {prod['value']}")
        elif product == '*':
            print(Product.stock)

        else:
            print("Produto não existe, digite um produto que contenha no stock")
            consult_prod()

    res = input("Deseja fazer outra pesquisa?: ")
    if res == 'yes':
        consult_prod()
    else:
        print("BYE")
        return


Product.add()
