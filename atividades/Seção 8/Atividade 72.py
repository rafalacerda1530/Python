"""
Foi realizada uma pesquisa da caracteristica de 5 pessoas,

retorne:

a) uma função que leia estes dados em um vetor
b) uma função que determine a média de idade das pessoas com olhos castanhos e cabelos pretos
c) a maior idade entre os habitantes
d) a quantidade de mulheres cuja a idade esta entre 18 e 35 e que tenham olhos azuis e cabelos loiros
"""

add = []


def caracteristicas():
    global add
    while True:

        if len(add) <= 4:
            caract = {'idade': int(input("digite a idade: ")), 'cabelo': input("digite a cor do cabelo: "),
                      'olhos': input("digite a cor dos olhos: "), 'sexo': input("digite o sexo 'f' ou 'm': ")}

            add.append(caract)

        else:
            return


def cond_run():
    global add
    if len(add) != 5:
        caracteristicas()
    elif len(add) > 5:
        print("lotado")


def castanho_preto():
    global add, media
    idades = []
    for cast in add:
        if cast['olhos'] == 'castanho' and cast['cabelo'] == 'preto':
            idades.append(cast['idade'])
            media = sum(idades) / len(idades)

    print(f'a média da idade de pessoas com cabelo preto e olhos castanhos é: {media}')


def maior_idade():
    global add, idade
    idade = []

    for idades in add:
        idade.append(idades['idade'])
    print(f'a maior idade entre os moradores é: {max(idade)}')


def idade_mulher():
    global add
    cond = []
    for cast in add:
        if 18 <= cast['idade'] <= 35:
            if cast['cabelo'] == 'loiro' and cast['olhos'] == 'azul' and cast['sexo'] == 'f':
                cond.append(cast['sexo'])
    print(f'a quantidade de mulheres cuja a idade esta entre 18 e 35 e que tenham olhos '
          f'azuis e cabelos loiros é : {len(cond)}')


def run():
    cond_run()

    castanho_preto()

    maior_idade()

    idade_mulher()


run()
