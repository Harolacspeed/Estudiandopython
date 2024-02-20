# Definimos el diccionario con los precios de las frutas
precios_frutas = {
    "manzana": 2,
    "banana": 1.5,
    "naranja": 1.8,
    "pera": 2.2,
    "uva": 3
}

# Función para calcular el precio total de la fruta vendida
def calcular_precio(fruta, cantidad):
    if fruta in precios_frutas:
        precio_unitario = precios_frutas[fruta]
        precio_total = precio_unitario * cantidad
        print(f"El precio total de {cantidad} {fruta}(s) es: ${precio_total}")
    else:
        print("Lo siento, esa fruta no está en el diccionario.")

# Ciclo principal del programa
while True:
    # Pedimos al usuario que ingrese el nombre de la fruta y la cantidad vendida
    fruta = input("Ingrese el nombre de la fruta vendida: ").lower()
    cantidad = int(input("Ingrese la cantidad vendida: "))
    
    # Calculamos el precio total y lo mostramos
    calcular_precio(fruta, cantidad)
    
    # Preguntamos al usuario si quiere hacer otra consulta
    respuesta = input("¿Quiere hacer otra consulta? (Sí/No): ").lower()
    if respuesta != "si":
        break
