
liste = [1,3,'a',1,1,'a'] 
res = {}

for i in liste:
    if i not in res:
        res[i] = liste.count(i)
        
print(res)