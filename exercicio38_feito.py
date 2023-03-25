'''Escreva um programa que leia dois números inteiros e compare-os.
  Mostrando na tela uma mensagem:
    - O primeiro valor é maior
    - O segundo valor é maior
    - Não existe valor maior, os dois são iguais.'''

n1 = int(input('DIGITE O 1º Número: '))
n2 = int(input('DIGITE O 2º Número: '))
if n1 > n2:
     print('1º Número tem MAIOR VALOR ')
elif n2 > n1:
     print('2º Número tem MAIOR VALOR ')
elif n1 == n2:
     print('OPS\' >> OS DOIS NÚMEROS INFORMADOS TEM O MESMO VALOR  <<')

