# Método para limpiar la consola en cualquier sistema operativo
import os


def cleanConsole():
    # Si el sistema operativo es Windows, usa 'cls, si no, usará 'clear'
    # os.name devuelve 'nt' en windows y 'posix' en Linux/Mac
    os.system("cls" if os.name == "nt" else "clear")


cleanConsole()
num1 = float(input("Inserte un número \n"))
num2 = float(input("Inserte otro número \n"))
operator = input(
    "¿ Que quiere hacer: Sumar(+), Restar(-), Dividir(/), Multiplicar(*) ?\n")

# Declaramos la función que va a recibir por parámetro 3 valores
# El primer número, el segundo número y el operador


def calculator(num1, num2, operator):
    try:
        if operator == "+":
            print(f"El resultado de la suma es: {num1 + num2}")
        elif operator == "-":
            print(f"El resultado de la resta es: {num1 - num2}")
        elif operator == "*":
            print(f"El resultado de la multiplicación es: {num1 * num2}")
        elif operator == "/":
            print(f"El resultado de la división es: {num1 / num2:.2f}")
        else:
            print("Resultado Indefinido")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre 0")


calculator(num1, num2, operator)
