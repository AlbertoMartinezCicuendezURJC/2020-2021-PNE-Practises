def sumn(n):
    res = 0
    for i in range(1, n+1):
        res += i
    return res

print("The total sum is", sumn(60))

#si pones el breakpoint en el print, pulsamos "step into" (en funciones)