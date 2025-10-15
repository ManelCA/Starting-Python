# Conversor de temperaturas

# f"{temperatura}" es para usar la variable dentro del print y convertirlo a float
# :.2f es lo mismo dentro del print pero lo convierte a float y mostrará dos decimales

temp = input("Ingrese la temperatura del lugar donde reside: ")
temperatura = float(temp)

dato = input("¿La temperatura ingresada está en Fahrenheit (F) o Celsius (C)? ")

if dato.upper() == "F":
    # Convertir de Fahrenheit a Celsius
    celsius = (temperatura - 32) * 5/9
    print(f"{temperatura}°F equivalen a {celsius:.2f}°C")
elif dato.upper() == "C":
    # Convertir de Celsius a Fahrenheit
    fahrenheit = (temperatura * 9/5) + 32
    print(f"{temperatura}°C equivalen a {fahrenheit:.2f}°F")
else:
    print("Introduzca un tipo de temperatura válido: F o C.")
