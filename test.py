def diviseurs(n:int)->list:
    liste_diviseurs = []
    for i in range(1,n+1):
        if n%i == 0:
            liste_diviseurs.append(i)
    return liste_diviseurs

def premier(n):
    if len(diviseurs(n)) == 2:
        return n
    else:
        return False, diviseurs(n)

print(premier(59))