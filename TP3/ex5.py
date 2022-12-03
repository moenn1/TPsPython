
def diviseurs(n):
    div = []
    if n>0:
        i = 2
        while i<n:
            if n % i == 0:
                div.append(i)
            i += 1
        return div
    else:
        return None
    
def nbDiviseurs(n):
    return len(diviseurs(n))


def premier(n):
    if nbDiviseurs(n) > 0:
        return False
    else:
        return True

def facteursPremiers(n):
    return [i for i in diviseurs(n) if premier(i)]



