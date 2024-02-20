# Definir la lista
lista = []

# Función para mostrar el menú
def mostrar_menu():
    print("\nMENU:")
    print("1. Añadir número a la lista")
    print("2. Añadir número de la lista en una posición")
    print("3. Longitud de la lista")
    print("4. Eliminar el último número")
    print("5. Eliminar un número")
    print("6. Contar números")
    print("7. Posiciones de un número")
    print("8. Mostrar números")
    print("9. Salir")

# Función para añadir un número al final de la lista
def agregar_numero():
    num = int(input("Por favor ingrese el número que desea agregar a la lista: "))
    lista.append(num)
    print(f"El número {num} ha sido añadido a la lista.")

# Función para añadir un número en una posición específica de la lista
def agregar_en_posicion():
    num = int(input("Por favor ingrese el número que desea agregar a la lista: "))
    posicion = int(input("Por favor ingrese la posición donde desea añadir el número (a partir de 1): "))
    
    if 1 <= posicion <= len(lista) + 1:
        lista.insert(posicion - 1, num)
        print(f"El número {num} ha sido añadido en la posición {posicion} de la lista.")
    else:
        print("La posición ingresada está fuera del rango válido.")

# Función para mostrar la longitud de la lista
def longitud_lista():
    print(f"La longitud de la lista es: {len(lista)}")

# Función para eliminar el último número de la lista
def eliminar_ultimo_numero():
    if lista:
        ultimo_num = lista.pop()
        print(f"El último número de la lista ({ultimo_num}) ha sido eliminado.")
    else:
        print("La lista está vacía, no hay elementos para eliminar.")

# Función para eliminar un número de la lista según la posición
def eliminar_numero():
    if lista:
        posicion = int(input("Por favor ingrese la posición del número que desea eliminar (a partir de 1): "))
        if 1 <= posicion <= len(lista):
            numero_eliminado = lista.pop(posicion - 1)
            print(f"El número {numero_eliminado} en la posición {posicion} ha sido eliminado de la lista.")
        else:
            print("La posición ingresada está fuera del rango válido.")
    else:
        print("La lista está vacía, no hay elementos para eliminar.")

# Función para contar la cantidad de veces que aparece un número en la lista
def contar_numeros():
    if lista:
        num = int(input("Por favor ingrese el número que desea contar en la lista: "))
        cant_apariciones = lista.count(num)
        print(f"El número {num} aparece {cant_apariciones} veces en la lista.")
    else:
        print("La lista está vacía, no hay elementos para contar.")

# Función para obtener las posiciones de un número en la lista
def posiciones_numero():
    if lista:
        num = int(input("Por favor ingrese el número del que desea conocer las posiciones en la lista: "))
        posiciones = [i + 1 for i, n in enumerate(lista) if n == num]
        if posiciones:
            print(f"El número {num} está en las posiciones:", posiciones)
        else:
            print(f"El número {num} no está en la lista.")
    else:
        print("La lista está vacía, no hay elementos para buscar.")

# Función para mostrar todos los números de la lista
def mostrar_numeros():
    if lista:
        print("Los números de la lista son:")
        for numero in lista:
            print(numero)
    else:
        print("La lista está vacía, no hay elementos para mostrar.")

# Ciclo principal del programa
while True:
    mostrar_menu()
    opcion = input("Por favor seleccione una opción del menú (1-9): ")

    if opcion == "1":
        agregar_numero()
    elif opcion == "2":
        agregar_en_posicion()
    elif opcion == "3":
        longitud_lista()
    elif opcion == "4":
        eliminar_ultimo_numero()
    elif opcion == "5":
        eliminar_numero()
    elif opcion == "6":
        contar_numeros()
    elif opcion == "7":
        posiciones_numero()
    elif opcion == "8":
        mostrar_numeros()
    elif opcion == "9":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor seleccione una opción del menú (1-9).")


