produtos = ['tv', 'celular', 'mouse', 'teclado', 'tablet']

vendas = [1000, 1500, 350, 270, 900]
print('As vendas de {} foram de {}'.format(produtos[1], vendas[1]))


produtos = ['tv', 'celular', 'mouse', 'teclado', 'tablet']

i = produtos.index('mouse')
print('O valor de 1 é ' + str(i))
print('O produto de posição i é ' + str(produtos[i]))


produtos = ['tv', 'celular', 'mouse', 'teclado', 'tablet']

vendas = [1000, 1500, 350, 270, 900]

produto = input('Insira o nome do produto em letra minuscula: ').lower()

#i = produtos.index(produto)

if produto in produtos:
    print('Seu produto esta na lista')
    i = produtos.index(produto)
    print('O produto {} esta no estoque'.format(produto))
else:
    print('Seu produto nao esta na lista')


    