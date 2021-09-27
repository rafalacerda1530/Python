"""
Forçando tipos de dados com decoradores
"""


def forca_tipo(*tipos):
    def decorador(funcao):
        def converte(*args, **kwargs):
            novo_args = []
            for (valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))
            return funcao(*novo_args, **kwargs)
        return converte

    return decorador


@forca_tipo(str, int)
def repetir(msg, vezes):
    for vez in range(vezes):
        print(msg)


repetir('geek', '3')


@forca_tipo(float, float)
def dividir(a, b):
    print(a/b)


print(dividir('3', 4))
