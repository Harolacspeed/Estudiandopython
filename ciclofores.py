
edadM=0
edadT=0
edadN=0
promeM=0
promeT=0
promeN=0

for ini in range(6):

    EstudMañana=int(input("porfavor ingresar la edad de los estudiantes de la mañana"))
 
    edadM=edadM+EstudMañana


   
for ini  in range(7):

    EstudTarde=int(input("porfavor ingresar la edad de los estudiantes de la tarde"))

    edadT=edadT+EstudTarde


for ini in range(12):

    EstudNoche=int(input("porfavor ingresar la edad de los estudiantes de la noche"))
 
    edadN=edadN+EstudNoche


promeM=edadM/6

promeT=edadT/7

promeN=edadN/12


if promeM > promeT and promeN:
    print("los de la mañana tiene el mayor promedio de edades")

elif promeT> promeN and promeM:
    print("los de la tarde tiene el mayor promedio de edades")

elif promeN > promeM and promeT:
    print("los de la mañana tiene el mayor promedio de edades")


print("el promedio de edad de la mañana son",promeM)
print("el promedio de edad de la tarde son",promeT)
print("el promedio de edad de la noche son",promeN)