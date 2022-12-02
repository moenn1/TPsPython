

ids=[1,2,3]
noms=['Mohamed' , 'Ahmed', 'Karima' ]
tels=['0612344567' , '0734565658' ,'0612345610']
res = {}

for i in range(len(ids)):
    dict1 = {}
    dict1[noms[i]] = tels[i]
    res[ids[i]] = dict1

print(res)