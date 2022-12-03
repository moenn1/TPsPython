

def operations(a,b):
    if b != 0:
        return (a+b, a-b, a*b, a/b)
    else:
        return (a+b, a-b, a*b, 0)
    
    
print(operations(5, 4))