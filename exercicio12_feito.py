'''Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.'''

preço = float(input('informe o preço do produto? R$ '))
novo = preço - (preço * 5 / 100)
economia = (preço-novo)
print('Preço do Produto:........... R$ {:.2F}'.format(preço))
print('Desconto de [ 5% ] Aplicado: R$ {:.2F}'.format(novo))
print('Você Economizou  [R$ {:.2f}]'.format(economia))
