# Desafio 008 - Referente aula Fase07
# Escreva um programa que leia um valor em metros
# e o exiba convertido em centímetros e milímetros.

# Versão 02

valor_m = float(input('Digite um valor em metros: '))

print(' ')
print('A medida de {}m convertido para centímetros e milímetros será: '.format(valor_m))
print('Em centímetros: {:.0f}cm'.format(valor_m * 100))
print('Em milímetros: {:.0f}mm'.format(valor_m * 1000))
