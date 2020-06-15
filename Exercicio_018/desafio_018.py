# Desafio 018 - Referente aula Fase08
# Faça um programa que leia um ângulo qualquer
# e mostre na tela o valor do seno, cosseno
# e tangente desse ângulo.

# Versão 01

from math import radians, sin, cos, tan

ang = float(input('Digite o ângulo que você deseja: '))

print('O ângulo de {:.2f}º tem o SENO de {:.2f}'.format(ang, sin(radians(ang))))
print('O ângulo de {:.2f}º tem o COSSENO de {:.2f}'.format(ang, cos(radians(ang))))
print('O ângulo de {:.2f}º tem o TANGENTE de {:.2f}'.format(ang, tan(radians(ang))))
