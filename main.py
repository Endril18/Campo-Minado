# imports
import random
import time
import pygame, sys
from pygame.locals import QUIT
import funcoes

# inicializar Pygame
#pygame.init()

# Configurações do jogo
#larguraTela = 640
#alturaTela = 480
#noBombs = 60
#bombsPlaced = 25

# Criar a tela
#tela = pygame.display.set_mode((larguraTela, alturaTela))
#pygame.display.set_caption('Campo Minado')
#while True:
#    for event in pygame.event.get():
#        if event.type == QUIT:
#            pygame.quit()
#            sys.exit()
#    linha = 0
#    for i in range(26):     
#      pygame.draw.line(tela, (255, 255, 255), (linha, 0), (linha, 480), 2)
#      linha += 25

#    pygame.display.update()

# Carrega as imagens
#bombsImg =

# Cria a matriz do campo minado
#for i in range(10):

# Coloca as minas aleatoriamente

# Conta o número de minas adjacentes para cada célula

# Função para abrir uma célula

# Mostra todas as minas

# Abre as células adjacentes

# ----------------------------------------------------


# No Terminal

# Itens da Matriz
campoVazio = ["X"]
campoBomba = ["💣"]
quantidadeBombas = 10

for i in range(6):
  print(funcoes.criarMatriz(campoVazio, campoBomba, quantidadeBombas)[i])