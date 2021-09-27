"""
LOOP WHILE

WHILE = BOOLEANO PQ SIGNIFICA ENQUANTO
ENQUANTO FOR TRUE ESTA EM LOO QUANDO FOR FALSE ELE PULA
"""
numero = 1

while numero < 5:
    print(numero)
    numero = numero + 1
# enquanto numero menor que 10 print o numero e no final do codigo
# estou atribuindo mais um valor ao numero, após isso ele volta para
# o while poq o numero ainda não é igual nem maior que 10
# o crtitério de parada é while numero < 10

resposta = ''

while resposta != 'sim':
    resposta = input('ja acabou ?')
    if resposta == 'sim':
        break
    else:
        resposta = input('e agora?')
