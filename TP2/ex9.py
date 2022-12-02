

inputString = "ensa alhoceima"
res = {}


for i in range(len(inputString)):
    if inputString[i] not in res and inputString != ' ':
        res[inputString[i]] = inputString.count(inputString[i])


print(res)
