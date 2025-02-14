#Faça um programa que o usuario digite um numero e diga se o numero é superior a 20, inferior a 10 ou se esta entre 10 a 20
num1 = int(input('Digite o numero desejado: '))
if num1 > 20:
    print('Seu numero é maior que 20')
elif num1 < 10:
    print('Seu numero é menor que 10')
else:
    print('Seu numero esta entre 10 e 20')