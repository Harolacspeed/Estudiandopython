cont=0
acum1=0
acum2=0
acum3=0

cantidad=int(input("personas que desea consultar "))


while cont < cantidad :
   sueldo=float(input("porfavor ingresar salario "))
   cont += 1
   acum3+=sueldo

   if sueldo >= 300000 and sueldo <= 10000000 :
       acum1 += 1

   if sueldo >= 3000000 :
 
       acum2 +=1
     


     

print("cantidad de personas que cobran entre $300.000 y $10'000.000 es ",acum1)
print("cantidad de personas que cobran mas de $3'000.000  es ",acum2)  
print("importe total en sueldos es",acum3) 
