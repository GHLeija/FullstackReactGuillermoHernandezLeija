## Formas de descomposición de problemas

## Declarar una función
# def impresion():
#     print("Hola")


# impresion()

#
#def saludo(nombre):
#    print("Hola " + nombre)


#saludo(4)

## Solución  1

#def suma(num1, num2):
#     resultado = str(num1 + num2)
#     print("El resultado es " + resultado)


# suma(1, 4)

#Entrada de datos
# print("Hola, ¿Cuál es tu nombre?")
# nombre = input()
# print("Hola " + nombre + " gusto en conocerte")

print("*** Operación a elegir ***")
print("Operaciones que puede realizar:\"+,-,*,/\"")


def operacion():
    num1 = int(input("Ingrese un valor entero: "))
    num2 = int(input("Ingrese otro valor entero: "))
    operacion = input("Seleccione la operación: ")


if operacion == '+':
    print("La suma es: ", num1 + num2)
elif operacion == '-':
    print("La resta es: ", num1 - num2)
elif operacion == '*':
    print("La multiplicación es: ", num1 * num2)
else:
    if num2 != 0:
        print("La división es: ", num1/num2)
    else:
        print("La operación no se puede realizar debido a que el divisor es 0")

operacion()
