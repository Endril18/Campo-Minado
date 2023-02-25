import random

# Criação da Matriz
def criarMatriz(vazio, bomba, quantBomba):
  novaLista = []
  campoBomba = 0
  for i in range(36):
    while(quantBomba > campoBomba):
      novaLista.append(bomba)
      campoBomba += 1
    
    novaLista.append(vazio)

  #embaralhar
  random.shuffle(novaLista)

  #Formando uma Matriz
  matriz = []
  pEsq = 0
  pDir = 6
  for j in range(6):
    matriz.append(novaLista[pEsq:pDir])
    pEsq += 6 
    pDir += 6
  
  return matriz
