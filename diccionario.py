# Creamos un diccionario para almacenar los artículos y sus precios
cesta_compra = {}

# Función para calcular el costo total de la compra
def calcular_costo_total(cesta):
    total = sum(cesta.values())
    return total

# Ciclo para añadir artículos a la cesta
while True:
    articulo = input("Ingrese el artículo (o escriba 'terminar' para finalizar): ")
    
    # Si el usuario escribe 'terminar', salimos del ciclo
    if articulo.lower() == 'terminar':
        break
    
    precio = float(input(f"Ingrese el precio de '{articulo}': "))
    
    # Añadimos el artículo y su precio a la cesta de compra
    cesta_compra[articulo] = precio

# Mostramos la lista de la compra y el costo total
print("\nLista de la compra:")
for articulo, precio in cesta_compra.items():
    print(f"{articulo}: ${precio}")

total = calcular_costo_total(cesta_compra)
print(f"\nCosto total: ${total:.2f}")
