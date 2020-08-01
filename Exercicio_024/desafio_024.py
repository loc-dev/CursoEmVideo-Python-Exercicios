# Desafio 024 - Referente aula Fase09
# Crie um programa que leia o nome de uma cidade
# e diga se ela começa ou não com o nome "SANTO".

cidade = str(input("Em que cidade você nasceu? ")).strip()

cidade = cidade.upper()

print('SANTO' in cidade[:5])
