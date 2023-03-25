nome = str(input('Qual é seu Nome? '))
if nome == 'Gustavo':
 print('Que nome Bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu Nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo Nome feminino')
else:
    print('Seu Nome é bem Normal.')
print('Tenha um bom dia , {}!'.format(nome))
