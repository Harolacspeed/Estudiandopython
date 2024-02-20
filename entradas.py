#definimos la edad (int)numero
Edad=int(input( " porfavor ingrese su edad " ))
#definimos las condiciones
if Edad < 4 :
    print(" su entrada es gratis " )
elif Edad == 4  or Edad <= 18 :
    print(" su entrada cuesta 30000 " )
else:
   print(" su esntrada cuesta 50000 " )