# Desafio 004 - Referente aula Fase06
# Faça um programa que leia algo pelo teclado
# e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele.

# Versão 02

dado = input('Digite algo: ')

print('')
print('O tipo primitivo desse valor dado pelo usuário é: ', type(dado))
print('O valor consiste apenas em caracteres númericos: {}'.format(dado.isnumeric()))
print('O valor consiste apenas em caracteres alfabéticos: {}'.format(dado.isalpha()))
print('O valor consiste em caracteres alfanuméricos: {}'.format(dado.isalnum()))
print('O valor consiste em espaços em branco: {}'.format(dado.isspace()))
print('')
print('Todas os caracteres(letras) estão em maiúsculas: {}'.format(dado.isupper()))
print('Todas os caracteres(letras) estão em minúsculas: {}'.format(dado.islower()))
print('A primeira letra é maiúscula (Capitalizada): {}'.format(dado.istitle()))
