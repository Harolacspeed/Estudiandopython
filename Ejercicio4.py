cont =0
acum = 0

cantidad=int(input("catidad de alturad que decea consultar promedio"))

while cont < cantidad :

    num=float(input("ingresar altura en centimetros"))

    acum=acum+num

    cont += 1

    promedio = acum/cantidad

else:
    print("el promedio de las alturas es:",promedio)

