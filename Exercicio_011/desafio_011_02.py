# Desafio 011 - Referente aula Fase07
# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade tinta necessária para pintá-la,
# sabendo que cada litro de tinta, pinta uma área de 2m².

# Versão 02

h = float(input('Digite o valor em metros da altura da parede: '))
w = float(input('Digite o valor em metros da largura da parede: '))

a = h * w

print('A área a ser pintada é {:.2f}m².'.format(a))
print('Para pintar toda a parede, é necessário {:.2f}l de tinta.'.format(a / 2))
