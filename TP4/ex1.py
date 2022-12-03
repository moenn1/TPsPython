

class Rectangle:
    count = 0
    def __init__(self, longueur, largeur):
      self.longueur = longueur
      self.largeur = largeur
      Rectangle.count+=1
    
    @staticmethod
    def calculerPerimetre(a, b):
        return 2*a+2*b
    
    @staticmethod
    def calculerSurface(a,b):
        return a*b
    
    def Perimetre(self):
        return Rectangle.calculerPerimetre(self.longueur, self.largeur)
    
    def Surface(self):
        return Rectangle.calculerSurface(self.longueur, self.largeur)
    
    @staticmethod
    def nombreRectangles():
        return Rectangle.count 
    
    def __str__(self):
        return "Longueur :" + str(self.longueur) + "\Largueur: "+ str(self.largeur)


a = Rectangle(5, 7)
b = Rectangle(13, 5)
print(a.Surface())
print(b.Perimetre())

print(Rectangle.nombreRectangles())