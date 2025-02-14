faturamento = input('Qual foi o faturamento da loja esse mes? ')
custo = input('Qual foi o custo da loja nesse mês? ')

if faturamento == '' and custo == '':
    print('Tente novamente e digite um numero')

else:
    lucro = int(faturamento) - int(custo)
    print('O lucro da loja foi de {}'.format(lucro))

#elif custo == '':
#print('Tente novamente e digite um numero')