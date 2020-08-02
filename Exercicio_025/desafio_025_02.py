# Desafio 025 - Referente aula Fase09
# Crie um programa que leia o nome de uma pessoa
# e diga se ela tem "SILVA" no nome.

# Versão 02

nome = str(input("Qual é o seu nome completo? ")).strip()

print("Seu nome tem Silva? {}".format("SILVA" in nome.upper()))
