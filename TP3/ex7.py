

def longueur(ch):
    if ch == "":
        return 0
    else:
        return longueur(ch[1:])+1
        
print(longueur('mohamed'))