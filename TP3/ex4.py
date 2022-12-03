
def maxAB(a,b):
    if a>b:
        return a
    return b

def maxListe(listeNombres):
    maxNbr = -1
    for i in listeNombres:
        maxNbr = maxAB(maxNbr, i)
    return maxNbr
                
listeNBR = [1, 43,4,6,5,22]

print(maxListe(listeNBR))