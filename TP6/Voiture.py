from Vehicule import Vehicule


class Voiture(Vehicule):
    def __init__(self, taille, typeCarburant, capacite, carburantRestant, maxPassagers, passagersActuels):
        super().__init__("Voiture", typeCarburant, capacite, carburantRestant, maxPassagers, passagersActuels)
        self.__taille = str(taille)

    def getTaille(self):
        return self.__taille
    
    def setTaille(self, taille):
        self.__taille = str(taille)
        
    def __str__(self):
        return super().__str__() + "  Taille: " + self.__taille

# m = Voiture('p', 'diesel', 5000, 500, 230, 200)

# print(m)

# m.addCarburant(500)

# print()
# print(m)
# print()

# m.faireLePlein()

# print(m)