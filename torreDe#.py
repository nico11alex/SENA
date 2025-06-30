def staircase(n):
    espacios=[]
    for i in range(0,n):
        espacios.append(" ")
        i +=1
        
    for i in range(1,n+1):
        espacios[-i]="#"
        print(*espacios,sep="")
        i+=1