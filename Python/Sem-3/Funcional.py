## Formas de descomposición de problemas

## Declarar una función
def impresion():
    print("Hola")


impresion()

#
#def saludo(nombre):
#    print("Hola " + nombre)


#saludo(4)

## Solución  1

def suma(num1, num2):
    resultado = str(num1 + num2)
    print("El resultado es " + resultado)


suma(1, 4)

#Entrada de datos
print("Hola, ¿Cuál es tu nombre?")
nombre = input()
print("Hola " + nombre + " gusto en conocerte")
