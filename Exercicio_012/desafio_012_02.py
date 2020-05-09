# Desafio 012 - Referente aula Fase07
# Faça um algoritmo que leia o preço de um produto
# e mostre seu novo preço, com 5% de desconto.

# Versão 02

price = float(input('Qual é o preço do produto? R$'))

new_price = price - ((price * 5) / 100)

print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(price, new_price))
