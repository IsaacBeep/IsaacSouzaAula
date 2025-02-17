estoque = [1200, 1000, 300, 400, 600, 500, 700, 900, 12, 23, 56, 89, 30]
funcionario = ['coca cola', 'pepsi', 'guarana', 'sprite', 'fanta', 'Agua da Serra', 'skol', 'brahma', 'pepsi cola', 'dolly', 'coiso', 'cachaça', 'tudo']
nivelM = 500

for i, qtde in enumerate(estoque):
    if qtde < nivelM:
        print(funcionario[i],qtde)
