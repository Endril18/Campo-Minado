import random

# Cria a matriz do campo minado
def criarMatriz(bomba, quantBomba, tamanho):
  novaLista = []
  campo = tamanho * tamanho
  contBomba = 0
  while(len(novaLista) != campo):
    if(contBomba < quantBomba):
      novaLista.append(bomba)
      contBomba += 1
    novaLista.append(0)
        
  #embaralhar
  random.shuffle(novaLista) 
  
  #Formando uma Matriz
  matriz = []
  pEsq = 0
  pDir = 6
  for con in range(6):
    matriz.append(novaLista[pEsq:pDir])
    pEsq += 6 
    pDir += 6
  
  return matriz

# Contagem das Minas Adjacentes
def minasAdjacentes(campoMinado, tamanhoCampo):
    for i in range(tamanhoCampo):
        for j in range(tamanhoCampo):
            if campoMinado[i][j] == "💣":
                continue
            for k in range(max(0, i - 1), min(tamanhoCampo, i + 2)):
                for l in range(max(0, j - 1), min(tamanhoCampo, j + 2)):
                    if campoMinado[k][l] == "💣":
                        campoMinado[i][j] += 1
    return campoMinado
