def fibon(n):
    a = 0
    b = 1
    for i in range(0, n-2):
        c = a + b
        a = b
        b = c
    return c

print("The term is:", fibon(5))
print("The term is:", fibon(10))
print("The term is:", fibon(15))

