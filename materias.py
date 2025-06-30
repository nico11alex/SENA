import os
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
#pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas.
#Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

materias=[]
notas=[]
posicion=0
numMaterias=1
print("Hola bienvenido a este programa")

lasMaterias=int(input("Ingrese cuantas materias presento: "))

for i in range(0,lasMaterias):
    os.system('cls')
    ingresoMaterias=input(f"Ingrese la materia {numMaterias}:")
    ingresenota=float(input(f"Ingrese la nota de {ingresoMaterias}:"))
    if ingresenota < 3.0:
        materias.append(ingresoMaterias)
        notas.append(ingresenota)
    numMaterias +=1
    
if len(materias)>0:
    os.system('cls')
    for i in materias:
        print(f"Debes recuperar {i} por que tu nota es de {notas[posicion]}")
        posicion +=1
else:
    print("Muchas Gracias")