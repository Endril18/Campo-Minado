# imports
import random
import time
import funcoes

# Itens da Matriz
tamanhoCampo = 6 
campoVazio = 0
campoBomba = "💣"
quantidadeBombas = 10

# Criacção da Matriz
matriz = funcoes.criarMatriz(campoBomba, quantidadeBombas, tamanhoCampo)

# Contagem das bombas adjacentes
cont = funcoes.minasAdjacentes(matriz, tamanhoCampo)

for j in range(6):
  print(cont[j])