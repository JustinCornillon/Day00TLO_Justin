import random

def trier(liste):
    while liste:
        max=liste[0]
        for i in liste:
            if i >  max:
                max = i
        liste.remove(max)
        x.append(max)
    return x

list_random = [random.randrange(1,100) for i in range(15)]
x=[]
trier (list_random)
print (x)