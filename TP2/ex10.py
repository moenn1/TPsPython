
res = {'a': 400, 'b': 400, 'd': 400, 'c': 300, 'h': '', 'k': '', 's': ''}
newRes = []
for i,j in res.items():
    if len(str(j)) > 0:
        newRes.append((i, j))

newRes = dict(newRes)
print(newRes)