#Suppose that a,b,c,d are all one digit numbers, a and c >= 0

equation = input("Saisir l'expression: ")
operations = []
numbers = []
operations.append(equation[2])
operations.append(equation[7])

numbers.append(equation[1]) #a
numbers.append(equation[3]) #b
numbers.append(equation[6]) #c
numbers.append(equation[8]) #d

print(equation)
print(numbers[0] + "*" + numbers[2] + " " + operations[1] + " " + numbers[0] + "*" + numbers[3] + " " + operations[0] + numbers[1] + "*" + numbers[2] + "  " + operations[0] + numbers[1] + "*" + numbers[3])


#evident

#a*c + a*d + b*c + b*d