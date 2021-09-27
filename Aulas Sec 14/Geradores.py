"""
Geradores

Generators são iterators, o contrário é falaso, nem todo iterator é um generator

generetaors podem ser criados com funções geradoras
funções geradoras utilizam a palavra reservada Yield
generators podem ser criados com expressões geradoras

Diferenças entre funções e generators function


-----------------------------------------------------------------------
|funções                               |generator functions           |
-----------------------------------------------------------------------
|Utilizam return                       | utiliza Yield                |
-----------------------------------------------------------------------
|retorna uma vez                       |podem utilizar diversas vezes |
-----------------------------------------------------------------------
|retorna um valor                      |retorna um generator          |
-----------------------------------------------------------------------

"""


# Generator function

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador  # yield para o sistema aqui e aguarda o next para dar continuidade
        # la embaixo ao aplicar o next no print ele da continuidade
        contador = contador + 1


# generator function gera um generator


gen = conta_ate(5)

print(next(gen))  # com o next ele vai pegar o valor  1
print(next(gen))  # com o next ele vai pegar o valor  2
print(next(gen))  # com o next ele vai pegar o valor  3
print(next(gen))
print(next(gen))

print("\nNumeração do FOR:\n")

for n in conta_ate(5):
    print(n)

