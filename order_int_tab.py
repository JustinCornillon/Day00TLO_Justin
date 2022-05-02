import random

def trier(liste):
    while liste:
        min=liste[0]
        for i in liste:
            if i < min:
                min = i
        liste.remove(min)
        x.append(min)
    return x

list_random = [random.randrange(1,100) for i in range(15)]
x=[]
trier (list_random)
print (x)

