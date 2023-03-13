edad = int(input("¿Cuál es tu edad? "))
ingresos = float(input("¿Cuáles son tus ingresos mensuales? "))

if edad >= 18 and ingresos > 1000:
    print("Tienes que tributar.")
else:
    print("No tienes que tributar.")
