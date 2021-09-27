"""
AND, OR, NOT, IS

OPERADOR BINÁRIO : AND, OR, is
OPERADORES UNÁRIOS : AND OR
"""

ativo = False
logado = True

if ativo and logado:  # para o AND precisa os dois serem TRUE
    print('Bem vindo user')
else:
    print('ativar a conta')

ativo2 = True
logado2 = False

if ativo2 or logado2:  # Um dos dois precisa ser True
    print('User no sistema')

ativo3 = False
logado3 = True

if not ativo3:  # para o NOT o valor invertido se esta TRUE vira FALSE
    print('Precisa ativar conta')
elif not logado3:  # se não esta loga ele vai printar a mensagem abaixo
    print('precisa logar')
else:
    print("Welcome")

ativo4 = True
logado4 = True

if ativo4:  # se logado é True ele printa abaixo
    print('conta ativa')
else:  # se não printa abaixo
    print('ativar conta')

print(ativo4 is False)  # ativo é falso?? resultado é False pois o ativo
# esta True
