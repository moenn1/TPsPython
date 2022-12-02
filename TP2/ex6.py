


dict1 = {'a': 100, 'b': 200, 'c':300}
dict2 = {'a': 300, 'b': 200, 'd':400}

res = {}

for key, value in dict1.items():
    if key in dict2:
        res[key] = value + dict2[key]
    else: 
        res[key] = value

for key, value in dict2.items():
    if key not in dict1:
        res[key] = value    

print(res)