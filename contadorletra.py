frase = input("por favor ingrese una frase")
letra = input("por favor ingresar la letra a buscar")
cletra = 0

for i in frase:
    if i == letra:
        cletra += 0


print("la letra '%s'aparece %2i en la frase '%s', "%(letra,cletra,frase))