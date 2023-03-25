'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

casa = float(input('Valor da casa:R$ '))
salário = float(input('Salário do comprador:R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
minimo = salário * 30 / 100
print('Para pegar uma casa de R${:.2F} em {} anos'.format(casa, anos), end='. ') # se liga na ideia do end= juntou dois prints
print('A prestação será de R${:.2f}'.format(prestação))
if prestação <= minimo:
    print('Emprestimo pode ser Concedido!')
else:
    print('Emprestimo Negado!')
