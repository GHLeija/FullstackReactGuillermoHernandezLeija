def suma(num1, num2):
    resultado = str(num1+num2)
    print("El resultado es " + resultado)


def resta(num1, num2):
    resultado = str(num1 - num2)
    print("El resultado es " + resultado)


def multiplicacion(num1, num2):
    resultado = str(num1 * num2)
    print("El resultado es " + resultado)


def division(num1, num2):
    if(num2 == 0):
        print("No se puede hacer división entre cero")
    else:
        resultado = str(num1 / num2)
        print("El resultado es " + resultado)


print(" Escribe el primer número: ")
numero1 = int(input())
print(" Escribe el segundo número: ")
numero2 = int(input())

print(" ¿Qué quieres hacer? ")
print(" a) Suma ")
print(" b) Resta ")
print(" c) Multiplicación ")
print(" d) División ")

opcion = input()

if (opcion == "a"):
    suma(numero1, numero2)
if (opcion == "b"):
    resta(numero1, numero2)
if (opcion == "c"):
    multiplicacion(numero1, numero2)
if (opcion == "d"):
    division(numero1, numero2)
