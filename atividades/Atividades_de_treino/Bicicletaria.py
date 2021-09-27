# -*- coding: utf-8 -*-
"""
Criar um software que armazene estoque, consulte produtos, realize vendas e ao realizar a venda exclua este
produto do estoque, receba um alerta ao vender um produto se o estoque tiver menos de 10 produtos, consultar lucro do dia
"""
import pydf

#  Variable definition
# The variable res, is the condition to module
# and stock, where the products will be add

stock = []
res1 = "1"
res2 = "2"
res3 = "3"
res4 = "4"
res5 = "5"
res6 = "6"
sold = []


def run():  # answer to module decision  # user's decision of module
    print("What do you wish ??"
          "\n"
          "1 - Consult Stock"
          "\n"
          "2 - Consult product value"
          "\n"
          "3 - Add new product"
          "\n"
          "4 - Remove a product"
          "\n"
          "5 - Sales"
          "\n"
          "6 - see the value sold today"
          "\n"
          "7 - Exit")

    answer = input("Type the Module: ")
    if answer == '1':
        consult_stock()
    elif answer == '2':
        search_prod_value(input("Type product name: "))
    elif answer == '3':
        add_product()
    elif answer == '4':
        remove_product(input("Insert product name to remove of the stock: "))
    elif answer == '5':
        sales(input('type a product to be sold: '))
    elif answer == '6':
        sales_today()
    elif answer == '7':
        exit_function()


def sales_today():  # function to see the sales today
    global sold

    for prod in sold:  # precisa aplicar para a cada dia ele zerar esta conta !!!!!
        if len(sold) == 1:
            pdf2(f"You have been sold {prod['value']} reais today")
            return sold
        else:
            value_sold = prod['value'] + prod['value']
            pdf2(f"You have been sold {value_sold} reais today")
            return value_sold


def sales(product_to_sales):  # Function to sale a product
    global stock, sold

    for prod in stock:

        if prod['product'] == product_to_sales:

            amount = float
            try:
                amount = float(input("Quantity of product sold: "))
            except ValueError:
                print("Type only Numbers")
                sales(input("Type a product name: "))

            if prod["amount_in_stock"] <= 0:
                print("Amount in stock is 0")
                sales(input("type a product in stock: "))

            if prod["amount_in_stock"] - amount >= 0:
                prod["amount_in_stock"] = prod["amount_in_stock"] - amount
                sold_today = {'product': prod["product"], 'value': prod["value"] * amount}
                sold.append(sold_today)
                print(sold)
                sales_again()
                run()
                return stock

            else:
                print(f"The amount in stock is {prod['amount_in_stock']}")
                sales(input("Type a product name: "))

    doesnt_exist()
    sales(input("Type a product name: "))
    

def remove_product(remove_prod):  # function to remove products to stock
    global stock

    for prod in stock:
        if prod['product'] == remove_prod:
            stock.remove(prod)
            print(stock)
            remove_product_again()
            run()


def add_product():  # function to add products to stock

    global stock

    product = {}

    product["product"] = input("Product Name: ")
    product["value"] = read_value()
    product["amount_in_stock"] = read_amount_in_stock()
    stock.append(product)
    again_add()
    run()


def read_value():  # ensure the float type
    try:
        value = float(input('Product Value: '))
        return value
    except ValueError:
        print("Just Type Numbers")
        read_value()


def read_amount_in_stock():  # ensure the float type
    try:
        amount = float(input('Quantity of products in stock: '))
        return amount
    except ValueError:
        print("Just Type Numbers")


def read_amount_to_sale():  # ensure the float type
    try:
        amount = float(input('Quantity of product sold: '))
        return amount
    except ValueError:
        print("Just Type Numbers")
        read_amount_to_sale()


def search_prod_value(search_product):  # function to search product values in stock

    global stock

    for prod in stock:
        if prod["product"] == search_product:
            print(f"the {prod['product']} costs {prod['value']} reais")
        else:
            doesnt_exist()

    again_search_prod_value()
    run()


def consult_stock():  # function to consult stock

    global stock

    if not stock:
        print("Stock empty")
        run()

    for item in stock:
        print(f"Your stock have items '{item['product']}' ")

    print('\n')

    product = input("Type product name: ")

    for prod in stock:

        if prod['product'] == product:
            print(f"the {prod['product']} has {prod['amount_in_stock']} in Stock")
            again_consult_in_stock()
            run()
            return

    doesnt_exist()
    again_consult_in_stock()


def doesnt_exist():  # function to show up when the value doesnt exist
    print("Value doesn't exist")
    return


"""
functions again, are to ask the user if he wants to do the process again YES OR NO
"""


def again_add():  # condition to add product again
    yes = 'yes'
    res = input("do you want to add a new product?: ")
    if res == yes:
        add_product()
    else:
        return "BYE"


def again_consult_in_stock():  # condition to search in stock again
    yes = 'yes'
    res = input("do you want consulting another product?: ")
    if res == yes:
        consult_stock()

    return "BYE"


def again_search_prod_value():  # condition to search product values again
    yes = 'yes'
    res = input("do you wanna search again?: ")
    if res == yes:
        search_prod_value(input("Type product name: "))
    return


def remove_product_again():  # condition to remove another product of the stock
    yes = 'yes'
    res = input("do you wanna remove another product?: ")
    if res == yes:
        remove_product(input("Insert product name to remove of the stock: "))
    return


def sales_again():  # condition to sales another product again
    yes = 'yes'
    res = input("do you wanna to sale another product?: ")
    if res == yes:
        sales(input("Type product name: "))
    return


def pdf2(solds):  # funciton to generate pdf of the sales

    pdf = pydf.generate_pdf(solds)

    with open('sales.pdf', 'wb') as f:
        f.write(pdf)


def exit_function(): # function to exit the software
    return

run()

