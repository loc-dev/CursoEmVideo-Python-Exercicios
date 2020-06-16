# Desafio 019 - Referente aula Fase08
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles
# e escrevendo o nome do escolhido.

# Versão 01

from random import choice

nome_01 = input('Primeiro Aluno: ')
nome_02 = input('Segundo Aluno: ')
nome_03 = input('Terceiro Aluno: ')
nome_04 = input('Quarto Aluno: ')

alunos = [nome_01, nome_02, nome_03, nome_04]

print('O aluno escolhido foi {}'.format(choice(alunos)))
