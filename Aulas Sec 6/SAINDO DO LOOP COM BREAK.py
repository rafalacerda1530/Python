"""
SAINDO DE LOOP COM BREAK
PARA SAI DE LOOP DE MANEIRA PROJETADA/FORÇADA
"""
for numero in range(1, 11):
    if numero == 6:
        break  # vai sair do loop se o numero 6 aparecer
    else:
        print(numero)
print('sai logo')

print('\n')

while True:
    comando = input("digite 'sair' para sair: ")
    if comando == 'sair':
        break
