'''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
 e mostre quantos dólares ela pode comprar.'''

real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real / 5.33
euro = real / 5.56
print('Com R${:.2F} Você pode adquirir US ${:.2F} Dolares'.format(real, dolar))
print('ou')
print('Você pode adquirir EUR$ {:.2F} Euros'.format(euro))