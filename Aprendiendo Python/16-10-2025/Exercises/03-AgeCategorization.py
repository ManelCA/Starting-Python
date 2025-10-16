# Método para limpiar la consola en cualquier sistema operativo
import os


def cleanConsole():
    # Si el sistema operativo es Windows, usa 'cls, si no, usará 'clear'
    # os.name devuelve 'nt' en windows y 'posix' en Linux/Mac
    os.system("cls" if os.name == "nt" else "clear")


cleanConsole()

# En caso de que el usuario no inserte el valor que queremos usamos el try
try:
    age = int(input("¿Qué edad tiene usted? \n"))
except ValueError:
    print("Por favor, introduzca un número válido.")
    exit()  # Finaliza el programa para evitar seguir con un valor inválido


def ageCategorizationFunction(age):
    if age == 0 and age <= 2:
        print("Bebé")
    elif age >= 3 and age <= 12:
        print("Niño")
    elif age >= 13 and age <= 17:
        print("Adolescente")
    elif age >= 18 and age <= 65:
        print("Adulto")
    elif age >= 65:
        print("Anciano")
    else:
        print("Introduzca un número únicamente")


ageCategorizationFunction(age)
