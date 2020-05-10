# Desafio 013 - Referente aula Fase07
# Com base das versões anteriores deste desafio, vamos aprimorar!

# Faça um programa que leia um determinado preço de algum produto,
# e mostre as alternativas, à vista e parcelado. Na opção à vista
# o produto tem desconto de 5%, já parcelado tem 8% de juros.

# Bônus

price = float(input('Digite o valor do produto: R$ '))

new_price = price - ((price * 5) / 100)
new_price_parc = price + ((price * 8) / 100)

print('Por R$ {:.2f}, à vista com 5% de desconto, será R$ {:.2f}'.format(price, new_price))
print('Sendo uma compra parcelada, haverá 8% de juros no preço final, será R$ {:.2f}'.format(new_price_parc))
