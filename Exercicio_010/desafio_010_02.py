# Desafio 010 - Referente aula Fase07
# Crie um programa que leia quanto de dinheiro em reais,
# uma pessoa pode comprar em Dólar, Euro e Libra.

# Versão 02

real = float(input('Digite o valor em reais : R$'))

dolar = 5.83
euro = 6.31
libra = 6.91
print('')
print('=' * 25)
print('§     D Ó L A R     §')
print('R${:.2f} vale US${:.2f}'.format(real, (real / dolar)))
print('=' * 25)
print('§     E U R O       §')
print('R${:.2f} vale {:.2f}€'.format(real, (real / euro)))
print('=' * 25)
print('§     L I B R A     §')
print('R${:.2f} vale £{:.2f}'.format(real, (real / libra)))
print('=' * 25)
