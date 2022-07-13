class Persona:  # Clase padre
    def __init__(self, nombre, apellido_pat, apellido_mat, domicilio, tipo):
        self.nombre = nombre
        self.apellido_pat = apellido_pat
        self.apellido_mat = apellido_mat
        self.domicilio = domicilio
        self.tipo = tipo

    def imprimeDatos(self):  # Es un método constructor
        print("Esta persona se llama", self.nombre)
        print("Es un ", self.tipo)


class Alumno(Persona):  # Clase hijo
    def __init__(self, nombre, apellido_pat, apellido_mat, domicilio, tipo, numeroCuenta, carrera):
        # Accede al método constructor del padre
        super().__init__(nombre, apellido_pat, apellido_mat, domicilio, tipo)
        self.numeroCuenta = numeroCuenta
        self.carrera = carrera


class Profesor(Persona):  # Clase hijo
    def __init__(self, nombre, apellido_pat, apellido_mat, domicilio, tipo, departamento, numeroEmpledo, gradoAcademico):
        super().__init__(nombre, apellido_pat, apellido_mat, domicilio, tipo)
        self.departamento = departamento
        self.numeroEmpleado = numeroEmpledo
        self.gradoAcademico = gradoAcademico

    def darClase(self):
        print("El profesor está dando clase")


p1 = Profesor("Paola", "Sanchez", "Castillo", "Cdmx",
              "Profesor", "Sistemas", 56784, "Licenciatura")

p2 = Alumno("Manuel", "Enriquez", "Pineda",
            "EdoMex", "Alumno", 123432, "Full stack React")

p1.darClase()

#Creando un objeto (instancia)
persona1 = Persona("Paola", "Sanchez", "Castillo", "Rosa Carmesí1", "Profesor")

persona2 = Persona("Manuel", "Enriquez", "Pineda", "EdoMex", "Alumno")

print("Objeto (Persona) 1")
print("Esta persona es : ", persona1.nombre)
print("Su tipo  : ", persona1.tipo)

print("Objeto (Persona) 2")
print("Esta persona es : ", persona2.nombre)
print("Su tipo  : ", persona2.tipo)
