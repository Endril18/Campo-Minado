# imports
import random
import time
import funcoes

# Itens da Matriz
espacos = 36 
campoVazio = ["X"]
campoBomba = ["💣"]
quantidadeBombas = 10

# Criacção da Matriz
matriz = funcoes.criarMatriz(campoVazio, campoBomba, quantidadeBombas, espacos)

for i in range(6):
  print(matriz[i])