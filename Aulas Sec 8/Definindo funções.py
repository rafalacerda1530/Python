"""
Definindo funções

- São pequenos trechos de código que realizam tarefas especifícas
- Pode ou não receber entradas de dados e retornar uma saida
- Uteis paa executar processos similiares varias vezes
- Funções integradas são chamadas de Built-in
- Algumas funções são agregadas a um tipo de dado especifico,
outras ja podem ser utilizadas com quaisquer dados
- Forma geral de finição da função:
def nome da função(parametros de entrada):
    Bloco da função
- Nome da função = sempre letras minusculas, nomes compostos semopre separados
por "_"
- Parametros de entrada são opcionais, se tiver mais de um cada um separa
por virgula
- bloco da função = chamado tbm de corpo da funçã ou implementação, onde o processo
da função acontece
Obs: para definir uma função utilizamos uma palavra reservada "def"

Obs: escreva funções simples e objetivas
"""


# Definin função

def diz_oi():
    print('Oi')


# utilizando funções
# chamada de execução

diz_oi()  # precisa colocar o parenteses


# Exemplo 2

def cantar_parabens():
    print('Parabens para você')
    print('Nessa data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')


cantar_parabens()  # chamada de execução

#for n in range(5):
#   cantar_parabens()
# para valor de 0 a 4 execute a função cantar parabens


canta = cantar_parabens

canta()  # a var canta recebe a funçao do metodo
# cantar_parabens e a variavel canta utilizamos como
# função

