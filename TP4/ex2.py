

class CompteBancaire:
    def __init__(self, numeroCompte, nom, solde):
        self.numeroCompte = int(numeroCompte)
        self.nom = str(nom)
        self.solde = float(solde)
    
    def __str__(self):
        return "NumeroCompte = + str(self.numeroCompte) + str(self.nom)+ str(self.solde)"




        
a = CompteBancaire(4, 'mohamed', 21)
print(a)