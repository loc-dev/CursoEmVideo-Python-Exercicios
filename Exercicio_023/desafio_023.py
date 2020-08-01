# Desafio 023 - Referente aula Fase09
# Faça um programa que leia um número de 0 a 9999
# e mostre na tela cada um dos digitos separados.
# Exemplo:
# 1834
# unidade: 4 | dezena: 3 | centena: 8 | milhar: 1

num = int(input("Digite um número: "))

unid = (num // 1) % 10
dez = (num // 10) % 10
cen = (num // 100) % 10
mil = (num // 1000) % 10

print('')
print("Analisando o número {}".format(num))

print('')
print("Unidade: {}".format(unid))
print("Dezena: {}".format(dez))
print("Centena: {}".format(cen))
print("Milhar: {}".format(mil))
