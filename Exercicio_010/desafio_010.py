# Desafio 010 - Referente aula Fase07
# Crie um programa que leia quanto dinheiro uma pessoa tem
# na carteira e mostre quantos dólares ela pode comprar.

# Versão 01

real = float(input('Quanto dinheiro você tem na carteira? R$'))

dolar = 5.84

print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, (real / dolar)))
