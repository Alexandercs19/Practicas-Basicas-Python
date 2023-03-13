contraseña = "contraseña"  # contraseña guardada en la variable

contraseña_usuario = input("Introduce la contraseña: ")  # pedir la contraseña al usuario

if contraseña.lower() == contraseña_usuario.lower():  # comparar las contraseñas sin tener en cuenta mayúsculas y minúsculas
    print("La contraseña es correcta.")
else:
    print("La contraseña es incorrecta.")
