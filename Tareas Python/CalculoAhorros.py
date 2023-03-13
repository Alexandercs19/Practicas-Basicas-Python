# Solicitar al usuario la cantidad de dinero depositada en la cuenta de ahorros
ahorros = float(input("Ingrese la cantidad de dinero depositada en la cuenta de ahorros: "))

# Calcular y mostrar los ahorros tras el primer año
ahorros *= 1.04 # aumentar un 4% los ahorros
print("Los ahorros tras el primer año son: $", round(ahorros, 2))

# Calcular y mostrar los ahorros tras el segundo año
ahorros *= 1.04 # aumentar otro 4% los ahorros
print("Los ahorros tras el segundo año son: $", round(ahorros, 2))

# Calcular y mostrar los ahorros tras el tercer año
ahorros *= 1.04 # aumentar otro 4% los ahorros
print("Los ahorros tras el tercer año son: $", round(ahorros, 2))
