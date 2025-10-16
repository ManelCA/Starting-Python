nombre = input("Hola, ¿Como te llamas?\n")
print(f"Hola {nombre}, encantado de conocerte")

age = int(input("Cuantos años tienes \n"))
print(f"Dentro de 20 años tendrás {age + 20}")

# Obtener multiples valores a la vez
country, city = input("¿En que país y ciudad resides \n?").split()

print(f"Vives en {country.upper()}, {city}")
