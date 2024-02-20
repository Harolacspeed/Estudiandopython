n = int(input("ingrese  # de empleados"))
cont = 0
cont1 = 0
gasto = 0

for ini in range(n):
    sueldo = float(input("ingresar el valor sueldo del empleado"))
    gasto =gasto+sueldo

    if sueldo >= 1300000 and sueldo <=3000000:
       cont +=1

    elif sueldo > 3000000:
        cont1 +=1

print("los gastos de la empresa total ",gasto)
print("empleados que ganan entre 1300000 y 3000000 son:",cont)
print("empleados que ganan mas de 3000000 son:",cont1)
