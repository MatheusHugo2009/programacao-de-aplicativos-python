#AULA: OPERADORES LÓGICOS E ESTRUTURAS CONDICIONAIS
# 1. OPERADORES LÓGICOS
from operator import truediv

# Os operados lógicos permitem combinar condições.

# and
# Todas as condições precisam ser verdadeiras

idade = 20
possui_carteira = True

resultado = idade >= 18 and possui_carteira
print(resultado)