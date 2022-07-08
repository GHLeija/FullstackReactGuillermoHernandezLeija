# Cuenta regresiva
def cuenta_reg(num):
    num -= 1  # pre decremente el número que entra automáticamete se le resta 1
    if num > 0:  # si llega a cero
        print(num)
        cuenta_reg(num)  # Al dejar de cumplir la condición entra al else
    else:
        print("Terminó el timer")

# Covierte el valor que está en los corchetes en una cadena
    print(f"Terminó la función + {num}")  # interpolación


cuenta_reg(5)
