# Desafio 017 - Referente aula Fase08
# Faça um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.

# Versão 03

from math import hypot

cat_op = float(input('Digite o valor do cateto oposto: '))
cat_adj = float(input('Digite o valor do cateto adjacente: '))

hip = hypot(cat_op, cat_adj)

print('O valor da hipotenusa é {:.2f}.'.format(hip))
