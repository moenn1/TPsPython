

n = int(input("Saisir n: "))

liste = ['abce', 'aufehef', 'nfnf', 'nn', 'hhh', 'lole', 'jijfir']

outputListe = []

for i in liste:
    if len(i)> n:
        outputListe.append(i)
        
        
print(outputListe)