# Desafio 005 - Referente aula Fase07
# Faça um programa que leia um número inteiro
# e mostre na tela o seu sucessor e seu antecessor.

# Versão 01

num = int(input('Digite um número: '))

num_ant = num - 1
num_suc = num + 1

print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(num, num_ant, num_suc))
