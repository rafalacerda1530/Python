"""
armazene dois vetores recebidos do usuário com 10 numeros cada
crie um novo vetor c e faça a-b e mostre na tela o resultado
"""
# Input de valores inteiros dentro de uma lista
a = [int(input(f'dite o 1 valor para a: '))]
pri1 = 2

# enquanto o len(tamanho de elementos) for menor
# que 10, ele vai pegar a lista a e acresecentar
# o valor que eu digitar
# obs a = a + [int(input(f'dite o {pri1} valor para a: '))]
# acima eu estou adicionando a lista a com um valor inteiro
# de uma lista que vou digitar
while len(a) != 10:
    a = a + [int(input(f'dite o {pri1} valor para a: '))]
    pri1 = pri1 + 1

# Input de valores inteiros dentro de uma lista
b = [int(input('Digite o 2 valor para b: '))]
pri2 = 2

# enquanto o len(tamanho de elementos) for menor
# que 10, ele vai pegar a lista a e acresecentar
# o valor que eu digitar
# obs b = b + [int(input(f'dite o {pri2} valor para b: '))]
# acima eu estou adicionando a lista a com um valor inteiro
# de uma lista que vou digitar
while len(b) != 10:
    b = b + [int(input(f'dite o {pri2} valor para b: '))]
    pri2 += 1

# ordenação da lista menor > maior
a.sort()
b.sort()

# printando as listas
print(a)
print(b)

# somando os valor de a e o resultado estou subtraindo
# da soma dos valores de B
c = sum(a) - sum(b)
print(c)
