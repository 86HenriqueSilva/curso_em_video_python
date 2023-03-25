r = int(input('Qual nº você desaja que seja feito o fatorial?'))
m = 1
for c in range(1, r+1):
   m *= c
   print(c, end='')
   print(' X ', end='')
print(m)