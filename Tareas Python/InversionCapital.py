# Preguntar al usuario la cantidad a invertir, el interés anual y el número de años
cantidad_invertida = float(input("Ingresa la cantidad a invertir: "))
interes_anual = float(input("Ingresa el interés anual en porcentaje: "))
años = int(input("Ingresa el número de años: "))

# Calcular el capital obtenido en la inversión
capital_obtenido = cantidad_invertida * (1 + (interes_anual / 100)) ** años

# Mostrar el capital obtenido en la inversión
print("El capital obtenido en la inversión es de:", round(capital_obtenido, 2))
