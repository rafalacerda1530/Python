"""
Generators

- após a utilização o resultado é apagado da memória
- o GEnerator é melhor para verificação de True e false pois ele apaga da memória e n ocupa espaço
-from sys importteste getsizeof
# retorna a quantidade de Bytes em memória
- generator é basicamente um comprehesion com tuplas
"""

"""
nomes = ['rafa', 'ricardo', 'riana']

print(any([nome[0] == 'r' for nome in nomes]))

# Generator
res = (nome[0] == 'r' for nome in nomes)
print(res)
"""

"""
from sys importteste getsizeof
# retorna a quantidade de Bytes em memória

print(getsizeof("RAFAEL" "LACERDAAAA"))
"""
"""
# verificando os bytes de memória
from sys importteste getsizeof

list_comp = getsizeof([x * 10 for x in range(1000)])

set_comp = getsizeof({x * 10 for x in range(1000)})

dict_comp = getsizeof({x: x * 10 for x in range(1000)})

generator = getsizeof(x * 10 for x in range(1000))

print(f"memória gastas: \nlist_comp: {list_comp}\n"
      f"set comp: {set_comp}\n"
      f"dict comp: {dict_comp}\n"
      f"Generator: {generator}\n"
      )
"""

# iterando no generator

from sys import getsizeof
gen = (x * 10 for x in range(1000))

for num in gen:
    print(num * 2500)
    print(getsizeof(num))
