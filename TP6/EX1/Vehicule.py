class Vehicule:
    def __init__(self, type, typeCarburant, capacite, carburantRestant, maxPassagers, passagersActuels):
        self.__type = str(type)
        self.__typeCarburant = str(typeCarburant)
        self.__capacite = float(capacite)
        self.__carburantRestant = float(carburantRestant)
        self.__maxPassagers = int(maxPassagers)
        self.__passagersActuels = int(passagersActuels)
    
    def getTypeCarburant(self):
        return self.__typeCarburant
    
    def getCapacite(self):
        return self.__capacite
    
    def getCarburantRestant(self):
        return self.__carburantRestant
    
    def getMaxPassagers(self):
        return self.__maxPassagers
    
    def getPassagersActuels(self):
        return self.__passagersActuels
    
    def setMaxPassagers(self, max):
        try:
            self.__maxPassagers = int(max)
        except:
            print("Valeur non numerique")
    
    def addCarburant(self, quantite):
        self.__carburantRestant +=  float(quantite)
    
    def consommerCarburant(self, quantite):
        if(quantite>self.__carburantRestant):
            print("Pas assez de carburant")
        else:
            self.__carburantRestant -= quantite
            
    def faireLePlein(self):
        self.__carburantRestant += self.__capacite - self.__carburantRestant
    
    def aPlacesLibres(self, nombrePlaces):
        if(self.__passagersActuels+nombrePlaces<self.__maxPassagers):
            return True
        return False
    
    def prendrePassagers(self, nombrePlaces):
        if(self.aPlacesLibres(nombrePlaces)):
            self.__passagersActuels += nombrePlaces
    
    
    def __str__(self):
        return   "Type: " + self.__type + "  Type de carburant: " + self.__typeCarburant + "  Capacite: " + str(self.__capacite) + "  Carburant restant: " + str(self.__carburantRestant) + "  Max passagers: " + str(self.__maxPassagers) + "  Passagers actuels: " + str(self.__passagersActuels)

    


