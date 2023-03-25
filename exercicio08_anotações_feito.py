# math (Biblioteca_matemática)/funcionalidade (ceil)*arredonda para cima* (floor)*arredonda para baixo*
# (trunc)*elimina da virgula para frente sem arredondamento* (pow)*potência semelhante a ** .
# (sqrt)*caucula a Raiz quadrada* (factorial)* fatorial*
# import math *importa todas as funcionalidades*
# *from* *math* import sqrt * nesse caso vc está limitado a usar a função squerroot, aqui só a raiz será importada
# de mesmo modo ao usar from math import sqrt, factorial vc está importando apenas duas funcionalidades.
import math # aqui ele traz tuda a função contida dentro de math #
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz)) # para arredondar + (num, math.ceil(raiz))
        # Arredondar resultado final #               # para arredondar - (num, math.floor(raiz))
        #caso não queira arredondar pode ser usado da seguinte forma#
# print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
# ou pode usar o sequinte método
# from math import sqrt,floor
# num = int (input('digite um número: '))
# raiz = sqrt(num)
# print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz)))
# assim com ao trazer o from trazemos juntos o math e informamos quais funções usar
# nesse caso acima from math import *sqrt,floor*