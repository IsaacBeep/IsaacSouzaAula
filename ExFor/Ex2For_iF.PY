vendedores = [100, 50, 80, 150, 120, 30, 19]
meta = 100
I = 0

for venda in vendedores:
    if venda >= meta:
        I += 1
        
i = len(vendedores)
print('O porcentual de pessoas que bateram a meta foi de {:.1%}'.format(I/i))