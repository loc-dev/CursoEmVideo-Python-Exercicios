# Desafio 006 - Referente aula Fase07
# Crie um algoritmo que leia um número
# e mostre o seu dobro, triplo e raiz quadrada.

# Versão 02

num = int(input('Digite um número: '))

d = num * 2
t = num * 3
r = num ** (1/2)

print('O dobro de {} é: {}'.format(num, (num * 2)))
print('O triplo de {} é {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(num, (num * 3), num, (num ** (1/2))))

