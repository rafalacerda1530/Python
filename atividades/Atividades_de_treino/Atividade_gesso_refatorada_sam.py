"""
Um programa que registre usuário e senha e valide usuário e senha, que calcule o preço
do gesso com os metros das paredes, que calcule a TAbica,
e de o orcamento em cima da mão de obra
"""

'''
  Define your variables first!
'''
regusr = None
usr = None
regsen = None
gesso = None
altura = None
largura = None

'''
  Functions should be small, few lines!
  It's not a rule, but try to use only four lines for each function!
  if you need more lines than four line, considere to make other function!
'''

'''
  1. You should starting with more abstract and generic methods!
  For example, a method who read only intergers and return the
  value.
'''


def readIntValue(message):
    intValue = int(input(message))
    return intValue


'''
  2. A function to read any text input.
'''


def readTextValue(message):
    text = input(message)
    return text


'''
  2.1 A function to read only float numbers.
'''


def readFloatValue(message):
    floatValue = float(input(message))
    return floatValue


'''
  3. A function to read a valid password.

  Avoid "while True" it's a bad code style!
  Use should use recursive functions!
'''


def readNumericPassword():
    try:
        password = readIntValue('Senha numérica: ')
        return password
    except ValueError:
        print('A senha deve ser numérica')
        readNumericPassword()


'''
  4. A function to validate the username.
'''


def checkUsername():
    global regusr
    usr = readTextValue('Nome do usuário: ')
    if regusr == usr:
        return
    else:
        print('Usuário inválido')
        checkUsername()


'''
  5. A function to validate the password.
'''


def checkPassword():
    global regsen
    pwd = readNumericPassword()
    if pwd == regsen:
        return
    else:
        print('Senha incorreta')
        checkPassword()


'''
  6. A function to say 'welcome'.
'''


def sayWelcome():
    print(f"Bem vindo {regusr}")


def readGesso():
    try:
        gesso = readFloatValue("Preço gesso [R$]: ")
        return gesso
    except:
        print('Preço inválido')
        readGesso()


'''
  7. A function to read the wall width.
'''


def readWidth():
    try:
        width = readFloatValue("Largura da parede [m]: ")
        return width
    except:
        print('Largura inválida')
        readWidth()


'''
  8. A function to read the wall height.
'''


def readHeight():
    try:
        height = readFloatValue("Altura da parede [m]: ")
        return height
    except:
        print('Altura inválida')
        readHeight()


'''
  6. A function to read the 'tabica'.
'''


def readTabica():
    try:
        tabica = readFloatValue("Preço tabica [R$]: ")
        return tabica
    except:
        print('Preço inválido')
        readTabica()


'''
  6. A function to read the price of manpower.
'''


def readManPower():
    try:
        manpower = readFloatValue("Preço mão-de-obra [R$]: ")
        return manpower
    except:
        print('Preço inválido')
        readManPower()


def calculateGesso(largura, altura, gesso):
    calcgesso = largura * altura * gesso
    print(f'Gasto de gesso R$: {round(calcgesso, 2)}')
    return calcgesso


def calculateTabica(largura, altura, prectab):
    calctab = (largura * altura) * prectab
    print(f'Gasto: R$ {round(calctab, 2)} com tabica')
    return calctab


def calculateGain(maodeobra, calcgesso, calctab):
    lucro = maodeobra - calcgesso - calctab
    gastototal = calcgesso + calctab
    print(f'Gasto com Tabicas e Gesso: R$ {round(gastototal, 2)}')
    print(f'Lucro:  R$ {round(lucro, 2)}')


def generateOrder():
    global regsen
    global regusr

    regusr = readTextValue("Usuário para cadastro: ")
    regsen = readNumericPassword()

    checkUsername()
    checkPassword()
    sayWelcome()

    gesso = readGesso()
    largura = readWidth()
    altura = readHeight()

    calcgesso = calculateGesso(largura, altura, gesso)
    prectab = readTabica()
    calctab = calculateTabica(largura, altura, prectab)
    maodeobra = readManPower()
    calculateGain(maodeobra, calcgesso, calctab)


def runOrder():
    YES = 'sim'
    NO = 'não'
    generateOrder()
    res = readTextValue('Novo orçamento [sim/não]? ')
    if res == YES:
        runOrder()
    elif res == NO:
        print('Obrigado,orçamento finalizado!')
    else:
        print('Opção Invalida!')


if __name__ == '__main__':
    runOrder()

