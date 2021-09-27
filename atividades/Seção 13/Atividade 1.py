"""
Programa que :
A) crie/abra um arquivo texto
b) o usuario grave caracteres ate que ele digite 0
c) feche o arquivo

agora abra e leia o arquivo todo e print os caractere
"""

with open('arq.txt', 'w') as arquivo:
    while True:
        text = input("Digite o texto: ")
        if text != "0":
            arquivo.write(text)
            arquivo.write('\n')
        else:
            print("finalizado")
            break

arqv = open('arq.txt')

print(arqv.read())

arqv.close()