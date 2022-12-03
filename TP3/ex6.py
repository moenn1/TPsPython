

def fact1(n):
    f = 1
    while n>1:
        n -= 1
        f += f*n
    return f

def fact2(n):
    if n < 2:
        return n
    else:
        return fact2(n-1)*n

fact3 = lambda n : n if n < 2 else n*fact3(n-1)

print(fact1(4))
print(fact2(4))
print(fact3(4))
