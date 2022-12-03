


def binaire(n):
    if n < 2:
        print(int(n), end="")
    else:
        binaire(n/2)
        print(int(n%2), end="")
        
        
binaire(30)