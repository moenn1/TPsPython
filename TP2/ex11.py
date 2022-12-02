

dict1={'Maths':12, 'PC':18, 'Informatique':16}
dictSorted = []
sorted_values = sorted(dict1.values()) # Sort the values
sorted_dict = {}

for i in sorted_values:
    for k in dict1.keys():
        if dict1[k] == i:
            sorted_dict[k] = dict1[k]

print(sorted_dict)