"""
Métodos

representam os comportamentos do objeto, as funções da classe

METODO __INIT__ È um metodo construtor e sua função é construir o objeto a partir da classe

Métodos de instancias - são os métodos dentro da classe


# Quando utilizar metdo de classe e instancia ?
# Métodos de instancia são quando precisam acessa atributos TEM ACESSO A INSTANCIA
# metodos de classe são quando não precisam de um atributo NÃO ACESSA A INSTANICA
# METODOS ESTATICOS, NÃO ACESSA NENHUM DOS DOIS

Métodos de classe são conhecidos como métodos estaticos em outras linguagens
"""

# METDOS DE INSTÂNCIA: SÃO METODOS DENTRO DO BLOCO DE DEFINIÇÃO DA CLASSE

from passlib.hash import pbkdf2_sha256 as cryp


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade


class Contacorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = Contacorrente.contador + 1  # para icrementar o contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__ligada = False
        Contacorrente.contador = self.contador  # para icrementar o contador + 1


class Produto:
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id + 1

    def desconto(self, porcentagem):
        return (self.__valor * (100 - porcentagem)) / 100


class Usuario:

    contador = 0

    @classmethod   # para criação de método de classe se utiliza os decorators, assim ele diferencia do metod de instancia
    def conta_user(cls):  # o cls é como a classe Usuário, como se fosse o self do usuário
        print(f'Temos {cls.contador} usuários no sistema')

    @staticmethod
    def definicao():  # UM METODO ESTATICO NÃO POSSUI ACESSO A CLASSE NEM A INSTACIA
        return 'UXR334'

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=20000, salt_size=16)
        self.__id = Usuario.contador + 1
        self.__sobrenome = sobrenome
        Usuario.contador = self.__id

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def check(self, senha):
        if cryp.verify(senha, self.__senha):  # verify é para verificação, ela vem da biblioteca passlib
            return True
        return False


"""
p1 = Produto('Playstation 4', 'Video game', 2300) 

print(p1.desconto(10))   
"""
"""
n1 = Usuario('Rafael', 'lacerda', 'lacerda@hotmail', '123456')

print(n1.nome_completo())

#  print(n1.nome)  # quando o atributo é privado, não conseguimos printar ele sem um método

"""

"""
nome = input("informe nome: ")
sobrenome = input("Informe sobrenome: ")
email = input("informe email: ")
senha = input("informe senha: ")
confirma_senha = input("confirme a senha: ")

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('senha não confere')
    exit(42)  # código para saida de erro

print('UUsário cadastrado')

senha = input("Digite a senha novamente: ")

if user.check(senha): # não precisa dar condição pois o if ja trás se for verdadeiro
    print('Acesso permitido')
else:
    print('acesso negado')

print(f'SEenha criptografada: {user._Usuario__senha}')  # acesso errado somente para validar a senha criptografada
"""


#  MÉTODOS DE CLASSE:  para criação de método de classe se utiliza os decorators


"""
user = Usuario('RAFAEL', 'LACERDA', 'RAFAEL@GMAIL', '12345')

Usuario.conta_user()  # maneira correta de acessar o metodo de classe
"""


# Quando utilizar metdo de classe e instancia ?
# Métodos de instancia são quando precisam acessa atributos TEM ACESSO A INSTANCIA
# metodos de classe são quando não precisam de um atributo NÃO ACESSA A INSTANICA
# METODOS ESTATICOS, NÃO ACESSA NENHUM DOS DOIS

