"""
Seek e Cursors

seek() -> utilizada para movimentar o cursor pelo arquivo
# indica onde queremos colocar o cursor

OBS: quando abrimos um arq2uivo, cria-se uma conexão com o disco da maquina(streaming), após isso devemos fechar com
close()
"""

"""
arquivo = open('texto.txt')

print(arquivo.read())

# movimentando o cursor om a função seek

arquivo.seek(0)  # indica que vai colocar o cursor na posição 0 (começo)
# podemos inidicar qualquer posição

print(arquivo.read())
"""

"""
arquivo = open('texto.txt')

# para ler o arquivo linha a linha

print(arquivo.readline())  # para ler as proximas linhas devo acrescentar mais prints de readline
"""

"""
# adicionar o texto em uma lista

arquivo = open('texto.txt')

print(arquivo.readlines())  # acrescenta o texto em listas, cada linha vira um item

arquivo.seek(0)

print(len(arquivo.readlines()))
"""

"""
# fechando o arquivo

# 1 - abrir o arquivo
arquivo = open('texto.txt')

# 2 trabalhar com o arquivo
print(arquivo.read())

print(arquivo.closed)  # verifica se o arquivo esta aberto ou fechado (aberto = FALSE, fechado = TRUE)

# 3 fechando o arquivo
arquivo.close()
# é necessário fechaar pois os sistemas operacionais criam um lock (não permitem duas edições ao mesmo tempo)

print(arquivo.closed)

print(arquivo.read())  # erro pois o arquivo esta fechado
"""