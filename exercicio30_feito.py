'''Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.'''


número = int(input('Me diga um número qualquer: '))
resultado = número % 2
if resultado == 0:
    print('O número {} é Par'.format(número))
else:
    print('O Número{} é Impar'. format(número))
