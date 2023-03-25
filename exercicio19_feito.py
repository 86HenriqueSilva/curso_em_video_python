'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.'''


import random
n1 = str(input('1º ALUNO: '))
n2 = str(input('2º ALUNO: '))
n3 = str(input('3º ALUNO: '))
n4 = str(input('4º ALUNO: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
#'ou'
#'''from random import choice
#n1 = str(input('1º ALUNO: '))
#n2 = str(input('2º ALUNO: '))
#n3 = str(input('3º ALUNO: '))
#n4 = str(input('4º ALUNO: '))
#lista = [n1, n2, n3, n4]
#escolhido = choice(lista)
#print('O aluno escolhido foi {}'.format(escolhido))