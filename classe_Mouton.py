class Mouton:
 """
 gain_nourriture: gain énergie apporté par la conso d'un carré d'herbe / valeur par défaut = 4
 position_x et position_y: position du mouton couple de x;y
 energie: >0 ou =0 / si energie = 0 le mouton meurt + initialisé entre 1 et 2 X gain_nourriture
 taux_reproduction: entier entre 1 et 100, 4 par défaut, chance d'un mouton de se reproduire
 """
 
 def __init__(self,gain_nourriture, position_x,position_y, energie, taux_reproduction,carte)):
  self.mouton = self
  
 def variationEnergie(i,j):
  
