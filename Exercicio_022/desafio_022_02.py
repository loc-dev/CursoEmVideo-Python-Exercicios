# Desafio 022 - Referente aula Fase09
# Crie um programa que leia o nome completo de uma pessoa
# e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras no total (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

# Versão 02

nome = str(input("Digite o seu nome completo: ")).strip()

print('')
print("Analisando o seu nome...")
print("Seu nome em letras maiúsculas é: {}".format(nome.upper()))
print("Seu nome em letras minúsculas é: {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras".format(len(nome) - nome.count(" ")))
print("Seu primeiro nome é {} e ele tem {} letras".format(nome.split()[0], nome.find(" ")))
