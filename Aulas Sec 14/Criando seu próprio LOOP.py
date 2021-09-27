"""
Criando LOOP
"""


def meu_for(interavel):
    it = iter(interavel)
    while True:
        try:
            print(next(it))  # ele vai printar cada elemento do iteravel
        except StopIteration:  # ele vai tratar o erro quando o next passar da quantiade de dados do ietravel
            break


meu_for('RAFAEL LACERDA')
