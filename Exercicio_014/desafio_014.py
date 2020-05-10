# Desafio 014 - Referente aula Fase07
# Escreva um programa que converta uma temperatua
# digita em ºC e converta para ºF.

# Versão 01

grau_c = float(input('Informe a temperatura em ºC: '))

grau_f = ((grau_c / 5) * 9) + 32

print('A temperatura de {:.1f}ºC corresponde a {:.1f}ºF'.format(grau_c, grau_f))
