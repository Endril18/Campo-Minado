# imports
import random
import time
import pygame, sys
from pygame.locals import QUIT

# inicializar Pygame
pygame.init()

# Configurações do jogo
larguraTela = 640
alturaTela = 480
clear = 60
bombs = 25

# Criar a tela
DISPLAYSURF = pygame.display.set_mode((larguraTela, alturaTela))
pygame.display.set_caption('Campo Minado')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

  # Carrega as imagens
  #bombsImg =

  # Cria a matriz do campo minado
  #for i in range(10):
  
  # Coloca as minas aleatoriamente

  # Conta o número de minas adjacentes para cada célula

  # Função para abrir uma célula

    # Mostra todas as minas

    # Abre as células adjacentes