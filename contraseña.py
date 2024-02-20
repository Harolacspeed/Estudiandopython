#definir contraseña
password="contraseña"

#definimos el bucle para la contraseña.mientras la condicion no sea verdadera se ejecutara infinito
while True:
 contra=input("porfavor ingrese su contraseña:\n")
 if contra==password:
     print("¡contraseña correcta! . bienvenido" )
     break
 else:
    print("¡contraseña incorrecta!. vuelve a intentarlo" ) 