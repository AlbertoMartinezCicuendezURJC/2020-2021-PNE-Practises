import Class

v1 = Class.Vehicle("Chula", "Renault", 6)
v2 = Class.Vehicle("Wow", "Ferrari", 42342)

print(f"{v1}")
print("===========================")
print(Class.Vehicle.print_seq(v2))

v1.calculate_price() #esto no se va a imprimir
print(v1.calculate_price()) #el v1 y el v2 son el self de los methods
print(v2.calculate_price())

#para ver si la marca esta en alguna de las que eligamos --->
print("===================")
available = ["Lambo", "Ferrari", "Opel"]
instances = [v1, v2]
for i in instances:
    if i.brand in Class.Vehicle.available:
        print("It is avaible!")
    else:
        print("Change it!")
