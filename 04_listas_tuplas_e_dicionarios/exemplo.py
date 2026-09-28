#Listas, Tuplas e Dicionários


#1. Listas


#Listas são utilizadas para armazenar vários valores
#dentro de uma única variável


nomes = ["Ana","Carlos","João","Maria"]
print(nomes)


#2.Acessando elementos na Lista


print(nomes[0])
print(nomes[1])


# Podemos acessar o ultimo elemento usando -1
print(nomes[-1])


# 3. Alternando elementos


#As listas são mutáveis, ou seja, os elementos podem ser alterados
nomes[0] = "Pedro"
print(nomes)


# 4. Adicionando Elementos
#append() adiciona um elemento no final da lista.
nomes.append("Lucas")
print(nomes)


# insert() adiciona um elemento em uma posição
nomes.insert(1, "Mariana")
print(nomes)


#5. Removendo Elementos
#remove() remove o elemento pelo seu valor
nomes.remove("Lucas")
print(nomes)


#pop() remove um elemento pelo índice
nomes.pop(0)
print(nomes)
