a = 0
b = 1
l = [a, b]
for i in range(0, 12):
    c = a + b
    a = b
    b = c
    l.append(c)
for element in l:
    print(element, end=" ")







