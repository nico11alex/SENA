def miniMaxSum(arr):
    numMenor=arr[0]
    numMayor=0
    for i in range(0,len(arr)):
        if arr[i]>=numMayor:
            numMayor=arr[i]
        if numMenor>=arr[i]:
            numMenor=arr[i]
    print(f"{sum(arr)-numMayor} {sum(arr)-numMenor}")