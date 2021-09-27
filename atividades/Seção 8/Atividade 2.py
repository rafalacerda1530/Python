"""
Uma função que recebe a data atual (dia, mês, ano) e exiba na tela
em formato de texto
"""

meses = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março,', 4: 'Abril', 5: 'Maio',
         6: 'Junho', 7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro',
         11: 'Novembro', 12: 'Dezembro'}


def data(di, me, an):
    global meses
    if me in meses:
        return f'{di} de {meses.get(me)} de {an}'
        # Nessa chave estou pesquisando no dicionario meses  na parte de chave o que foi digitado em "me"


d = input('Digite o dia: ')
m = int(input('Digite o mês: '))
a = int(input('Digite o ano: '))

print(data(di=d, me=m, an=a))
