"""
Escrevendo em arquivos

Obs: ao abrir para leitura não podemos realizar a escrita nele

ao utilizar o with open('texto.txt', 'w'), em um arquivo que ja existe, ele sera apagado e outro criado
ou seja o arquivo anterior é perdido (utilizando o modo w)

"""

"""
with open('texto.txt', 'w') as arquivo:  # mode de arbetura w = write (apaga o anterior)
    arquivo.write('força\n')
    arquivo.write('a luta é assim mesmo\n')
    arquivo.write('vai dar certo\n')

with open('texto.txt') as arquivo2:
    arquivo2.seek(0)
    print(arquivo2.read())
"""

"""
with open('rafael.txt', 'w') as arquivo:
    arquivo.write('rafael\n' * 1000)
"""

with open('frutas.txt', 'w') as arquivo:
    while True:
        fruta = input("Digite a fruta se não digite sair: ")
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break

