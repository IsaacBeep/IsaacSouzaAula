produtos = ['tv', 'celular', 'mouse', 'teclado', 'tablet']
Nprodutos = ['forno', 'microondas']

produtos.extend(Nprodutos)
print(produtos, "\n")


produtos = ['tv', 'celular', 'mouse', 'teclado', 'tablet']
Nprodutos = ['forno', 'microondas']

print('Usando + ')
Lprodutos = produtos + Nprodutos
print(Lprodutos, "\n")


print('Usando Append + ')
produtos.append(Nprodutos)
print(produtos, "\n")