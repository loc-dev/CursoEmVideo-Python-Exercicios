# Desafio 013 - Referente aula Fase07
# Faça um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário, com 15% de aumento.

# Versão 02

name = input('Digite o nome do funcionário(a): ')
salary = float(input('Qual é o salário de {}: R$'.format(name)))

new_salary = salary + ((salary * 15) / 100)

print('{} que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(name, salary, new_salary))
