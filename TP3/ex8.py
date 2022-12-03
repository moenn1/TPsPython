


def somme(liste):
    if len(liste) == 0:
        return 0
    else:
        return liste[0]+somme(liste[1:])
    
listeNBR = [1, 43,4,6,5,22]

print(somme(listeNBR))