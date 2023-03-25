'''Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.'''

salário = float(input('Qual é o salário do funcionário? R$ '))
novo = salário + (salário * 15 / 100)
aumento = novo - salário
print('Um funcionário que ganhava R${:.2F}, com 15% de aumento, passa a receber R${:.2f}'.format(salário, novo))
print('O aumento equivale a[{:.2f}]Reais'.format(aumento))