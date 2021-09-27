"""
Um programa que possua um vetor, que se chame A,
que armazene 6 numeros int, o programa deve fazer

A) atribuir os seguintes valores 1, 0, 5, -2, -5, 7
B) armazenar em uma variavel a soma destes numeros das
posições 0, 1, 5
C) modificar o vetor na posição 4, colcoar o valor 100
D) mostrar o valor do vetor a, um em cada linha
"""

A = [1, 0, 5, -2, -5, 7]

B = A[0] + A[1] + A[5]

print(f'A somas das posições 0, 1, 5, é: {B}')

print('\n')

print(f'Antes de excluir a posição 4 e adicionar o 100 era assim : {A}')

A.pop(4)  # esta excluindo a posição 4
A.insert(4, 100)  # na posição 4 esta inserindo o 100

print('\n')

print(f'Após, ficou assim : {A}')

for i in range(len(A)):  # O RANGE VAI COMEÇAR DA POSIÇÃO ZERO ATÉ O TAMANHO DA LISTA
    print(f' os caracteres que compõe o numero {A} são {A[i]}')

# o I começa assumindo a posição 0, após toda execução ele o loop e
# assume o valor na posição 1 e assim sucessivamente
