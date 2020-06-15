# Desafio 016 - Referente aula Fase08
# Crie um programa que leia um número Real qualquer pelo teclado
# e mostre na tela a sua porção inteira.

# Versão 01

from math import trunc

valor = float(input('Digite um número: '))

print('O número {} tem a parte inteira {}'.format(valor, trunc(valor)))
