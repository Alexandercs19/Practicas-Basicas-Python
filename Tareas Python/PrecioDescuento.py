# Pedir al usuario que ingrese el número de barras vendidas que no son del día
num_barras_vendidas = int(input("Ingrese el número de barras vendidas que no son del día: "))

# Definir las constantes del programa
PRECIO_HABITUAL = 3.0  # Precio de una barra de pan fresca
DESCUENTO_NO_FRESCA = 0.5  # Descuento en el precio para barras no frescas

# Calcular el precio de una barra no fresca y el costo total de las barras vendidas
precio_no_fresca = PRECIO_HABITUAL * (1 - DESCUENTO_NO_FRESCA)
costo_total = num_barras_vendidas * precio_no_fresca

# Mostrar el resultado al usuario
print("El precio habitual de una barra de pan es:", PRECIO_HABITUAL)
print("El descuento por no ser fresca es:", DESCUENTO_NO_FRESCA)
print("El costo total de", num_barras_vendidas, "barras no frescas es:", costo_total)
