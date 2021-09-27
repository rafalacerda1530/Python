"""
Listas,
- FUncionam como vetores ou matrizes (Arrays)
- São dinâmicos e pode colocar qualquer dado
- Em outras linguagens o tipo do Array não pode ser alterado
- Python não tem tamanho fixo
- as listas podem ser adicionadas elementos
- as listas são representadas por colchetes []
- posso colocar qualquer tipo de dados dentro de uma lista
[1,2,3, True, 'rafa', 4.50]

lis6 = lis1.copy() para copiar a lista 1 # sem sentido
print(lis6)


"""

lis1 = [1, 82, 55, 5, 6, 50, 35, 89]

lis2 = ['r, a, f, a, e, l']

lis3 = []

lis4 = list(range(11))  # vai listar numeros do 0 a 10 (range) porém mantendo
# umas lista ex: [0, 1, 2, 3,...]

lis5 = list('rafael')  # é gerado uma lista igual a lis2

"""
#  - podemos checar se um valor esta na lista 

num = int(input("digite o valor: "))

if num in lis4:
    print(f'tem o {num}')
else:
    print(f'não tem o {num}')
"""

#  --------------------------------------------------------

"""
#  - podemos checar se qualuer valor esta na lista    

letra = input("digite a letra: ")

if letra in lis5:
    print(f'tem a letra {letra}')
else:
    print(f'não possui a letra {letra}')
"""

#  -----------------------------------------------------------

"""
#  Ordenando uma lista:

print(lis1)
lis1.sort()  # vai ordenar a lista em ordem crescente
print(lis1)

print('\n')

print(lis5)
lis5.sort()  # vai ordenar a lista em ordem crescente         
print(lis5)
"""

#  -----------------------------------------------------

"""
# podemos contar o número de ocorrências de um valor na lista

print(lis1.count(1))  # quero contar na variavel lis1
# quantos numeros 1 tem

print(lis5.count('r'))  # quero contar na variavel lis1
# quantos letras r tem
"""

# ----------------------------------------------------------
"""
# adicionar elementos em listas, somente um elemento ou
# uma lista dentro de outra (sublist)

"para adicionar elementos nalista utilizamos o append"

print(lis1)
lis1.append(15)  # esta "apendando" adicionando o 15 na lista
# porém ele apenda somente um elemento por vez
print(lis1)

print("\n")

print(lis1)
lis1.append([140, 150, 160])  # ele cria uma lista dentro de
# outra para numeros
print(lis1)

# ex com string:

print(lis5)
lis5.append(list('lacerda'))  # cria uma lista dentro de outra
# para string
print(lis5)

if [140, 150, 160] in lis1:
    print('tem')
else:
    print('não tem')
"""

# -----------------------------------------------

"""
# adicionando elementos a lista
# neste caso ele realmente adiciona o valor na lista
# neste caso utiliza-se o .extend
# o extend aceita somente varios valores, para valores unicos
# utiliza-se o append
# os valores vão sempre para o final da lista

print(lis1)
lis1.extend([1, 50, 45])  # esta adicionando este valor na lista
print(lis1)

print(lis5)
lis5.extend(list('lacerda'))  # esta adicionando a letra na lista
print(lis5)

"""

# --------------------------------------------------

"""
# podemos inserir um novo elemento informando a posição
# do indice na lista
# utiliza-se o insert
# ele não subistui o valor que esta no indice,
# ele só joga ele pra direita

print(lis1)
lis1.insert(2, 'novo valor')  # na posição 2 ele vai inserir
print(lis1)                   # o "novo valor"
"""

# ---------------------------------------------------------

"""
# para juntar listas
# lista 6 = lista1 + lista2 # pode ser feitos assim,
# porém é necessário uma váriavel
# podemos utilizar o extend
# lis1 = lis1 + lis2 pode-swe utilizar assim tbm

lis1.extend(lis2)
print(lis1) # estou juntando a lista 1 com a 2,
# a lista 1 esta sendo alterda por isso devemos printa-la
"""

# ----------------------------------------------------------

"""
# Imprimir a lista inversa utilizando o reverse

print(lis1)
lis1.reverse()
print(lis1)

# outra forma de inverter
print(lis1[::-1])  # ::= começando da posição zero
# -1 = inverter ou seja começar do final
"""

# --------------------------------------------------------

"""
# para contar as posições de uma lista
print(lis1)
print(len(lis1))
"""

# ------------------------------------------------------------

"""
# remover o ultimo elemento da lista com o .pop
# quando o pop é utilizado no terminal ele mostra o numero que foi removido

#print(lis5)
#lis5.pop()
#print(lis5)

# podemos remover um elemento pelo indice com o pop

print(lis5)
lis5.pop(2)  # ele esta removendo o caracter no indice 2
print(lis5)  # e os elementos são juntado, n fica buraco
"""

# -------------------------------------------------------

"""
# Limpar a lista utiliza o .clear
print(lis5)
lis5.clear()
print(lis5)
"""

# ----------------------------------------------------

"""
# repetir os elementos na lista
print(lis1)
lis1 = lis1 * 3  # ele vai repetir os elementos da lista 3 vezes
print(lis1)
"""

# -------------------------------------------------------

"""
# transformando string em listas
string = "rafael lacerda"
print(string)
string = string.split()  # separa as strings pelos espaços
print(string)            # tranformando em lista

string2 = "rafael,lacerda"
print(string2)
string2 = string2.split(",")  # ele vai separar a lista normalmente
print(string2)                # pois estou informando que o separador
# é a virgula
"""

# ------------------------------------------------------------

"""
# Transformando LISTAS em STRINGD
string2 = ['rafael', 'lacerda', 'rodrigues']
string2 = ' '.join(string2)  # ele vai pegar a lista e
print(string2)  # trsnformar em string e colocar um espaço
# entre cada elemento

print('\n')

print(lis5)
lis5 = ' '.join(lis5)   # ele vai pegar a lista e
# trsnformar em string e colocar um espaço
# entre cada elemento
print(lis5)

print('\n')

print(lis2)
lis2 = ' '.join(lis2)  # ele vai pegar a lista e
# trsnformar em string e colocar um espaço
# entre cada elemento
print(lis2.replace(',', ''))
# para a Lis2, estou tirando
#  a virgula e sobrepondo com um espaço no caso ele vai
# juntar as letras

curso = ['rafael', 'rodrigues', 'lacerda']
curso2 = '$'.join(curso)
print(curso2)  # vai virar uma str e nos espaços
# serão colocados os $
"""

# ---------------------------------------------------

"""
# Iterando sobre listas utilizando FOR

soma = 0

for elemento in lis1:  # ele vai mostrar os dados(elementos) da lista
    print(elemento)

for elemento in lis1:
    soma = soma + elemento
    print(soma)  # o elemento vai assumir o valor da posição 0
# e somar com a posição 1, ai o elemento assume esse valor e
# soma com a posição 2, ai o elemento assume esse valor e
# soma com a posição 3, assim sucessivamente.
"""

# -----------------------------------------------------------

"""
# Iterando sobre listas utilizando WHILE
carrinho = []
produto = ''

while produto != 'sair':
    print('adicione um produto na lista ou digite sair para sair')
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

#  enquanto produto for diferente de sair, didgite o produto
# ele vaiadicionar na variavel produto, se o produto for
# igual sair, ele vai apendar(juntar) a variavel produto
# na variavel carrinho que é uma lista vazia
# vai finalizar o loop e printar abaixo:

for produto in carrinho:
    print(produto)

# para cada valor do produto dentro do carrinho:
# print a posição zero depois ele repete o processo
# ou seja na proxima vez ele printa a proxima posição
"""

# -----------------------------------------------------

"""
# fazemos acesso aos elementos de forma indexidada

cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])  # ele vai imprimir na posição 0 (verde)

# fazemos acesso aos elementos de forma indexidada inversa

cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[-1])  # ele vai puxar o valor de tras pra frente
#  de tras pra ferente a posição começa no -1
"""

# -----------------------------------------------------

"""

# mais utilização de for e while
cores = ['verde', 'amarelo', 'azul', 'branco']

for cor in cores:
    print(cor)

indice = 0

while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

# Enquanto indice for menor do que as posições(len) na varivel
# cores, print as cores nas posições equivalentes ao indice,
# e vou somar mais uma posição na variavel indie:
# ex: no primeiro loop a posição é zero, ou seja:
# indice é menor que a posição totaç da varivel cores? não,
# print cores na posição do valor da variavel indice
# e adicione mais um valor para o indice,
# agora o indice vale 1 e repete a estrutura
"""

# ----------------------------------------------------


"""
# gerar indice em um for
cores = ['verde', 'amarelo', 'azul', 'branco']

for indice, cor in enumerate(cores):  # enumerate mostra a posição
    print(indice, cor)                # e o que tem nela

# para o indice(posição) de cor no enumerate da variavel cores
# print o indice e a cor
# ou seja vai mostrar a posição junto com a cor

cores = list(enumerate(cores))
print(cores)  # vou colocar a variavel cores em uma lista,
# e fazer o enumerate (posição e valor) da variavel cores
# ou seja, na lista ela me mostra qual a posição e o que tem nela
"""

# ----------------------------------------------------


""""
# encontrar o indice de um elemento na lista
numeros = [1, 2, 5, 8, 110]
print(numeros.index(5))  # qual o indice esta o numero 5?
#  caso tenha varios valores repetidos, ele tras sempre o primeiro
"""

# -----------------------------------------------------

"""
# podemos buscar um indice em um range
numeros = [5, 2, 5, 8, 110, 5]
print(numeros.index(5, 1, 5))

# ele vai procurar o valor 5 nos indices do 1 ao 5
"""

# -----------------------------------------------------

"""
# Revisando Slicing [inicio: fim: passo]
# slicing de lsitas

lista = [1, 2, 3, 4]
print(lista[1:])  # começa do indice 1 e vai até o fim
# se não colocar o ":" ele vai retornar o que esta na posição 1

print(lista[1:3])  # começa do 1 e vai até o indice 3

print(lista[1::2])  # começa no indice 1, vai até o final de 
# em 2

print(lista[::2])  # começa no zero até o fim de 2 em 2
"""

# ------------------------------------------------------

"""
# Invertendo valores em uma lista
nomes = ['rafael', 'lacerda']
nomes.reverse()
print(nomes)

print(nomes[::-1])
"""

# ----------------------------------------------------------

"""
# Soma, Valor maximo, Valor minimo, tamanho
valor = [1, 2, 3, 4, 5, 6]

print(sum(valor))  # Soma
print(max(valor))  # Maximo valor
print((min(valor)))  # Minimo valor
print(len(valor))  # Tamanho da lista
"""

# --------------------------------------------

"""
# Transformar lista em Tupla
valor = [1, 2, 3, 4, 5, 6]
valor2 = tuple(valor)
print(type(valor2))
# a variavel valor vira uma tupla
"""

# -------------------------------------------------

"""
# desempacotamento de listas
valor = [1, 2, 3]
num1, num2, num3 = valor
print(num1, num2, num3)
# as variaveis devem ter a mesma quantidade de elementos
"""

# -----------------------------------------------------

"""
# Copiando uma lista para outra (Shallow e Deep Copy)

lista = [1, 2, 3]
print(lista)

nova = lista.copy()  # ele ta fazendo uma cópia da var lista
# e adicionando na VAr nova
print(nova)

nova.append(4)  # ta adicionando o valor 4 na var nova
print(lista)
print(nova)
#  elas são listas diferentes  (Deep copy)

#  SHALLOW COPY
lista = [1, 2, 3]
print(lista)

nova = lista
print(nova)

nova.append(4)
print(lista)
print(nova)
# se uma das duas listas for alterada, reflete na outra
"""
"""
musicas = [
    {"TItulo": "Forro Boys", "Tocou": 17},
    {"TItulo": "Djonga", "Tocou": 9000},
    {"TItulo": "iron", "Tocou": 950},
    {"TItulo": "XAND", "Tocou": 850}
]

print(max(musicas, key=lambda musica: musica['Tocou'])['TItulo'])  # desse objeto informe somente a chave titulo
print(min(musicas, key=lambda musica: musica['Tocou'])['TItulo'])  # printe em musicas e armazene na variavel
# musica as que possuem o menor valor e apresente somente o titulo

# OBS: o KEY é a forma que ele vai buscar esses resultados,
"""

lista = 'Rafael'

print(lista[0][0])  # trás somente a letra R