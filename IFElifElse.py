meta = 20000
vendas = 25000

if vendas < meta:
    print('Não ganhou bonus')
elif vendas > (meta*2):
    bonus = 0.07 > vendas   
    print("Ganhou {} de bonus".format(bonus))
else:
    bonus = 0.03 * vendas
    print("ganhou {} de bonus".format(bonus))