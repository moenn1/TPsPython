listeNat = [1, 4, 53, 32, 8, 9]
diviseurs = []
for i in listeNat:
    j = 2
    div = []
    while(j<i):
        if(i%j == 0):
            #print(str(j) + " est un diviseur de "+ str(i))   
            div.append(j)
        j += 1
    diviseurs.append(div)
    
print(diviseurs)