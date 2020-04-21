# Desafio 004 - Referente aula Fase06
# Faça um programa que leia algo pelo teclado
# e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele.

# Versão 01

dado = input('Digite algo: ')

print('')
print('O tipo primitivo desse valor dado pelo usuário é: ', type(dado))
print('O valor consiste apenas em caracteres númericos: ', dado.isnumeric())
print('O valor consiste apenas em caracteres alfabéticos: ', dado.isalpha())
print('O valor consiste em caracteres alfanuméricos: ', dado.isalnum())
print('O valor consiste em espaços em branco: ', dado.isspace())
print('')
print('Todas os caracteres(letras) estão em maiúsculas: ', dado.isupper())
print('Todas os caracteres(letras) estão em minúsculas: ', dado.islower())
print('A primeira letra é maiúscula (Capitalizada): ', dado.istitle())