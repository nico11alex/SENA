import os
#En una máquina expendedora, los usuarios pueden seleccionar bebidas múltiples veces:
#1. café ($3.000), 2. té ($2.500) o 3. jugo ($3.500); cada vez que el usuario ingresa una opción(1, 2, o 3),
#se muestra el valor del producto y se acumula el total a pagar;
#el programa termina cuando el usuario ingresa el número 0; usar un bucle while, match-case y break.

total=0

while True:
    print(f"Esto es lo que has gastado {total}")
    print(" ")
    print("""Estas son las bebidas que estan en la maquina expendedora
    1. café ($3.000)
    2. té ($2.500)
    3. jugo ($3.500)
    Para salir del programa presione 0""")
    eleccion=int(input("Ingrese el número de la bebida que desea: "))
    match eleccion:
        case 1:
            total += 3000
        case 2:
            total += 2500
        case 3:
            total += 3500
        case 0:
            break
    os.system('cls')    
        
print(" ")        
print(f"Este es el total de lo que compraste:{total}")