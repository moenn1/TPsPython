import math

def calculerDelta(a,b,c):
    return b**2-4*a*c

def resoudreEq(a,b,c):
    delta = calculerDelta(a, b, c)
    if delta < 0:
        print("No solutions")
    elif delta == 0:
        x1 = (-b-math.sqrt(delta))/(2*a)
        print("1 solution: x1 = " + str(x1))
    else:
        x1 = (-b-math.sqrt(delta))/(2*a)
        x2 = (-b+math.sqrt(delta))/(2*a)
        print("2 solutions: x1 = " + str(x1) + "\nx1 = "+str(x2))
        
        
resoudreEq(3, 10, 4)