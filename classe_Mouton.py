class Mouton:
 """
 gain_nourriture: gain énergie apporté par la conso d'un carré d'herbe / valeur par défaut = 4
 position_x et position_y: position du mouton couple de x;y
 energie: >0 ou =0 / si energie = 0 le mouton meurt + initialisé entre 1 et 2 X gain_nourriture
 taux_reproduction: entier entre 1 et 100, 4 par défaut, chance d'un mouton de se reproduire
 """
 
 def __init__(self,gain_nourriture, position_x,position_y, energie, taux_reproduction,carte)):
  self.mouton = self
  
def variationEnergie(self,f,i,j):
        self.carte2=f
        if self.carte2[i][j] == 0:
            self.energie = self.energie - 1
        else:
            self.energie = self.energie + self.gain_nourriture
        return self.energie

    def déplacement(self) :
        a=random.randint(-1,1)
        b=random.randint(-1,1)
        if a==-1 and  self.position_x==0:
            a=0
        if b==-1 and  self.position_y==0:
            b=0
        if a==1 and  self.position_x==self.dimen-1:
            a=0
        if b==1 and  self.position_y==self.dimen-1:
            b=0
        else:
            self.position_x=self.position_x+a
            self.position_y=self.position_y+b

    def place_mouton(self,i,j) :
        self.position_x = i
        self.position_y = j


    def nbMouton(self):
        c=0
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.position_x==i and self.position_y==j:
                    c=c+1
        return c
    def carte2(self,f):
        self.carte2=f

    def d_ener(self):
        return self.energie
  

  
