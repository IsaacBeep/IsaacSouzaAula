venda = input('Registre um produto: ')
vendas = []
while venda != '':
    vendas.append(venda)
    venda = input('Registre outro produto: ')
print('Registro pronto: {}'.format(vendas))
