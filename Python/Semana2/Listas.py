## ejemplo de listas en python

#Creando una lista
nombres = ["Paola", "Carlos", "Mario", "Israel", "Manuel", "Luis", "Guillermo"]

# Accediendo y pintando un elemento con x posicion de la lista
print(nombres[1])

# Cambiando un elemento con x posicion en la lista
nombres[0] = "Elizabeth"

# Agregar elementos a la lista

nombres.insert(7, "Juan")
nombres.insert(1, "Pedrita")

nombres.append("Perenganita")
##nombres.("sutanita")

print(nombres)

# Despues de dos meses

nombres.remove("Juan")


#Barrer una lista
#Para barrer una lista, se requiere un loop
#FOR
#WHILE
#DO-WHILE
#FOREACH


for x in nombres:
    print(x)


nombres.pop(1)

print(nombres)


for y in range(1):
    print(nombres[y])

print(len(nombres))


nombres = ["Paola", "Carlos", "Mario", "Israel", "Manuel", "Luis"]

## While

i = 0
while 1 < len(nombres):
    print(nombres[i])
    i = i + 1
