# Leer la puntuación del usuario
puntuacion = int(input("Introduzca su puntuación: "))

# Determinar el nivel de rendimiento y la cantidad de dinero que recibirá
if puntuacion >= 90:
    nivel_rendimiento = "Excelente"
    dinero = 1000
elif puntuacion >= 80:
    nivel_rendimiento = "Bueno"
    dinero = 500
elif puntuacion >= 70:
    nivel_rendimiento = "Regular"
    dinero = 250
else:
    nivel_rendimiento = "Insuficiente"
    dinero = 0

# Mostrar el nivel de rendimiento y la cantidad de dinero que recibirá
print("Su nivel de rendimiento es", nivel_rendimiento)
print("Recibirá $", dinero)
