# Desafio 031 - Referente aula Fase10
# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200km
# e R$ 0,45 para viagens mais longas.

# Versão 02

distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distancia))

p = distancia * 0.50 if distancia <= 200 else distancia * 0.45

print('E o preço da sua passagem será de R${:.2f}'.format(p))
