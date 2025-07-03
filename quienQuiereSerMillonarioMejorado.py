import random
import time
import os
preguntas={1:[{"pregunta":"¿De que color es el cielo en un dia despejado?","opciones":["A.Verde","B.Azul","C.Rojo","D.Naranja"],"respuesta":"B"},
              {"pregunta":"¿Cuántas patas tiene un perro","opciones":["A.Dos","B.Seis","C.Cuatro","D.Ocho"],"respuesta":"C"}],
           2:[{"pregunta":"¿Cuál es la capital de España?","opciones":["A.Madrid","B.Barcelona","C.Sevilla","D.Valencia"],"respuesta":"A"},
              {"pregunta":"¿Qué planeta es conocido como el (planeta rojo)?","opciones":["A.Marte","B.Venus","C.Saturno","D.Júpiter"],"respuesta":"A"}],
           3:[{"pregunta":"¿Quién escribió Cien años de soledad?","opciones":["A.Mario Vargas Llosa","B.Gabriel García Márquez","C.Isabel Allende","D.Pablo Neruda"],"respuesta":"B"},
              {"pregunta":"¿Cuántos continentes hay en la Tierra?","opciones":["A.5","B.6","C.7","D.8"],"respuesta":"C"}],
           4:[{"pregunta":"¿Qué gas es esencial para que podamos respirar?","opciones":["A.Oxígeno","B.Nitrógeno","C.Hidrógeno","D.Dióxido de carbono"],"respuesta":"A"},
              {"pregunta":"¿Cuál es el número primo más bajo?","opciones":["A.0","B.1","C.2","D.3"],"respuesta":"C"}],
           5:[{"pregunta":"¿En qué año llegó el hombre a la Luna?","opciones":["A.1965","B.1969","C.1971","D.1973"],"respuesta":"B"},
              {"pregunta":"¿Qué país tiene forma de bota?","opciones":["A.Grecia","B.Italia","C.Turquía","D.Francia"],"respuesta":"B"}],
           6:[{"pregunta":"¿Qué elemento químico tiene el símbolo (Au)?","opciones":["A.Plata","B.Aluminio","C.Oro","D.Uranio"],"respuesta":"C"},
              {"pregunta":"¿Quién pintó “La noche estrellada”?","opciones":["A.Monet","B.Picasso","C.Van Gogh","D.Da Vinci"],"respuesta":"C"}],
           7:[{"pregunta":"¿Cuál es la capital de Nueva Zelanda?","opciones":["A.Auckland","B.Wellington","C.Christchurch","D.Dunedin"],"respuesta":"B"},
              {"pregunta":"¿Cuál es la raíz cuadrada de 144?","opciones":["A.10","B.11","C.12","D.14"],"respuesta":"C"}],
           8:[{"pregunta":"¿Qué filósofo dijo “Solo sé que no sé nada”?","opciones":["A.Platón","B.Sócrates","C.Aristóteles","D.Pitágoras"],"respuesta":"B"},
              {"pregunta":"¿En qué año comenzó la Primera Guerra Mundial?","opciones":["A.1912","B.1914","C.1916","D.1918"],"respuesta":"B"}],
           9:[{"pregunta":"¿Qué científico propuso la teoría del electromagnetismo unificado?","opciones":["A.Isaac Newton","B.James Clerk Maxwell","C.Nikola Tesla","D.Albert Einstein"],"respuesta":"B"},
              {"pregunta":"¿Cuál es el país con más lenguas oficiales reconocidas?","opciones":["A.Suiza","B.Sudáfrica","C.India","D.Canadá"],"respuesta":"B"}],
           10:[{"pregunta":"¿Cuál es el nombre del satélite natural más grande de Saturno?","opciones":["A.Europa","B.Titán","C.Ganimedes","D.Encélado"],"respuesta":"B"},
              {"pregunta":"¿Qué obra musical fue compuesta por Stravinski y causó disturbios en su estreno en 1913?","opciones":["A.El lago de los cisnes","B.La consagración de la primavera","C.Carmen","D.Rapsodia en azul"],"respuesta":"B"}],   }

opciones=["1).Llamada a un amigo","2).50/50","3).Cambio de pregunta"]
level=1
ganacia=10000000
ganado=0
eleccion=["A","B","C","D"]
cambio=0
print(" ")
print("Bienvenido a el juego Quien quiere ser millonario")
print(" ")
while level < 11:   
   print("*"*100)
   print(" ")
   print(f"Estas en el nivel {level}                              Has ganado {ganado}")
   print(" ")
   print(preguntas[level][cambio]["pregunta"])
   print(" ")
   for i in preguntas[level][cambio]["opciones"]:
      print(i)  
      time.sleep(1)
   print(" ")
   if len(opciones)!=0: 
      comodin=input("Desea un comodin (si) o (no): ").upper()
      print(" ")
      if comodin=="SI":
         os.system('cls')
         print("*"*100)
         print(" ")
         for y in opciones:
            print(y)
         print(" ")
         ayuda=input("Que comodin desea: ")
         print(" ")
         if ayuda=="1" and "1).Llamada a un amigo" in opciones:
            os.system('cls')
            print("*"*100)
            print(" ")
            print(f"Estas en el nivel {level}                              Has ganado {ganado}")
            print(" ")
            opciones.remove("1).Llamada a un amigo")
            time.sleep(2)
            llamada=eleccion[random.randint(0,len(eleccion)-1)]
            print(f"La opción que te da Laura es {llamada}")
            print(" ")
            print(preguntas[level][cambio]["pregunta"])
            print(" ")
            for i in preguntas[level][cambio]["opciones"]:
                print(i)  
                time.sleep(1)
            print(" ")
            comodin=input("Desea un comodin (si) o (no): ").upper()
            print(" ")
            if comodin=="SI":
                os.system('cls')
                print("*"*100)
                print(" ")
                for y in opciones:
                    print(y)
                print(" ")
                ayuda=input("Que comodin desea: ")
                print(" ")
                if ayuda=="2" and "2).50/50" in opciones:
                    os.system('cls')
                    print("*"*100)
                    print(" ")
                    print(f"Estas en el nivel {level}                              Has ganado {ganado}")
                    print(" ")
                    opciones.remove("2).50/50")
                    eleccion.remove(preguntas[level][cambio]["respuesta"])
                    letra=eleccion[random.randint(0,len(eleccion)-1)]
                    print(" ")
                    print(preguntas[level][cambio]["pregunta"])
                    print(" ")
                    for x in preguntas[level][cambio]["opciones"]:
                        if x[0]==preguntas[level][cambio]["respuesta"] or x[0]==letra:
                            print(x)
                            time.sleep(1)
                    print(" ")
                    comodin=input("Desea un comodin (si) o (no): ").upper()
                    print(" ")
                    if comodin=="SI":
                        os.system('cls')
                        print("*"*100)
                        print(" ")
                        for y in opciones:
                            print(y)
                        print(" ")
                        ayuda=input("Que comodin desea: ")
                        print(" ")
                        if ayuda=="3" and "3).Cambio de pregunta" in opciones:
                            os.system('cls')
                            opciones.remove("3).Cambio de pregunta")
                            cambio +=1
                            print(" ")
            else:
               respuesta=input("Da la respuesta: ").upper()
               if respuesta== preguntas[level][cambio]["respuesta"]:
                    ganado=ganacia+ganado
                    print("Felicitaciones respuesta correcta")
                    time.sleep(2)
                    print(" ")
                    level+=1
                    os.system('cls')
               else:
                    print("Fallaste, haz perdido")
                    break

         elif ayuda=="2" and "2).50/50" in opciones:
            os.system('cls')
            print("*"*100)
            print(" ")
            print(f"Estas en el nivel {level}                              Has ganado {ganado}")
            print(" ")
            opciones.remove("2).50/50")
            eleccion.remove(preguntas[level][cambio]["respuesta"])
            letra=eleccion[random.randint(0,len(eleccion)-1)]
            print(" ")
            print(preguntas[level][cambio]["pregunta"])
            print(" ")
            for x in preguntas[level][cambio]["opciones"]:
               if x[0]==preguntas[level][cambio]["respuesta"] or x[0]==letra:
                  print(x)
                  time.sleep(1)
            print(" ")
            comodin=input("Desea un comodin (si) o (no): ").upper()
            print(" ")
            if comodin=="SI":
                os.system('cls')
                print("*"*100)
                print(" ")
                for y in opciones:
                    print(y)
                print(" ")
                ayuda=input("Que comodin desea: ")
                print(" ")
                if ayuda=="1" and "1).Llamada a un amigo" in opciones:
                    os.system('cls')
                    opciones.remove("1).Llamada a un amigo")
                    print("*"*100)
                    print(" ")
                    print(f"Estas en el nivel {level}                              Has ganado {ganado}")
                    print(" ")
                    print(preguntas[level][cambio]["pregunta"])
                    print(" ")
                    for x in preguntas[level][cambio]["opciones"]:
                        if x[0]==preguntas[level][cambio]["respuesta"] or x[0]==letra:
                            print(x)
                        else:
                            eleccion.remove(x[0])
                    print(" ")
                    time.sleep(2)
                    print(f"La opción que te da Laura es {eleccion[random.randint(0,len(eleccion)-1)]}")
                    print(" ")
                    comodin=input("Desea un comodin (si) o (no): ").upper()
                    print(" ")
                    if comodin=="SI":
                        os.system('cls')
                        print("*"*100)
                        print(" ")
                        for y in opciones:
                            print(y)
                        print(" ")
                        ayuda=input("Que comodin desea: ")
                        print(" ")
                        if ayuda=="3" and "3).Cambio de pregunta" in opciones:
                            os.system('cls')
                            opciones.remove("3).Cambio de pregunta")
                            cambio +=1
                            print(" ")
                elif ayuda=="3" and "3).Cambio de pregunta" in opciones:
                    os.system('cls')
                    opciones.remove("3).Cambio de pregunta")
                    cambio +=1
                    print(" ")
            elif comodin=="NO":
                respuesta=input("Da la respuesta: ").upper()
                print(" ")
                if respuesta== preguntas[level][cambio]["respuesta"]:
                    ganado=ganacia+ganado
                    print("Felicitaciones respuesta correcta")
                    time.sleep(1)
                    print(" ")
                    level+=1
                    os.system('cls')
                else:
                    print("Fallaste, haz perdido")
                    break 
         elif ayuda=="3" and "3).Cambio de pregunta" in opciones:
            os.system('cls')
            opciones.remove("3).Cambio de pregunta")
            cambio +=1
            print(" ")
         else:
            print("Coloca algo que concuerde")
            time.sleep(2)
            os.system('cls')
      elif comodin=="NO":
         respuesta=input("Da la respuesta: ").upper()
         print(" ")
         if respuesta== preguntas[level][cambio]["respuesta"]:
            ganado=ganacia+ganado
            print("Felicitaciones respuesta correcta")
            time.sleep(1)
            print(" ")
            level+=1
            os.system('cls')
         else:
            print("Fallaste, haz perdido")
            break 
      else:
         print("Coloca algo que concuerde")
         time.sleep(2)
         os.system('cls')
   else:
      respuesta=input("Da la respuesta: ").upper()
      if respuesta== preguntas[level][cambio]["respuesta"]:
         ganado=ganacia+ganado
         print("Felicitaciones respuesta correcta")
         time.sleep(2)
         print(" ")
         level+=1
         os.system('cls')
      else:
         print("Fallaste, haz perdido")
         break
if level == 11:
   os.system('cls')
   print("GANASTE EL JUEGO")

