import random
import time
import os
#Ejercicio 2
#El jugador debe competir contra la “banca” en varias rondas.
#En cada ronda, se reparten cartas (valores aleatorios entre 1 y 13, 
#como en una baraja francesa sin palos).
#El jugador elige si quiere jugar la ronda o retirarse. 
#Gana la ronda si su carta es mayor que la de la banca. El juego termina
#cuando:El jugador pierde 3 veces, gana 5 veces o decide retirarse.

def asignacionDeCarta(respuesta):
    os.system('cls')
    if respuesta == "si":
        cartaJugador= random.randint(1, 13)
        cartaBanca=random.randint(1,13)
        print(f"Esta es tu carta {cartaJugador}")
        time.sleep(1)
        print(" ")
        
    return cartaBanca,cartaJugador

def comenzarJugar():
    desicion=input("""Deseas jugar 
        1.Si
        2.NO
        3.retirarte: """).lower()
    print(" ")
    if desicion == "1" or desicion == "si":
        return desicion
    elif desicion == "2" or desicion == "no":
        return desicion
    else:
        return desicion



def jugar(desicion,cartaBanca,cartaJugador,bancaVictorias,jugadorVictorias):
    if desicion == "1" or desicion == "si":
        if cartaBanca > cartaJugador:
            bancaVictorias +=1
            print("Has perdido")
            print(f"Esta era la carta de la banca {cartaBanca}")
            print(" ")
            print(" ")
            print(f"Victorias de la banca:{bancaVictorias}        |        Victorias del jugador:{jugadorVictorias}")
            print(" ")
            time.sleep(5)


        else:
            print(f"Esta era la carta de la banca {cartaBanca}")
            jugadorVictorias +=1
            print(f"Has ganado {jugadorVictorias} rondas")
            print(" ")

            print(" ")
            print(f"Victorias de la banca:{bancaVictorias}        |        Victorias del jugador:{jugadorVictorias}")
            print(" ")
            time.sleep(5)

            
    elif desicion == "no" or desicion == "2":
        print(f"Esta era la carta de la banca {cartaBanca}")
        print(" ")
        print(f"Victorias de la banca:{bancaVictorias}        |        Victorias del jugador:{jugadorVictorias}")
        print(" ")
        time.sleep(5)
        
    else:
        print("TE HAS RETIRADO")
    return desicion,bancaVictorias,jugadorVictorias
        


def volverJugar():
    desicion=input("""Deseas volver jugar 
        1.Si
        2.NO: """).lower()
    print(" ")
    if desicion == "1" or desicion == "si":
        return desicion
    else:
        bienvenida="no"
        return bienvenida
    
print("hola bienvenido al casino desea jugar")
print(" ")
print("""El jugador debe competir contra la “banca” en varias rondas.
En cada ronda, se reparten cartas (valores aleatorios entre 1 y 13, 
como en una baraja francesa sin palos).
El jugador elige si quiere jugar la ronda o retirarse. 
Gana la ronda si su carta es mayor que la de la banca. El juego termina
cuando:El jugador pierde 3 veces, gana 5 veces o decide retirarse.""")
print(" ")
bancaVictorias=0
jugadorVictorias=0
volver="1"
bienvenida=input("si o no: ").lower()
while bienvenida == "si" and volver =="1" or volver =="si":
    cartaBanca, cartaJugador = asignacionDeCarta(bienvenida)
    desicion=comenzarJugar()
    if desicion=="3" or desicion=="retirarse":
        print("TE HAS RETIRADO")
        break 
    resultado,bancaVictorias,jugadorVictorias=jugar(desicion,cartaBanca,cartaJugador,bancaVictorias,jugadorVictorias)
    if bancaVictorias == 3:
        print("PERDISTE")
        break
    if jugadorVictorias == 5:
        print("GANASTE")
        break
    volver=volverJugar()
    

print(f"Has ganado {jugadorVictorias} rondas y has perdido {bancaVictorias} rondas")
