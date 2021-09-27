"""
Modo de abertura de arquivos

r = abre para leitura

w = abre para escrita e sobrescreve caso o arquivo exista

X = Abre para escrita somente se o arquivo não existir
obs: caso exista o arquivo gera o erro File exists

A = abre para a escrita adicionando o conteudo ao final do aquivo (sempre ao final)
obs: se o arquivo não existir sera criado

+ = abre para o modo de atualização leitura e escrita
"""

"""
with open('rafael.txt', 'x') as arquivo:
    arquivo.write('TESTE DE CONTEUDO. \n')
"""

"""
# adiciona mais textos

with open('frutas.txt', 'a') as arquivo:
    while True:
        fruta = input("Digite a fruta se não digite sair: ")
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break
"""

with open('texto.txt', '+r') as arquivo:
    arquivo.seek(0)
    arquivo.write('nos topos \n')
    arquivo.write('mais uma linha \n')
