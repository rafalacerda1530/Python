"""
Any e All

All - retorna True, se o iteravel for verdadeiro ou estiver vazio

Any - retorna True se qualquer elemento for verdadeiro, se o iterabel tiver vazio, retorna false
"""

"""
# ex all:

print(all([0, 1, 2, 3, 4]))  # o retorno é False pois o zero é false e All - retorna True, se o iteravel
# for verdadeiro ou estiver vazio

print(all([ 1, 2, 3, 4])) # o retorno é True pois todos os valores são True

nomes = ['rafa', 'ricardo', 'riana']

print(all([nome[0] == 'r' for nome in nomes]))  # o resultado é True pois todos os valores possuem o r

print(all([numero for numero in [1, 5, 6, 10, 8] if numero % 2 == 0]))  # retorna false se possuir um zero (valor false)
"""

# EX ANY

print(any([0, 1, 2, 3, 4]))  # ele possui elementos True, ent o result é True

print(any([]))  # False, pois a lista esta vazia

nomes = ['rafa', 'ricardo', 'riana']

print(any([nome[0] == 'r' for nome in nomes]))  # retorna True pois possui valores True