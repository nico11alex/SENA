#Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes: 
# * - Múltiplos de 3 por la palabra "fizz".
# * - Múltiplos de 5 por la palabra "buzz".
# * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

número=1

while número < 101:
    if número % 3 == 0 and número % 5 == 0:
        print("fizzbuzz")
    elif número % 3 == 0:
        print("fizz")
    elif número % 5 == 0:
        print("buzz")
    else:
        print(número)
    número +=1