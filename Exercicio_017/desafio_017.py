# Desafio 017 - Referente aula Fase08
# Faça um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.

# Versão 01

from math import pow, sqrt

a = float(input('Comprimento do cateto oposto: '))
b = float(input('Comprimento do cateto adjacente: '))

a = pow(a, 2)
b = pow(b, 2)

c = a + b

c = sqrt(c)

print('A Hipotenusa vai medir {:.2f}'.format(c))
