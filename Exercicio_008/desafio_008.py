# Desafio 008 - Referente aula Fase07
# Escreva um programa que leia um valor em metros
# e o exiba em outras unidades de medidas de comprimento.

# Versão 01

valor_m = float(input('Digite um valor em metros: '))

print(' ')
print('A medida de {}m corresponde a: '.format(valor_m))
print('{}km (Quilômetro)'.format(valor_m / 1000))
print('{}hm (Hectômetro)'.format(valor_m / 100))
print('{:.2f}dam (Decâmetro)'.format(valor_m / 10))
print('{:.0f}dm (Decímetro)'.format(valor_m * 10))
print('{:.0f}cm (Centímetro)'.format(valor_m * 100))
print('{:.0f}mm (Milímetro)'.format(valor_m * 1000))
