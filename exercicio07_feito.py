'''Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.'''
n1 = float(input('primeira nota do aluno: '))
n2 = float(input('segunda nota do aluno: '))
m = (n1+n2) / 2
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, m))
# {:.1f} (Depois do ponto flutuante coloque apenas 1 digito.)