#definimos el valor a ingresar(float)decimales
Factura=float(input("Porfavor ingresar el valor de su factura : " ))
iva=input("¿Decea aplicar el iva? (SI o NO) : ")

if iva.lower() == "no" :
    Factura += Factura * 0.21
    print("automaticamente se aplicara iva  de 21 % " )
elif iva.lower() == "si" : 
    iva_personalizado =float(input("porfavor digite el iva que decea solicitar : "))
    Factura += Factura *(iva_personalizado/100)
    
print(f"este es el total de la factura con el iva incluido: {Factura} " )
    

