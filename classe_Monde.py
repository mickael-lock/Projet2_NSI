class Monde(dimension,duree_repousse,carte):
"""
dimension = entier, min 50, taille du côté de la matrice
duree_pousse = entier entre 1 et 100, vitesse de repousse herbe
carte = liste de liste, matrice de dimension dimension(variable en haut) + c'est une matrice carré
"""
  def __init__(self):
    self.contenu = carte
    self.__duree_repousse = duree_repousse
    self.__dimension = dimension
    
  def nbHerbe(self):
    cpt = 0
    for i in range(self.__dimension):
      for j in range(self.__dimension):
        if self.contenu[i][j]>self.__duree_repousse:
          cpt += 1
    return cpt
        
  def herbePousse(self):
    for i in range(self.__dimension):
      for j in range(self.__dimension):
        self.contenu[i][j] += 1
        
  def herbeMangee(self,i,j):
    self.contenu[i][j] = 0
    
  def getCoefCarte(self,i,j):
    return self.contenu[i][j] 
