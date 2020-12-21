# Tipos Primitivos

# float 
pi = 3.14
# int
idade = 25
# boolean
maior_de_idade = True
# str
nome = "Luciana"

# Iteraveis
# list
lista = ["a", "b", "c", 5, [1, 2, 3, {"k":20}], ("tupla", "lista")]
# dictionary
dicionario = {"cores":["verde", "vermelho", "azul"], "b":False}
# set
conjunto = {"banana", "maca", "brocolis", "banana"}# dicionario}
# tuples
tupla = (1, 2, 3, lista)
#tupla[2] = "arvore" # nao da certo
tupla[3][0] = "C" # da certo

# Estruturas de Decisao

# if
if tupla[0] == 1:
    print("alguma coisa")
#elif
elif tupla[0] == 2:
    print("outra coisa")
# else
else:
    print("sei la")

# for
for i in lista:
    print(i)
# while
tamanho = len(lista)
while tamanho > 0:
    print("alguma coisa também")
    tamanho -= 1
# 

# Formas para interagir com o usuário

# print()
print("{} tem {} anos.".format(nome, idade))
print(f"{nome} tem {idade} anos.") # interpolação de strings
print(nome, idade, pi) # __str__
print(nome + str(idade) + str(pi))

nome = input(f"O valor do nome é {nome}.\nDigite um novo valor")
print(int(nome) + idade + pi)

