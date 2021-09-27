"""
teste de velocidade com expressões generators
"""

"""
def nums():
    for num in range(1, 10):
        yield num


ge1 = nums()

print(next(ge1))
print(next(ge1))


ge2 = (num for num in range(1, 10))  # expressão generator

print(next(ge2))
print(next(ge2))
"""

# teste de velocidade com time

import time

# generator expression

gen_inicio = time.time()  # vai dar o tempo de inicio a partir desta linha
print(sum(num for num in range(100000000)))
gen_tempo = time.time() - gen_inicio  # vai subtrair o tempo de inicio menos o final

# List comprehension

list_inicio = time.time()  # vai dar o tempo de inicio a partir desta linha
print(sum([num for num in range(100000000)]))
list_tempo = time.time() - list_inicio  # vai subtrair o tempo de inicio menos o final

print(gen_tempo)
print(list_tempo)