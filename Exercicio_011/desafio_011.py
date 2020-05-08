# Desafio 011 - Referente aula Fase07
# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade tinta necessária para pintá-la,
# sabendo que cada litro de tinta, pinta uma área de 2m².

# Versão 01

h = float(input('Altura da parede em metros: '))
w = float(input('Largura da parede em metros: '))

a = h * w

print('Sua parede tem a dimensão de {}m x {}m e sua área é de {}m².'.format(h, w, a))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(a / 2))
