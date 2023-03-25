'''Faça um programa que leia algo pelo teclado
e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.'''
# + adição - subtração *multiplicação
# /divisão **potenciação //divisão inteira % resto da divisão(mod)
# Orden de precedência 1.() 2.**exponenciação 3.* /divisão // divisão inteira % resto da divisão
# + adição - subtração pow(4,3)função interna(perca de ordem de precedência
# 81**(1/2) para achar a raiz quadrada de um número divide por (meio)
# uma dica é poder usar (oi + olá= oilá) logo 'oi'*5 =(oioioioioi)
# {} chamado como máscara de substituição
nome = input('qual é seu nome? ')
print('Prazer em te conhecer! {:=^20}'.format(nome))
############################################################
n1 = int(input('um valor: '))
n2 = int(input('outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('a soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end='')
print('a soma inteira {} e potência {}'.format(di, e))
# end='' a expressão juntou as duas linhas que envolvem o print.
################################################################