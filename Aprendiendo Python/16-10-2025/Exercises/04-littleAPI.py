# Método para limpiar la consola en cualquier sistema operativo
import os


def cleanConsole():
    # Si el sistema operativo es Windows, usa 'cls, si no, usará 'clear'
    # os.name devuelve 'nt' en windows y 'posix' en Linux/Mac
    os.system("cls" if os.name == "nt" else "clear")


cleanConsole()
