'''Escreva um programa em Python que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:
 1 para binário, 2 para octal e 3 para hexadecimal.'''


num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
opção = int(input('Sua Opção: '))
if opção == 1:
    print('{} Convertido para BINÁRIO é igual a {}'.format(num,bin(num)[2:]))
elif opção == 2:
    print('{} Convertido para OCTAL é iqual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} Convertido para HEXADECIMAL é iqual a {}'.format(num, hex(num,)[2]))
else:
    print('NÚMERO DIGITADO NÃO CONTA NA LISTA [1] [2] [3] FAVOR TENTE NOVAMENTE!')