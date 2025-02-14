#Transforma apenas a primeira letra de uma String em maiuscula
nome = "Isaac"
print(nome.capitalize(),"\n")


#transforma todas as letras em minuscula
nome = "ISAAC"
print(nome.casefold(),"\n")


#conta o numero de vezes que um caractere especifico aparece na string
nome = "Isaacsilva@gmail.com"
print(nome.count('i'), "\n")


#retorna true (verdadeiro) ou false (falso) para um teste se a string termina com uma string especifica
nome = "Isaacsilva@gmail.com"
print(nome.endswith('gmail.com'), "\n")


#encontra a posição do termo procurado lembre-se começa do zero
nome = 'isaacsilva@gmail.com'
print(nome.find('@'),"\n")


#verifica se  o texto é todo feito com letras
nome = "isaac"
print(nome.isalpha(),"\n")


#verifica se o texto é feito com numeros
nome = "123"
print(nome.isnumeric(), "\n")


#substitui um caractere escolhido por outro
nome = "isaac"
print(nome.replace("c"," "), '\n')


#separa o texto string baseado em algum caractere indicado
nome = "isaac @ ruan"
print(nome.split("@"), "\n")


#colocar todas as letras iniciais em maiscula
nome = 'isaac silva de lima souza'
print(nome.title(), "\n")


#retira caractere indesejados, como por exemplo espaços que nao agregam valor
nome = " isaac silva de lima souza "
print(nome.strip(), "\n")


#retorna true ou false para um teste de uma string se inicia com um texto especifico
nome = "isaac 2007"
print(nome.startswith("isa"), "\n")
print(nome.startswith("Isa"), "\n")