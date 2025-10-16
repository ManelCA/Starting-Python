import os
os.system("cls")

# Creación de listas
print("\n Crear listas")
lista1: list[int] = [1, 2, 3, 4, 5]  # lista de enteros
lista2: list[str] = ["Manzanas", "Peras", "Plátanos"]  # Lista de cadenas
lista3 = [1, "Hola", 3.14, False]  # Lista de tipos mixta

lista_vacia = []
lista_de_listas = [[1, 2], [3, 4]]
matriz = [[1, 2], [2, 3], [4, 5]]

print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_listas)
print(matriz)

# Acceso a elementos por índice
print("\n Acceso a elementos por índice")
print(lista2[0])  # Manzanas
print(lista2[1])  # Peras
print(lista2[-1])  # Plátanos
print(lista2[-2])  # Peras

print(lista_de_listas[1][0])

# Slicing (rebanado)

print(lista1[1:4])
print(lista1[:3])
