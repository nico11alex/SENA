def compareTriplets(a, b):
    contador=0
    primerArray=0
    segundoArray=0
    for i in range(0,len(a)):
        if a[contador]>b[contador]:
            primerArray +=1
        elif a[contador]==b[contador]:
            pass
        else:
            segundoArray +=1
        contador +=1
    return f"{primerArray}{segundoArray}"