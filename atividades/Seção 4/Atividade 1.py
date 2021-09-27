"""
Tres amigos jogaram na loteria, faça um programa que leia os dados
do valor investido e que o premio seja dividido proporcuionalmente
a quantidade investida e de forma justa.

"""
print('Insira o valor valor do premio')

vlrpremio = float(input())

maiorvl = vlrpremio * 50 / 100
print('o vencedor 1 leva', maiorvl)

vlrmedio = vlrpremio * 30 / 100
print('o vencedor 2 leva', vlrmedio)

menvalor = vlrpremio * 20 / 100
print('o vencedor 3 leva', menvalor)
