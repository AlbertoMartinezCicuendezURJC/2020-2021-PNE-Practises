class Dog: #Dog es un objeto y las funciones dentro de la clase son methods
    def __init__(self, name, age): #constructor
        self.name = name #los self.noseque son los atributes
        self.age = age

    def set_name(self, name):
        if self.name == "tueno":
            print("...") #esto se usa para que el usuario tenga que elegir uno de los nombres que sea valido en tu programa

    def set_age(self, age):
        if self.age == 20:
            print("....")

    def sit_down(self):  #para ejecutar esta ---> ares.sit_down()
        print("Yes, I'\n m jumping")

    @staticmethod
    def count_names(name):
        print(name)   #para ejecutar esta ---> Dog.count_names(loquesea)

ares = Dog("ares", 10)

ares.name = "trueno"
ares.age= 20    #Para cambiar la informacion de la clase
ares.sit_down()


#el orden de las funciones en las clases es irrelevante
#IMPORTANTE: si usamos un modulo -> nombremodulo.nombrefuncion, si usamos un method -> self.nombremethod, si usamos un static -> nombreclase.nombrestatic