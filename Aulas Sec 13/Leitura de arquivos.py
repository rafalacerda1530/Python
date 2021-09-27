"""
Leitura de arquivos

para ler um arquivo utilizamos a função open()

open() informamos o parametro de entrada e retorna _io.TextIOWrapper,

a função abre um arquivo para leitura, caso ele não exista teremos o erro FileNotFoundError

encoding = utf8 = significa que suporta caracteres especiais

para ler o conteudo de um arquivo após sua abertura utilizamos a função read() ex: arquivo.read
"""

arquivo = open('texto.txt')

print(arquivo)

print(type(arquivo))

# para ler o conteudo de um arquivo após sua abertura utilizamos a função read()

print(arquivo.read())

print(arquivo.read())  # ele utiliza a ideologia de cursor, após executar a primeira vez ele fica com o cursor no final
