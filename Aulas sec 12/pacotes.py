"""
Pacotes - um diretório contendo uma coleção de módulos

para criarmos nossos pacotes, criamos um python package
"""

from pacotes_teste import teste1, teste2

from pacotes_teste.pacotes_teste_2 import teste3, teste4

# utiliza-se deste forma quando se tem sub pacote

print(teste1.pi)

print(teste1.func1(15, 12))

print(teste2.curso)

print(teste2.func2())

print(teste3.func3())

print(teste4.func4())


from pacotes_teste.teste1 import func1

#  para importar somente a função de um subpacote

print(func1(15, 3))
