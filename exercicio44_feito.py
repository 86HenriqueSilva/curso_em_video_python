'''Elabore um programa que calcule o valor a ser pago por um produto,
 considerando o seu preço normal e condição de pagamento:
 à vista dinheiro/cheque: 10% de desconto
 à vista no cartão: 5% de desconto
 em até 2x no cartão: preço formal
 3x ou mais no cartão: 20% de juros'''

#print(f'{"EXPAND CONNECTION":=^40}') OU
print('{:=^40}'.format('EXPAND CONNECTION'))
preço = float(input('Preço das compras: R$ '))
print('''Formas de Pagamento
[ 1 ] À VISTA Dinheiro/Pix
[ 2 ] À VISTA  Cartão Débito
[ 3 ] 2X no Cartão 
[ 4 ] 3x ou mais no Cartão ''')
Opção = int(input('Qual é a Opção Desejada? '))
if Opção == 1:
    total = preço - (preço * 10 / 100)
elif Opção == 2:
    total = preço - (preço * 5 / 100)
elif Opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2F} SEM JUROS '.format(parcela))
elif Opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas Parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}X de R${:.2f} COM JUROS '.format(totparc, parcela))
else:
    total = preço
    print('OPÇÃO DIGITADA NÃO ESTÁ ENTRE AS OPÇÕES!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))



