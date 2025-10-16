# Operadores lógicos
age = int(input("¿Cuantos años tienes? \n"))

have_carnet = input("¿Tienes carnet, Sí(S), No,(N)? \n")

if have_carnet.upper() == "S":
    have_carnet = True
else:
    have_carnet = False

if age >= 18 and have_carnet:
    print("Puedes conducir")
else:
    print("No puedes conducir")

# Negacion en las condiciones
# not -> !
if not have_carnet:
    print("Para sacarte el carnet acuda a clases de conducir")

# Condición anidada
if age < 70:
    print("Debería dejar de conducir")
    if age < 80:
        print("Porfavor deje de conducir")
else:
    print("Olvidate de este condicional")
