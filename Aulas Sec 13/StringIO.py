"""
StringIO = utilizado para ler e criar arquivos em memória

Obs: para ler e escrever em arquivos o sistema deve ter permissões

o STringIo serve para alocar arquivos de string em memória, onde podemos ler futuramente
"""

from io import StringIO

mensagem = 'Esta é apenas uma string nomral'

# podemos criar um arquivo em memória ja com uma string inserida ou mesmo vazia para escrever depois

arquivo = StringIO(mensagem)

print(arquivo.read())


arquivo.seek(3)

print(arquivo.read())