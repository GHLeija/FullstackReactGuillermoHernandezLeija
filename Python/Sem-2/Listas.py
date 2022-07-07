## ejemplo de listas en python

#Creando una lista
#nombres = ["Paola", "Carlos", "Mario", "Israel", "Manuel", "Luis", "Guillermo"]

# Accediendo a una posición o un elemento de la lista
#print(nombres[1])

# Cambiando un elemento con x posicion en la lista
#nombres[0] = "Elizabeth"

# Agregar elementos a la lista

#nombres.insert(7, "Juan")
#nombres.insert(1, "Pedrita")

#nombres.append("Perenganita")
##nombres.("sutanita")

#print(nombres)

# Despues de dos meses

#nombres.remove("Juan")


#Barrer una lista
#Para barrer una lista, se requiere un loop
#FOR
#WHILE
#DO-WHILE
#FOREACH


#for x in nombres:
#    print(x)


#nombres.pop(1)

#print(nombres)


#for y in range(1):
#    print(nombres[y])

#print(len(nombres))


#nombres = ["Paola", "Carlos", "Mario", "Israel", "Manuel", "Luis"]

## While

#i = 0
#while 1 < len(nombres):
#    print(nombres[i])
#    i = i + 1

#Las listas son estructuras especiales de datos

#se pueden utilizar diferentes métodos

nombres = ["Paola", "Carlos", "Mario", "Israel",
           "Manuel", "Luis", "Guillermo", "David"]

#Imprime toda lista ordenada de forma ascendente
# nombres.sort()
# print(nombres)

# #Imprime por la longitud de la cadena
# nombres.sort(key=len)
# print(nombres)

# #Imprime la lista de forma descendente
# nombres.sort(reverse=True)
# print(nombres)

# #Imprime por la longitud de la cadena, en froma descendente.
# nombres.sort(key=len, reverse=True)
# print(nombres)

nombres = ["Paola", "Carlos", "Mario", "Israel",
           "Manuel", "Luis", "Guillermo", "David"]


# Se hacen copias de la original, se utilizan las copias.
#Sorted es un método que recibe algo y lo ordena
alfabetico = sorted(nombres.copy())
keys = nombres.copy()
reversas = nombres.copy()

print(alfabetico)
print(keys)
print(reversas)
