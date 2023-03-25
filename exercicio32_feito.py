'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto.'''


from datetime import date
ano = int(input('Insira o ano que deseja analisar? Para analisar ano atual basta inserir [ 0 ]: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: # 'if_se' 'and_ e tambem' ['!="] não iqual or_ ou então
    print('O ano {} informado é Bissexto'.format(ano))
else:
    print('O ano {} informado não é Bissexto'.format(ano))
