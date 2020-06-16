# Desafio 020 - Referente aula Fase08
# O mesmo professor do desafio anterior que sortear
# a ordem de apresentação de trabalhos dos alunos
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

# Versão 01

from random import sample

nome_01 = input('Primeiro Aluno: ')
nome_02 = input('Segundo Aluno: ')
nome_03 = input('Terceiro Aluno: ')
nome_04 = input('Quarto Aluno: ')

alunos = [nome_01, nome_02, nome_03, nome_04]

print('A ordem de apresentação será {}'.format(sample(alunos, 4)))
