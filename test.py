def seuil(a) :
 v=0.1
 n=0
 while v<a :
    v=1.6*v-1.6*v*v
    n=n+1
    return n
print(seuil(0.35))