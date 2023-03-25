'''Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.'''
n = int(input('digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print(' O dobro de {} vale {}.'.format(n, d))
print(' O triplo de {} vale {}. \n A raiz quadrada de {} é igual a {:.2f}.'.format(n, t, n, r))
###############
print('ou')
###############
n2 = int(input('digite um número: '))
print('O dobro de {} vale {}.'.format(n2, (n2*2)))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.4f}...'.format(n2, (n2*3),n2, (n2**(1/2))))

# (n2**(1/2)))) pode ser substituida pela função "pow(n2, (1/2))))"