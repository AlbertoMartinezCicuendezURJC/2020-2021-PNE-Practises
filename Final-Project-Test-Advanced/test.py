def test(x, y):
    if x == 2:
        return x
    else:
        return x,y


x, y = test(2, 4)
print(x)