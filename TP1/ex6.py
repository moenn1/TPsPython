
print("Saisir 2 nombres entiers: ")

a, b = input().split()

a = int(a)
b = int(b)

somme = a+b
print("Somme: " + str(somme))
diff = a-b
print("Difference: " + str(diff))
produit = a*b
print("Produit: " + str(produit))
if(b!=0):
    quotient = a/b
    print("Quotient: " + str(quotient))