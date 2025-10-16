# Método para limpiar la consola en cualquier sistema operativo
import os


def cleanConsole():
    # Si el sistema operativo es Windows, usa 'cls, si no, usará 'clear'
    # os.name devuelve 'nt' en windows y 'posix' en Linux/Mac
    os.system("cls" if os.name == "nt" else "clear")


cleanConsole()

try:
    year = int(input("Introduzca un año \n"))
except ValueError:
    print("Ingrese un año válido")
    exit()


def leapYearFunction(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print("Es año Bisiesto")
    else:
        print("No es año Bisiesto")


leapYearFunction(year)
