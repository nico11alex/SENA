import random
import time
import os
rondas=int(input("Cuantas rondas desea jugar: "))
opciones=["piedra","papel","tijera"]
maquina=0
usuario=0

for i in range(0,rondas):
    eleccion=input("Escoge piedra, papel o tijera: ").lower()
    print(" ")
    time.sleep(3)
    eleccionRandom=opciones[random.randint(0,2)]
    print(f"la maquina escogio {eleccionRandom}")
    if eleccion=="piedra" and eleccionRandom=="tijera" or eleccion=="papel" and eleccionRandom=="piedra" or eleccion=="tijera" and eleccionRandom=="papel":
        print("GANASTE")
        usuario+=1
    elif eleccion==eleccionRandom:
        print("EMPATE")
    else:
        print("PERDISTE")
        maquina+=1
    time.sleep(3)
    os.system('cls')
        
if usuario>maquina:
    print(f"Ganaste más rondas")
    print(f"rondas ganadas {usuario} y rondas perdidas {maquina}")
elif usuario==maquina:
    print(f"EMPATASTE")
    print(f"rondas ganadas {usuario} y rondas perdidas {maquina}")
else:
    print(f"Perdiste más rondas")
    print(f"rondas ganadas {usuario} y rondas perdidas {maquina}")