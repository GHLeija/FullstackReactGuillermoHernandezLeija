from tkinter.font import names


nombres = ["Paola", "Carlos", "Mario", "Israel",
           "Manuel", "Luis", "Guillermo", "David"]
#print(nombres)

#print(nombres[6])

#print(nombres[6])
#index = nombres.index("Guillermo")
#print(index)

i = 0

while i < len(nombres):
  if "Guillermo" == nombres[i]:
    print("Te encontré :  ", nombres[i])
    print("La posición es:  ",  i)
    break

i = i + 1
