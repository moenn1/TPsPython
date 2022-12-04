


class Client:
    def __init__(self, nom, numero):
        self.nom = str(nom)
        self.numero = int(numero)
        
    @property
    def Nom(self):
        return self.nom
    
    @Nom.setter
    def Nom(self, nom):
        self.nom = str(nom)
        
    @property
    def Numero(self):
        return self.numero
    
    @Nom.setter
    def Numero(self, numero):
        self.numero = int(numero)
    

class Article:
    def __init__(self, titre, prix):
        self.titre = str(titre)
        self.prix = int(prix)
        
    @property
    def Titre(self):
        return self.titre
    
    @Titre.setter
    def Titre(self, titre):
        self.titre = str(titre)
        
    @property
    def Prix(self):
        return self.prix
    
    @Prix.setter
    def Prix(self, prix):
        self.prix = int(prix)
        
class Commande:
    articles = []
    def __init__(self, date, reference, article):
        self.date = str(date)
        self.reference = int(reference)
        self.articles = article
        
    @property
    def Date(self):
        return self.date
    
    @Date.setter
    def Date(self, date):
        self.date = str(date)
        
    @property
    def Reference(self):
        return self.reference
    
    @Reference.setter
    def Reference(self, reference):
        self.reference = int(reference)
        
    @property
    def Articles(self):
        return self.articles
    
    @Articles.setter
    def Articles(self, articles):
        self.articles = int(articles)   
        
class Ligne:
    def __init__(self, article, qte):
        self.article = article
        self.qte = qte
    
    @property
    def Article(self):
        return self.article
    
    @Article.setter
    def Article(self, article):
        self.article = article
        
    @property
    def Qte(self):
        return self.qte
    
    
    @Qte.setter
    def Qte(self, qte):
        self.qte = qte
        
    
        
m = Ligne(12, 1)

print(m.Qte)