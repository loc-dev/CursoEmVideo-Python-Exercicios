# Desafio 027 - Referente aula Fase09
# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input("Digite o seu nome completo: ")).strip()

print('')
print("Muito prazer em te conhecer !")
print("Seu primeiro nome é {}".format(nome.split()[0]))
print("Seu último nome é {}".format(nome.split()[-1]))
