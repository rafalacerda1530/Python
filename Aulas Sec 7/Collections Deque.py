"""
Deque - é uma lista de alta performance
"""

# importando

from collections import deque

deque = deque('rafa')
print(deque)
# Cria uma lista

# adicionando elementos no deque

deque.append('y')  # adiciona no final
print(deque)

deque.appendleft('k')
print(deque)  # adiciona no começo da lista

# removendo elementos
print(deque.pop())  # remove e retorna o ultimo elemento
print(deque)

print(deque.popleft())  # remove e retorna o primeiro elemento
print(deque)

