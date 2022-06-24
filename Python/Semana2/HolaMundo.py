print("Hola mundo desde archivo")


#Esta es una impresion en consola
print("Hola mundo desde archivo!")


#javac HolaMundo.java
#java HolaMundo

# Variable
#Espacio reservado en memoria

## Tipos de Datos

## Primitivos
# char (1 carater)
# int (tipo de dato numerico entero)
# float (tipo numerico con punto decimal)
# double (tipo numerico con punto decimal largo a)
# boolean  true-false (1-0)
# decimal (tipo numerico con punto decimal fraccionarios)

##Especiales

# string (cadena de caracteres)
# Pilas
# Listas
# Arreglos
# Listas Ligadas


# Python NO es un lenguaje fuertemente tipeado, es decir,
# cuando yo creo una variable esta aun NO sabe que va a recibir


## Variable en JAVA String nombre;

nombre = "Paola"

edad = 10

print(nombre)
print(edad)

# (int) nombre = 5

##Nombres funcionales de las variables

var1 = 5
variable_1 = 6
VARIABLE = "HOLI"  # Variable de tipo constante
_variable = 1
#3_variable = 5  NO se puede iniciar el nombre de una variable con un numero
#variable-1 = 5  NO se puede usar - en nombre de variables
#var 1 = 5 NO se puede dejar espacios en los nombres de las variables
#"var 1" Aqui no aplica


numerica = int(1000)
flotante = float(1000.56)
cadena = str(1000)
complejo = 1j

print(numerica)
print(flotante)
print(cadena)
print(complejo)

## Verficar la diferencia de tipos

print(type(numerica))
print(type(cadena))


#Casteo de tipo de tipo de datos

casteado = int(flotante)
print(casteado)
print()

print(type(casteado))


print("Hola")
print('hola')


nombre_completo = "Paola Sanchez"
apellido = nombre_completo[6:13]

print(apellido)


## TRUE - FALSE

print(10 == 10)
print(100 == 10)
print(100 > 10)
