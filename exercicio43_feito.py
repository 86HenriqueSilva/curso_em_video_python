'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
 calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
 IMC abaixo de 18,5: Abaixo do Peso
 Entre 18,5 e 25: Peso Ideal
 25 até 30: Sobrepeso
 30 até 40: Obesidade
 Acima de 40: Obesidade Mórbida'''

peso = float(input('Qual é o seu peso? (kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura**2)
print('O IMC dessa pesooa é de {}'.format(imc))
if imc < 18.5:
    print('Você está BAIXO DO PESO normal')
#elif imc >= 18.5 and imc < 25: ou
elif 18.5 <= imc< 25:
    print('Parabéns, você está na faixa de PESO NORMAL.')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO.')
elif 30<= imc <40:
    print('Você está em OBESIDADE.')
elif imc >= 40:
    print('Você está em OBESIDADE Mórbida,cuidado!.')

