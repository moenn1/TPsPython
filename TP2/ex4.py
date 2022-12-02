


liste1 = [1, 4,3 ,3,13,49]


liste2 = [1, 2,3 ,3,1,9]

common = False

for i in liste1:
    for j in liste2:
        if i == j:
            common = True
            break
    if common == True:
        break
    
if common == True:
        print("True")
else:
        print("False")