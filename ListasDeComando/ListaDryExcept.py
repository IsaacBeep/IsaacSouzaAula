produtos = ['tv', 'celular', 'mouse', 'teclado', 'tablet']
item_usuario = input('Qual item deseja remover: ')
try:
    produtos.remove(item_usuario)
    print(produtos)
except:
    print('o produton "{}" nao existe na lista'.format(item_usuario))
    
#len = Mostra uma quantidade de itens na lista
#min = Mostra o min de valor em uma lista
#max = Mostra o max de valor em uma lista