# Solicitar la cantidad de payasos y muñecas vendidos
num_payasos = int(input("Ingrese el número de payasos vendidos: "))
num_munecas = int(input("Ingrese el número de muñecas vendidas: "))

# Calcular el peso total del paquete que será enviado
peso_payasos = num_payasos * 112
peso_munecas = num_munecas * 75
peso_total = peso_payasos + peso_munecas

# Mostrar el peso total del paquete
print("El peso total del paquete que será enviado es:", peso_total, "gramos")
