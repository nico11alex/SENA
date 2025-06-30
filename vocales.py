#Escribir un programa que pida al usuario
#una palabra y muestre por pantalla el número
#de veces que contiene cada vocal.

print("Bienvenido a este programa")
palabra=input("Ingrese una palabra: ")
vocales=["a","e","i","o","u"]
contador=0

for i in vocales:
    contador=0
    for j in range(0,len(palabra)):
        if i == palabra[j]:
            contador +=1
    print(f"La vocal {i} se repite {contador}")