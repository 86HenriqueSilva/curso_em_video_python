'''Exercício Python 003:
Crie um programaqueleia dois números e mostre a soma entre eles.'''

a = input('digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('só tem espaços?', a.isspace())
print('É um número?', a.isnumeric())
print('É alfabetico?', a.isalpha())
print('É alfanúmerico', a.isalnum())
print('É maiúscula?', a.isupper)
print(' está em minúsculas?', a.islower())
print('está capitalizada?', a.istitle())