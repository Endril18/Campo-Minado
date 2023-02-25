import random

# Criação da Matriz
def criarMatriz(vazio, bomba, quantBomba, espacos):
  
  item = (bomba * quantBomba)
  while(len(item) < 36):
    item += vazio
  
  novaLista = list (item)
  
  #embaralhar
  novaLista = random.sample(novaLista, len(novaLista)) 
  
  #Formando uma Matriz
  matriz = []
  pEsq = 0
  pDir = 6
  for j in range(6):
    matriz.append(novaLista[pEsq:pDir])
    pEsq += 6 
    pDir += 6
  
  return matriz
