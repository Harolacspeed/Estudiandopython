# Juego de dados 
import random
#Funcion aplicar numero alazar dado
Numero1=random.randint(1,6)
Numero2=random.randint(1,6)

def saludo():
    print("bienvenidos a un juego de azar con dados")
# definiendo los jugadores
def jugador1():
    print(" Jugador Alvaro ")
def jugador2():
    print(" Jugadora Barbara ")
# condiciones de los jugadores
    if Numero1 > Numero2 :
        print(f" Felicidades has ganado Alvaro con el numero ! : {Numero1} ")
        print(f" Barbara tu numero es : {Numero2} ")
    elif Numero2 > Numero1 :
        print(f"Felicidades has ganado Barbara con el numero ! : {Numero2} ")
        print(f" Alvaro tu numero es : {Numero1} ")
    else:
        Numero1 == Numero2 
        print("Felicidades Ambos an quedado empatados ")
        print(f"Alvaro su numero es: {Numero1} ")
        print(f"Barbara su numero es: {Numero2} ")
#llamando a las funciones
saludo()
jugador1()
jugador2()