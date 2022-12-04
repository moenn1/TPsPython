from Vehicule import Vehicule


class Camion(Vehicule):
    def __init__(self, capaciteMarchandise, marchandiseActuelle, typeCarburant, capacite, carburantRestant, maxPassagers, passagersActuels):
        if maxPassagers < 3:
            super().__init__("Camion", typeCarburant, capacite, carburantRestant, maxPassagers, passagersActuels)
            self.__capaciteMarchandise = float  (capaciteMarchandise)
            self.__marchandiseActuelle = float(marchandiseActuelle)
        else:
            print("Max passagers est 2")
            exit()

    def getCapaciteMarchandise(self):
        return self.__capaciteMarchandise
    
    def setCapaciteMarchandise(self, qte):
        self.__capaciteMarchandise = qte
        
    def getMarchandiseActuelle(self):
        return self.__marchandiseActuelle
    
    def setMarchandiseActuelle(self, qte):
        self.__marchandiseActuelle = qte
        
    def chargerMarchandise(self, qte):
        if(self.__marchandiseActuelle+qte<self.__capaciteMarchandise):
            self.__marchandiseActuelle += qte
            
    def dechargerMarchandise(self, qte):
        self.__marchandiseActuelle -= qte
        
    def __str__(self):
        return super().__str__() + "  Marchandise Actuelle: " + str(self.__marchandiseActuelle) + " Capacite marchandise:  "+ str(self.__capaciteMarchandise)
    

a = Camion(2000, 120, "BENZINE", 50000, 200, 2, 1)

print(a)

a.chargerMarchandise(100)

print()

print(a)