# Función para calcular la nota media de un alumno
def calcular_media(notas):
    if notas:
        return sum(notas) / len(notas)
    else:
        return 0

# Pedir al usuario el número de alumnos
num_alumnos = int(input("Ingrese el número de alumnos: "))

# Crear un diccionario para almacenar los nombres y notas de los alumnos
alumnos = {}

# Pedir el nombre y notas de cada alumno
for _ in range(num_alumnos):
    nombre = input("Ingrese el nombre del alumno: ")
    
    # Verificar si el alumno ya existe en el diccionario
    if nombre in alumnos:
        print("Error: ¡El alumno ya existe en la lista!")
        continue
    
    notas = []
    while True:
        nota = float(input(f"Ingrese la nota del alumno {nombre} (ingrese un número negativo para terminar): "))
        if nota < 0:
            break
        notas.append(nota)
    
    # Agregar el nombre y las notas al diccionario de alumnos
    alumnos[nombre] = notas

# Mostrar la lista de alumnos y la nota media de cada uno
print("\nLista de alumnos y sus notas medias:")
for nombre, notas in alumnos.items():
    media = calcular_media(notas)
    print(f"{nombre}: Notas = {notas}, Media = {media:.2f}")
