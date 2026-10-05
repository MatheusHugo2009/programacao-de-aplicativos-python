#O que é uma função:

#uma função é um bloco de código criado para realizar uma determinada tarefa

#ela permite organizar e reutilizar código

#1. Criando uma função

#Utilizar a palavra def para uma função

def saudacao():
    print("Olá, seja bem vindo")

#para executar a função, chamamos seu nome
saudacao()

#2. Função com parâmetro
def saudacao(nome):
    print(f"olá, {nome}")

saudacao("Ana")
saudacao("Carlos")

#3. Mais de um parâmetro
def apresentar(nome, idade):
    print(f"nome: {nome}")
    print(f"idade: {idade}")

apresentar("Ana", 17)

#4. Função com cálculo
def somar(numero1, numero2):
    resultado = numero1 + numero2
    print(f"resultado: {resultado}")

    somar(10 , 5)

#5. Retornando um valor
#O returm devolve um valor para o local onde a função foi chamada

def somar(numero1, numero2):
    return numero1 + numero2

resultado = somar(10 , 5)
print(resultado)

#6. Função com condição
def verificarIdade(idade):
    if idade >=18:
        return "Maior de idade"
    else:
        return "Menor de idade"

resultado = verificarIdade(20)
print(resultado)

#7 Parâmetro com valor padrão
#podemos definir um valor padrão para um parâmetro.

def saudacao(nome="Aluno"):
    print(f"Olá, {nome}")

saudacao()
saudacao("joão")

#8 varios parâmetros
def calcularMedia(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3  ) / 3
    return media
print(calcularMedia(8, 7, 9))

#9. funçoes para organizar um programa
def cadastraProduto():
    nome = input("Digite o nome do produto")
    preco = float(input("Digite o preço"))
    return nome, preco

def exibirProduto(nome ,preco):
    print("\n ==== Produto ====")
    print(f"Nome: {nome}")
    print(f"Preço: R${preco}")

nome , preco = cadastraProduto()
exibirProduto(nome , preco)