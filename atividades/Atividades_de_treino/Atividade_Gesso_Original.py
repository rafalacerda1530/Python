"""
Um programa que registre usuário e senha e valide usuário e senha, que calcule o preço
do gesso com os metros das paredes, que calcule a TAbica,
e de o orcamento em cima da mão de obra
"""
regusr = input("Digite o usuário para cadastro: ")

while True:
    try:
        regsen = int(input('digite uma senha apenas com numeros: '))
        break
    except ValueError:
        print('A senha permite apenas numeros: ')


usr = input('Entre com o usuário: ')


while usr != regusr:
    print("Usuário invalido")
    usr = input('Digite usuário correto: ')

sen = 0

while sen != regsen:
    try:
        sen = int(input(' digite a senha registrada: '))
    except ValueError:
        print('Senha Aceita somente numeros')


if usr == regusr and sen == regsen:
    print(f"Bem vindo {usr}")

#  Até aqui foi a autenticação do usuário,
# APós faremos os calculos


def orcamento():
    while True:
        try:
            gesso = float(input('digite o valor do gesso: '))
            break
        except ValueError:
            print('digite um valor valido para o Gesso: ')

    while True:
        try:
            par1 = float(input('o tamanho da parede 1: '))
            par2 = float(input('o tamanho da parede 2: '))
            break
        except ValueError:
            print('digite um valor valido para as paredes')

    calcgesso = (par1 * par2) * gesso
    print(f'Você vai gastar de gesso {calcgesso} reais')

    while True:
        try:
            prectab = float(input(' digite o valor da Tabica: '))
            break
        except ValueError:
            print('Digite um valor Valido')

    calctab = (par1 * par2) * prectab
    print(f'você vai gastar {calctab} reais com a tabica')

    while True:
        try:
            maodeobra = float(input('Digite o valor da mão de obra para calcularmos o Lucro: '))
            break
        except ValueError:
            print('Digite um valor valido para a sua Mão de obra')

    lucro = maodeobra - calcgesso - calctab
    gastototal = calcgesso + calctab

    print(f'Você vai gastar com as Tabicas e gessos {gastototal} Reais')
    print(f'Você vai receber de lucro {lucro}')
    return


orcamento()

res = input('deseja fazer outro orcamento? ')

if res == 'não':
    print('obrigado')

while res == 'sim':
    orcamento()
