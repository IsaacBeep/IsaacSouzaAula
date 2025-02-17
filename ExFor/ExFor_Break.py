pessoasP = ['Isaac', 'Ruan', 'Gabriel', 'bruno']
chamada = 'Gabriel'
for pessoa in pessoasP:
    if pessoa == chamada:
        print('{} esta presente. '.format(chamada))
        break
    else:
        print('Esta pessoa nao esta presente: '+str(pessoa))


print('')
pessoasP = ['Isaac', 'Ruan', 'Gabriel', 'bruno']
chamada = 'Gabriel'
for pessoa in pessoasP:
    if pessoa == chamada:
        print('{} esta presente. '.format(chamada))
        break
    else:
        print('Esta pessoa nao esta presente: '+str(pessoa))
        continue