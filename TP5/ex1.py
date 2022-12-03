


class CompteBancaire:
    serie = '505'
    titulaire = ""
    solde = 0
    numero = serie
    
    def __str__(self):
        return "Le solde du compte: " + str(self.numero)  + " est " + str(self.solde)
    
    @property
    def Solde(self):
        return self.solde
    @property
    def Numero(self):
        return self.numero
    @property
    def Titulaire(self):
        return self.titulaire
    @Solde.setter
    def Solde(self, solde):
        self.solde = solde
    @Numero.setter
    def Numero(self, id):
        self.numero = CompteBancaire.numero + "-" + str(id)
    @Titulaire.setter
    def Titulaire(self, titulaire):
        self.titulaire = titulaire
    
    
class Client:
    def __init__(self, nom, prenom, age, adresse):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.adresse = adresse
        self.comptes = []
    
    @property
    def Nom(self):
        return self.nom
    
    @Nom.setter
    def Nom(self, nom):
        self.nom = nom
    
    @property
    def Prenom(self):
        return self.prenom
    @Prenom.setter
    def Prenom(self, prenom):
        self.prenom = prenom
    
    @property
    def Adresse(self):
        return self.adresse
    @Adresse.setter
    def Adresse(self, adresse):
        self.adresse = adresse
    
    @property
    def Comptes(self):
        return self.comptes
    @Comptes.setter
    def Comptes(self, comptes):
        self.comptes = comptes
        
    
    def addCompteBancaire(self, compte):
        compte.titulaire = str(self.Nom) + " " + str(self.Prenom)
        self.Comptes.append(compte)  
          
    def identifierCompte(self):
        print("Choisir le compte (1, 2...): ")
        count =  1
        for i in self.Comptes:
            print(str(count) + ". Numero: " + str(i.Numero) + " Solde: "+ str(i.Solde) + "\n")
            count +=1
        nbcompte = int(input("Saisir: "))
        return self.Comptes[nbcompte]
    
    
    def Deposer(self, n):
        c = self.identifierCompte()
        c.Solde += n
        print("Somme: " + str(n) + " deposée\nNouveau Solde: "+ str(c.Solde))
        
    def Retirer(self, n):
        c = self.identifierCompte()
        if(c.Solde>n):
            c.Solde -= n
            print("Somme: " + str(n) + " deposée\nNouveau Solde: "+ str(c.Solde))   
        else:
            print("Fonds insuffisants") 
    
    def __str__(self):
        outputString = ""
        for i in self.Comptes:
            outputString += i.__str__() + "\n"
        return outputString


m = Client("ennassibi", "mohamed", 21, "Nador")

a = CompteBancaire()
a.Solde = 1500
a.Numero = 1

b = CompteBancaire()
b.Solde = 152200
b.Numero = 2

c = CompteBancaire()
c.Solde = 152300
c.Numero = 3

d = CompteBancaire()
d.Solde = 12300
d.Numero = 4

m.addCompteBancaire(a)
m.addCompteBancaire(b)
m.addCompteBancaire(c)
m.addCompteBancaire(d)

print(m)

m.Retirer(300)

print(m)