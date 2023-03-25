from random import choice
#DIFICULDADE
lista= []
palpites = 0
dificuldade = int(input('Digite o total de números que você quer no jogo:'))
for c in range(1,dificuldade +1):
    lista.append(c)
#ESCOLHA
print('Tente adivinhar o número que eu estou pensando!!')
escolha = int(input(f'\nEscolha um número de 1 à {dificuldade}:'))
pc = choice(lista)
if escolha != pc:
    palpites+=1
if escolha == pc:
    palpites +=1
#ANÁLISE
while escolha != pc:
    escolha = int(input('Você errou!! tente outra vez:'))
    palpites+= 1
print('Meus parabéns!!! Você acertou!!!')
print(f'Palpites necessários: {palpites}')