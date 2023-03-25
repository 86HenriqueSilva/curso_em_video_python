'''Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.'''

n = int(input('Digite um Número:'))
a = n - 1
s = n + 1
print('Analisando o valor {}, seu Antecessor é {} e o Sucessor é {}'.format(n, a, s))
#########################################################################################
print('ou')
n = int(input('digite um número: '))
print('Analisando o valor {}, seu Antecessor é {} e o Sucessor é {}'.format(n, (n-1), (n+1)))