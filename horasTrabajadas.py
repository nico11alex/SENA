#Determinar la cantidad de dinero que recibirá un trabajador por concepto de las horas extras trabajadas en una empresa,
#sabiendo que cuando las horas de trabajo exceden de 40,
#el resto se consideran horas extras y que estas se pagan al doble de una hora normal cuando no exceden de 8;
#si las horas extras exceden de 8 se pagan las primeras 8 al doble de lo que se pagan las horas normales y el resto al triple.

pago=6200
horasTrabajadas=int(input("Ingrese la cantidad de horas trabajadas a la semana: "))
horasNormales=0
horasDobles=0
horasTriples=0

if horasTrabajadas <= 40:
    horasNormales=horasTrabajadas*6200
    print(f"Has ganado {horasNormales}")
elif horasTrabajadas > 40 and horasTrabajadas < 49:
    horasNormales= 40 *6200
    horasDobles=horasTrabajadas -40
    horasDobles = horasDobles *12400
    print(f"Has ganado {horasNormales} en horas normales")
    print(f"Has ganado {horasDobles} en horas dobles")
elif horasTrabajadas > 48:
    horasNormales= 40 *6200
    horasDobles=8*12400
    horasTriples=horasTrabajadas -48
    horasTriples = horasTriples *6200*3
    print(f"Has ganado {horasNormales} en horas normales")
    print(f"Has ganado {horasDobles} en horas extras dobles")
    print(f"Has ganado {horasTriples} en horas extras Triples")
