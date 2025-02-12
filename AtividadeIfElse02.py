#Faca um programa que receba uma nota do aluno e se for superior ou igual a 7 (sete) apareça mensagem que ele esta Aprovado, se for Inferior a 5 ele esta "reprovado" e se estiver entre 5 e 7 apareça mensagem "NAO APROVADO"
nota1 = int(input('Digite o numero desejado: '))
if nota1 >= 7:
    print('Aprovado')
else:
    if nota1 >= 5:
        print('Não aprovado/reprovado direto')
    else: 
        print('Nao Aprovado/recuperação')