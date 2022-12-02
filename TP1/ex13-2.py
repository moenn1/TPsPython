
inputString = input("Saisir les entiers separés par des virgules: ")

listinit = inputString.split(",")

liste1 = []
liste2 = []
for i in listinit:
    if i not in liste1:
        liste1.append(i)

# for i in range(len(liste1)):
#     for j in range(i,len(liste1)):
#         if (int(liste1[i])>int(liste1[j])):
#             liste1[i], liste1[j] = liste1[j], liste1[i]
    

    
for i in liste1:
    liste2.append(listinit.count(i))



print(liste1)
print(liste2)