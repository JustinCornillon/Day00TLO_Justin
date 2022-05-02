n = int(input("Quel table souhaitez vous afficher ? :"))
print("La table de : ", n, " est :")
for i in range(1,10):
    print(i , " x ", n, " = ", i*n)