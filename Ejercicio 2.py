
n = (input("Ingrese el primer nombre de pila: "))
n1 = (input("Ingrese el segundo nombre de pila: "))



nombres = [n, n1]

nombres.sort()

print("Los nombres ordenados alfabeticamente: ")
for nombre in nombres:
    print(nombre)
#Cada itineracion, imprime el nombre actual 
