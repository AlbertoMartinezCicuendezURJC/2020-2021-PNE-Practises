import sys

#los elementos que pongamos se van a guardar en una lista dentro del modulo
#el argumento de la posicion uno es el nombre del file que estamos ejecutando, en este caso sys.py
#hay que pasar los argumentos cada vez, como un input. cuando run otra vez se pierden los argumentos
#los argumentos son literales, no guardan valores ni nada, solo son strings
#algun uso ---> with open(filename, 'r') as:, para poner sys.argv[1] en vez del filename

print(sys.argv)
for i in range(1, len(sys.argv)):
    print(sys.argv[i], end=",")


count = 0
add = 0
for i in sys.argv:
    try:
        add += i
        count += 1
    except ValueError:
        print("Careful! This is not an integer!")
    except TypeError:
        print("Careful! This is not an integer!")

try:
    print("Average: ", add/count)
except ZeroDivisionError:
    print("al pozo")
print(len(sys.argv[1]))