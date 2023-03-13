# Pedimos al usuario que elija si quiere una pizza vegetariana o no
es_vegetariana = input("¿Quieres una pizza vegetariana? (Sí/No): ")

# Creamos una lista con los ingredientes disponibles
ingredientes = ["jamón", "pepperoni", "pollo", "cebolla", "champiñones", "pimientos", "piña"]

# Si la respuesta del usuario es Sí, mostramos un menú con los ingredientes disponibles y le pedimos que elija uno
if es_vegetariana.lower() == "sí":
    print("Ingredientes disponibles:")
    for i, ingrediente in enumerate(ingredientes):
        print(f"{i + 1}. {ingrediente}")
    eleccion = input("Elige un ingrediente (1-7): ")
    
    # Comprobamos que la elección es válida
    while eleccion not in ["1", "2", "3", "4", "5", "6", "7"]:
        eleccion = input("Elección inválida. Elige un ingrediente (1-7): ")
    
    # Creamos la pizza con los ingredientes elegidos
    pizza = ["mozzarella", "tomate", ingredientes[int(eleccion) - 1]]
    print("Has elegido una pizza vegetariana con los siguientes ingredientes:")
    print(", ".join(pizza))
    
# Si la respuesta del usuario es No, mostramos el mismo menú pero sin la opción de elegir carne
elif es_vegetariana.lower() == "no":
    print("Ingredientes disponibles:")
    for i, ingrediente in enumerate(ingredientes):
        if ingrediente in ["jamón", "pepperoni", "pollo"]:
            continue
        print(f"{i + 1}. {ingrediente}")
    eleccion = input("Elige un ingrediente (1-4): ")
    
    # Comprobamos que la elección es válida
    while eleccion not in ["1", "2", "3", "4"]:
        eleccion = input("Elección inválida. Elige un ingrediente (1-4): ")
    
    # Creamos la pizza con los ingredientes elegidos
    pizza = ["mozzarella", "tomate", ingredientes[int(eleccion) - 1]]
    print("Has elegido una pizza no vegetariana con los siguientes ingredientes:")
    print(", ".join(pizza))
    
# Si la respuesta del usuario no es ni Sí ni No, mostramos un mensaje de error
else:
    print("Respuesta inválida. Por favor, responde Sí o No.")
