# Desafio 007 - Referente aula Fase07
# Desenvolva um programa que leia as duas notas de um aluno,
# calcule e mostre a sua média.

# Versão 01

nota_01 = float(input('Primeira nota do Aluno: '))
nota_02 = float(input('Segunda nota do Aluno: '))

m = (nota_01 + nota_02) / 2

print('A média entre a primeira nota {} e a segunda nota {} \né igual a {:.1f}'.format(nota_01, nota_02, m))
