# Desafio 028 - Referente aula Fase10
# Escreva um programa que faça o computador "pensar",
# em um npumero inteiro entre  0 e 5,
# e peça para o usuário tentar descobrir,
# qual foi o número escolhido pelo computador.
# O programa deverá esscrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

computador = randint(0, 5)

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

jogador = int(input('Em que numero eu pensei? '))

print('PROCESSANDO...')
sleep(3)

if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
