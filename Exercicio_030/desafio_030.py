# Desafio 030 - Referente aula Fase10
# Crie um programa que leia um número inteiro
# e mostre na tela se ele é PAR ou ÍMPAR.

n = int(input('Me diga um número qualquer: '))

r = n % 2

if r == 0:
    print('O número {} é PAR'.format(n))
else:
    print('O número {} é ÍMPAR'.format(n))
