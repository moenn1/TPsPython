
res = {'a': 40, 'b': 50, 'd': 99, 'c': 300}

values = sorted(res.values(), reverse=True)

for i in range(3):
    print(values[i])