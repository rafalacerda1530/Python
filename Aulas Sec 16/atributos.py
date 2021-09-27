"""
ATributos - > são as caracteristicas do objeto

são 3 grupos de atributos:
     - Atributos de Instâncias -> são datributos declarados dentro do construtor
     - Atributos de Classe -> é um metodo especial para a construção do objeto
     - Atribubtos Dinamicos


chamamos de método tudo que esta dentro de uma classe

"SELF" = é basicamente o proprio objeto, no caso abaixo o self representa a lampada

em Python, todo atributo é publico (pode ser utilizado em todo o sistema),
para que ele seja privado (somente acessivel na classe que foi declarado), deve-se utilizar __ no nome

PAra acessar atributo fora da classe instancia_CLasse__atributo

o Atributo privado é importante para não ter alterações nos atributos fora da classe

print(conta1.__dict__)  # para verificar os atributos
"""


class Lampada:
    # "SELF" = é basicamente o proprio objeto, no caso abaixo o self representa a lampada

    def __init__(self, voltagem, cor):  # O Self pode ser alterado para o nome que desejar
        self.voltagem = voltagem  # aqui ele esta falando o objet self(lampada) no atributo nome vai receber
        self.cor = cor           # a variavel nome
        self.ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto1:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

# Atributos publicos ou privados

# Atributo privado, só ppode ser acessado dentro da própria classe


class Acesso:
    def __init__(self, email, senha):
        self.__email = email  # o __ informa que o atributo é privado
        self.__senha = senha


user = Acesso('rafa', 123)

print(user._Acesso__email) # Forma de acesso ao atributo privado (name MAngling)


# ATRIBUTOS DE CLASSE - ATributos declarados diretamente na classe

# p1 = Produto('PLaystation 4', "video game", 2300)
# p2 = Produto("Xbox s", "video game", 4500)

# refatorando a classe produto


class Produto:

    imposto = 1.05  # 0.05% de imposto
    contador = 0  # estes são atributos da classe

    def __init__(self, nome, descricao, valor):  # esses são atributos de instancia pois estão em um namespace
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id # para acessar o atributo de classe, utilizamos atributodeclase.nome do atributo inst


p1 = Produto('play 4', 'game', 2300)
p2 = Produto('xbox', 'game', 4000)

print(p1.valor)  # acesso incorreto a um atributo de classe

print(Produto.imposto)  # acesso correto

print(p1.id)  # acesso ao atributo de instancia
print(p2.id)

# Atributos dinâmicos

# Ele cria o atributo no tempo de execução.

p1.peso = '5KG'

print(p1.peso, p1.nome)

# DEletando atributos dinamicamente

print(p1.__dict__)   # mostra todos os atributos

del p1.peso

print(p1.__dict__)