# Desafio 017 - Referente aula Fase08
# Faça um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.

# Versão 02

cat_op = float(input('Digite o comprimento do cateto oposto: '))
cat_adj = float(input('Digite o comprimento do cateto adjacente: '))

hip = ((cat_op ** 2) + (cat_adj ** 2)) ** (1/2)

print("O valor da Hipotenusa é {:.2f}.".format(hip))
