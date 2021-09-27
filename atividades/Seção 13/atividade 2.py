"""
Receba um texto e mostre quantas letras são vogais
"""

with open('arq2.txt', 'w') as arquivo:
    text = input("digite seu texto: ")
    resul = 0
    for letra in text:
        if letra == 'a':
            resul = resul +1
        elif letra == 'e':
            resul = resul + 1
        elif letra == 'i':
            resul = resul + 1
        elif letra == 'o':
            resul = resul + 1
        elif letra == 'u':
            resul = resul + 1
    print(f'o texto possui {resul} vogais')
    arquivo.write(text)

    arquivo .close()


arquivo = open('arq2.txt')
arquivo.seek(0)
print(f'o arquivo possui o seguinte texto: {arquivo.read()}')